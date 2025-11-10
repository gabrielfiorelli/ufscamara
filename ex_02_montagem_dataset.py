# -*- coding: utf-8 -*-
"""
Created on Sat Aug 23 19:02:02 2025

@author: BlinkPC
"""

from util import config_reader
from core.ufscamara import Ufscamara
import pandas as pd

################################################################
## Starting UFSCAMARA
################################################################

config = config_reader.load_config()
ufscamara = Ufscamara(config)

################################################################
## CARREGANDO DADOS RAW
################################################################

##--------------------
## VOTACOES
##--------------------

votacoes_id_df = ufscamara.data_manager.carregar_dataframe('votacoes_id')
votacoes_id_df['idVotacao'] = votacoes_id_df['id']
cols_to_remove = [
    "id",
    "uri",
    "dataHoraRegistro",
    "uriOrgao",
    "uriEvento",
    "proposicaoObjeto",
    "uriProposicaoObjeto",
    "__source_file__"]

votacoes_id_df = votacoes_id_df.drop(columns=cols_to_remove)
votacoes_id_df['data'] = pd.to_datetime(votacoes_id_df['data'], errors='coerce')
votacoes_id_df['anoVotacao'] = votacoes_id_df['data'].dt.year



##--------------------
## VOTOS
##--------------------

votos_df = ufscamara.data_manager.carregar_dataframe('votacoes_votos')
cols_to_remove = [
    "dataRegistroVoto",
    "deputado_.uri",
    "deputado_.uriPartido",
    "deputado_.idLegislatura",
    "deputado_.urlFoto",
    "deputado_.email"]

votos_df = votos_df.drop(columns=cols_to_remove)

##--------------------
## PROPOSICOES
##--------------------

proposicoes_df = ufscamara.data_manager.carregar_dataframe('proposicoes_id')
df_flat = pd.json_normalize(proposicoes_df["statusProposicao"]).add_prefix("statusProposicao.")
proposicoes_df = pd.concat([proposicoes_df.drop(columns=["statusProposicao"]), df_flat], axis=1)
del df_flat

cols_to_remove = [
    "uri",
    "codTipo",
    "uriOrgaoNumerador",
    "uriAutores",
    "uriPropPrincipal",
    "uriPropAnterior",
    "uriPropPosterior",
    "urlInteiroTeor",
    "urnFinal",
    "texto",
    "justificativa",
    "statusProposicao.sequencia",
    "statusProposicao.uriOrgao",
    "statusProposicao.uriUltimoRelator",
    "statusProposicao.codTipoTramitacao",
    "statusProposicao.codSituacao",
    "statusProposicao.url",
    "statusProposicao.dataHora",
    "dataApresentacao"]

proposicoes_df = proposicoes_df.drop(columns=cols_to_remove)

##--------------------
## TEMAS
##--------------------

temas_df = ufscamara.data_manager.carregar_dataframe('proposicoes_temas')

cols_to_remove = [
    "codTema"]

temas_df = temas_df.drop(columns=cols_to_remove)

##--------------------
## ORIENTACOES
##--------------------

orientacoes_df = ufscamara.data_manager.carregar_dataframe('votacoes_orientacoes')

## codTipoLideranca
## P = Partido
## B = Bloco

cols_to_remove = [
    "codPartidoBloco",
    "uriPartidoBloco"]

orientacoes_df = orientacoes_df.drop(columns=cols_to_remove)
del cols_to_remove

orientacoes_df["siglaPartidoBloco"] = orientacoes_df["siglaPartidoBloco"].str.strip()
orientacoes_df["siglaPartidoBloco"] = orientacoes_df["siglaPartidoBloco"].replace("MINORIA", "Minoria")

##--------------------
## GOVERNOS
##--------------------

governos_df = ufscamara.data_manager.carregar_dataframe('mandatos')
governos_df['idGoverno'] = governos_df['id']

cols_to_remove = [
    "id"]

governos_df = governos_df.drop(columns=cols_to_remove)
del cols_to_remove


################################################################
## JOIN DOS DADOS
################################################################

##--------------------
## votacoes + votos
##--------------------

df_final = votacoes_id_df.merge(votos_df, left_on="idVotacao", right_on="idVotacao", how="left", suffixes=('', '_y'))

df_final = df_final[[c for c in df_final.columns if not c.endswith("_y")]]
df_final = df_final[df_final['siglaOrgao'].notna()]

##--------------------
## votos + votacoes + proposicoes
##--------------------

df_final = df_final.merge(proposicoes_df, left_on="idProposicao", right_on="id", how="left", suffixes=('', '_y'))
df_final = df_final.drop(columns=["id"], errors="ignore")

##--------------------
## votos + votacoes + proposicoes + temas
##--------------------

temas_df = (
    temas_df.groupby("idProposicao")["tema"]
      .unique()  # ou .apply(set) — remove duplicados
      .reset_index(name="lista_temas")
)

df_final = df_final.merge(temas_df, left_on="idProposicao", right_on="idProposicao", how="left", suffixes=('', '_y'))
df_final = df_final.drop(columns=["id"], errors="ignore")

##--------------------
## votos + votacoes + proposicoes + temas + governos
##--------------------

df_final["data"] = pd.to_datetime(df_final["data"], errors="coerce")
governos_df["dataInicio"] = pd.to_datetime(governos_df["dataInicio"], errors="coerce")
governos_df["dataFim"] = pd.to_datetime(governos_df["dataFim"], errors="coerce")

df_final = df_final.sort_values("data")
governos_df = governos_df.sort_values("dataInicio")

df_final = pd.merge_asof(
    df_final, governos_df,
    left_on="data", right_on="dataInicio",
    direction="backward"
)

df_final = df_final.drop(columns=["dataInicio"], errors="ignore")
df_final = df_final.drop(columns=["dataFim"], errors="ignore")

##--------------------
## votos + votacoes + proposicoes + temas + governos = orientacoes
##--------------------

orientacao_governo = orientacoes_df[orientacoes_df["siglaPartidoBloco"] == "Governo"][["idVotacao", "orientacaoVoto"]].rename(columns={"orientacaoVoto": "orientacao_governo"})
orientacao_oposicao = orientacoes_df[orientacoes_df["siglaPartidoBloco"] == "Oposição"][["idVotacao", "orientacaoVoto"]].rename(columns={"orientacaoVoto": "orientacao_oposicao"})
orientacao_maioria  = orientacoes_df[orientacoes_df["siglaPartidoBloco"] == "Maioria"][["idVotacao", "orientacaoVoto"]].rename(columns={"orientacaoVoto": "orientacao_maioria"})
orientacao_minoria  = orientacoes_df[orientacoes_df["siglaPartidoBloco"] == "Minoria"][["idVotacao", "orientacaoVoto"]].rename(columns={"orientacaoVoto": "orientacao_minoria"})

##--------------------
## Filtrar apenas 
##--------------------

#df_final = df_final[df_final["siglaTipo"].isin(["PEC", "PLP", "PL"])].reset_index(drop=True)

df_final = (
    df_final
    .merge(orientacao_governo, on="idVotacao", how="left")
    .merge(orientacao_oposicao, on="idVotacao", how="left")
    .merge(orientacao_maioria,  on="idVotacao", how="left")
    .merge(orientacao_minoria,  on="idVotacao", how="left")
)

################################################################
## JOIN DOS DADOS
################################################################

ufscamara.data_manager.salvar_dataframe(df_final, '2025_11_07_df_completo')
del df_final

################################################################
## EXPLORAÇÃO
################################################################

df = ufscamara.data_manager.carregar_dataframe('2025_11_07_df_completo')

df.info()

################################################################
## Imports
################################################################

import matplotlib.pyplot as plt
import pandas as pd
import os
os.makedirs("imagens", exist_ok=True)

################################################################
## Votações por Ano
################################################################

votacoes_por_ano = (
    df.groupby('anoVotacao')['idVotacao']
      .nunique()
      .reset_index(name='qtd_votacoes')
      .sort_values('anoVotacao')
)


fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(votacoes_por_ano['anoVotacao'], votacoes_por_ano['qtd_votacoes'], color='steelblue')


ax.bar_label(bars, labels=[f'{v:,}'.replace(',', '.') for v in votacoes_por_ano['qtd_votacoes']],
             padding=3, fontsize=9, color='black')

ax.set_title('Quantidade de Votações Distintas por Ano', fontsize=14)
ax.set_xlabel('Ano', fontsize=12)
ax.set_ylabel('Número de Votações', fontsize=12)
ax.grid(axis='y', linestyle='--', alpha=0.6)
plt.xticks(votacoes_por_ano['anoVotacao'], rotation=45, ha='right')
plt.tight_layout()


output_path = os.path.join("imagens", "votacoes_por_ano.png")
plt.savefig(output_path, dpi=300)
print(f"✅ Gráfico salvo em: {output_path}")

plt.close()

################################################################
## Votações com e sem votos por Ano
################################################################

total_por_ano = (
    df.groupby('anoVotacao')['idVotacao']
      .nunique()
      .reset_index(name='total_votacoes')
)

com_votos = df[df['tipoVoto'].notna() & (df['tipoVoto'].str.strip() != '')]
com_votos_por_ano = (
    com_votos.groupby('anoVotacao')['idVotacao']
    .nunique()
    .reset_index(name='votacoes_com_votos')
)

comparacao = pd.merge(total_por_ano, com_votos_por_ano, on='anoVotacao', how='left').fillna(0)
comparacao['votacoes_sem_votos'] = comparacao['total_votacoes'] - comparacao['votacoes_com_votos']

fig, ax = plt.subplots(figsize=(12, 6))

x = range(len(comparacao))
largura = 0.4

bars1 = ax.bar(
    [i - largura/2 for i in x],
    comparacao['votacoes_com_votos'],
    width=largura,
    label='Com votos',
    color='seagreen'
)

bars2 = ax.bar(
    [i + largura/2 for i in x],
    comparacao['votacoes_sem_votos'],
    width=largura,
    label='Sem votos',
    color='lightcoral'
)

ax.bar_label(bars1, padding=2, fontsize=7, color='black')
ax.bar_label(bars2, padding=2, fontsize=7, color='black')

ax.set_title('Comparação: Votações com e sem votos por Ano', fontsize=14)
ax.set_xlabel('Ano', fontsize=12)
ax.set_ylabel('Número de Votações', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(comparacao['anoVotacao'], rotation=45, ha='right')
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()

os.makedirs("imagens", exist_ok=True)
output_path = os.path.join("imagens", "votacoes_com_e_sem_votos_por_ano.png")
plt.savefig(output_path, dpi=300)
print(f"✅ Gráfico salvo em: {output_path}")

plt.close()

print("\nResumo (votações por ano):")
print(comparacao.head())

################################################################
## Votações por Governo
################################################################

votacoes_por_governo = (
    df.groupby(['idGoverno', 'alias'])['idVotacao']
      .nunique()
      .reset_index(name='qtd_votacoes')
      .sort_values('idGoverno')  # mantém ordem cronológica
)

fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(votacoes_por_governo['alias'], votacoes_por_governo['qtd_votacoes'], color='royalblue')

ax.bar_label(
    bars,
    labels=[f'{int(v):,}'.replace(',', '.') for v in votacoes_por_governo['qtd_votacoes']],
    padding=3,
    fontsize=9,
    color='black'
)

ax.set_title('Quantidade de Votações Distintas por Governo', fontsize=14)
ax.set_xlabel('Governo', fontsize=12)
ax.set_ylabel('Número de Votações', fontsize=12)
ax.grid(axis='y', linestyle='--', alpha=0.6)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

output_path = os.path.join("imagens", "votacoes_por_governo.png")
plt.savefig(output_path, dpi=300)
print(f"✅ Gráfico salvo em: {output_path}")

plt.close()

################################################################
## Votações por Tipo de Proposição (siglaTipo)
################################################################

votacoes_por_tipo = (
    df.groupby('siglaTipo')['idVotacao']
      .nunique()
      .reset_index(name='qtd_votacoes')
      .sort_values('qtd_votacoes', ascending=False)
)

fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(votacoes_por_tipo['siglaTipo'], votacoes_por_tipo['qtd_votacoes'], color='steelblue')

ax.bar_label(
    bars,
    labels=[f'{int(v):,}'.replace(',', '.') for v in votacoes_por_tipo['qtd_votacoes']],
    padding=3,
    fontsize=9,
    color='black'
)

ax.set_title('Quantidade de Votações Distintas por Tipo de Proposição', fontsize=14)
ax.set_xlabel('Tipo de Proposição (siglaTipo)', fontsize=12)
ax.set_ylabel('Número de Votações', fontsize=12)
ax.grid(axis='y', linestyle='--', alpha=0.6)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

output_path = os.path.join("imagens", "votacoes_por_tipo.png")
plt.savefig(output_path, dpi=300)
print(f"✅ Gráfico salvo em: {output_path}")

plt.close()

################################################################
## Votações por Tipo de Proposição por Ano
################################################################

votacoes_por_ano_tipo = (
    df.groupby(['anoVotacao', 'siglaTipo'])['idVotacao']
      .nunique()
      .reset_index(name='qtd_votacoes')
)

tipos_principais = ["PL", "MPV", "PDC", "PEC", "PLP", "PRC", "PDL"]
votacoes_por_ano_tipo = votacoes_por_ano_tipo[votacoes_por_ano_tipo['siglaTipo'].isin(tipos_principais)]

votacoes_pivot = votacoes_por_ano_tipo.pivot(index='anoVotacao', columns='siglaTipo', values='qtd_votacoes').fillna(0)

fig, ax = plt.subplots(figsize=(12, 6))

for tipo in votacoes_pivot.columns:
    ax.plot(votacoes_pivot.index, votacoes_pivot[tipo], marker='o', label=tipo)

ax.axvspan(2020, 2021, color='lightcoral', alpha=0.2, label='Pandemia (2020–2021)')

ax.set_title('Evolução das Votações por Tipo de Proposição (por Ano)', fontsize=14)
ax.set_xlabel('Ano', fontsize=12)
ax.set_ylabel('Número de Votações Distintas', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend(title="Tipo de Proposição")
plt.xticks(votacoes_por_ano_tipo['anoVotacao'], rotation=45, ha='right')
plt.tight_layout()

# 🔹 Salva a imagem
output_path = os.path.join("imagens", "votacoes_por_tipo_ano.png")
plt.savefig(output_path, dpi=300)
print(f"✅ Gráfico salvo em: {output_path}")

plt.close()

################################################################
## Votações por Tipo de Proposição por Ano (com pelo menos 1 voto)
################################################################

df_com_votos = df[df['tipoVoto'].notna() & (df['tipoVoto'].str.strip() != '')]

votacoes_por_ano_tipo_com_votos = (
    df_com_votos.groupby(['anoVotacao', 'siglaTipo'])['idVotacao']
      .nunique()
      .reset_index(name='qtd_votacoes')
)

tipos_principais = ["PL", "MPV", "PDC", "PEC", "PLP", "PRC", "PDL"]
votacoes_por_ano_tipo_com_votos = votacoes_por_ano_tipo_com_votos[
    votacoes_por_ano_tipo_com_votos['siglaTipo'].isin(tipos_principais)
]

votacoes_pivot = (
    votacoes_por_ano_tipo_com_votos
    .pivot(index='anoVotacao', columns='siglaTipo', values='qtd_votacoes')
    .fillna(0)
)

fig, ax = plt.subplots(figsize=(12, 6))

for tipo in votacoes_pivot.columns:
    ax.plot(
        votacoes_pivot.index,
        votacoes_pivot[tipo],
        marker='o',
        label=tipo
    )

ax.axvspan(2020, 2021, color='lightcoral', alpha=0.2, label='Pandemia (2020–2021)')

ax.set_title('Evolução das Votações com Votos por Tipo de Proposição (por Ano)', fontsize=14)
ax.set_xlabel('Ano', fontsize=12)
ax.set_ylabel('Número de Votações com Votos', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend(title="Tipo de Proposição")
plt.xticks(votacoes_pivot.index, rotation=45, ha='right')
plt.tight_layout()

os.makedirs("imagens", exist_ok=True)
output_path = os.path.join("imagens", "votacoes_por_tipo_ano_com_votos.png")
plt.savefig(output_path, dpi=300)
print(f"✅ Gráfico salvo em: {output_path}")

plt.close()

################################################################
## Percentual de Votações sem Votos Registrados por Ano
################################################################

assert 'tipoVoto' in df.columns and 'anoVotacao' in df.columns, "Colunas 'tipoVoto' e 'anoVotacao' são obrigatórias"

votacoes_com_votos = df[df['tipoVoto'].notna() & (df['tipoVoto'].str.strip() != '')].groupby('anoVotacao')['idVotacao'].nunique()

votacoes_totais = df.groupby('anoVotacao')['idVotacao'].nunique()

votacoes_sem_votos = votacoes_totais - votacoes_com_votos.reindex(votacoes_totais.index, fill_value=0)

percentual_sem_votos = (votacoes_sem_votos / votacoes_totais * 100).reset_index(name='pct_sem_votos')
percentual_sem_votos['votacoes_sem_votos'] = votacoes_sem_votos.values
percentual_sem_votos['votacoes_totais'] = votacoes_totais.values

fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(percentual_sem_votos['anoVotacao'], percentual_sem_votos['pct_sem_votos'], color='indianred')

ax.bar_label(
    bars,
    labels=[f"{v:.1f}%" for v in percentual_sem_votos['pct_sem_votos']],
    padding=3,
    fontsize=5,
    color='black'
)

ax.set_title('Percentual de Votações sem Votos Registrados por Ano', fontsize=14)
ax.set_xlabel('Ano', fontsize=12)
ax.set_ylabel('Percentual de Votações sem Votos (%)', fontsize=12)
ax.grid(axis='y', linestyle='--', alpha=0.6)
plt.xticks(percentual_sem_votos['anoVotacao'], rotation=45, ha='right')
plt.tight_layout()

output_path = os.path.join("imagens", "percentual_votacoes_sem_votos_por_ano.png")
plt.savefig(output_path, dpi=300)
print(f"✅ Gráfico salvo em: {output_path}")

plt.close()

print("\nResumo das votações sem votos por ano:")
print(percentual_sem_votos[['anoVotacao', 'votacoes_totais', 'votacoes_sem_votos', 'pct_sem_votos']].round(1))