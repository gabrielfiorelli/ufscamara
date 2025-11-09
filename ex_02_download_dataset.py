# -*- coding: utf-8 -*-
"""
Created on Sat Aug 23 19:02:02 2025

@author: BlinkPC
"""

from util import config_reader
from util.logger_config import logger
from datetime import date
from core.ufscamara import Ufscamara
import numpy as np

def format_date(date):
    return date.strftime("%Y-%m-%d")

logger.info('[main] - Starting download step.')

################################################################
## FOCO INICIAL
## 1. Buscar tudo raw e salvar em disco.
## 2. Fazer tratamentos com os dados que tiver em disco
## 3. Descrever as ligações possíveis.
################################################################


################################################################
## Starting UFSCAMARA
################################################################

config = config_reader.load_config()
ufscamara = Ufscamara(config)

# Este arquivo serve para demonstrar os usos dos métodos disponíveis.

# Download
# O método principal de download é sempre responsável por iterar por todo o conteúdo e fazendo o download para o local.
# No entanto, existe a possibilidade de passar filtros para acessar apenas alguns dados específicos.7

################################################################
## DOWNLOAD DATA -> VOTAÇÕES
## votacoes
## Estado: Funcionando
################################################################

data_inicio = date(config["start_year"], 1, 1)
data_fim = date.today()

plen_orgao_id = 180

resultado = ufscamara.download_arquivos_votacao_v2(dataInicio=data_inicio,
                                                   dataFim=data_fim,
                                                   idOrgao=plen_orgao_id)

################################################################
## LOAD DATA            -> VOTACOES
## CREATE DATAFRAME     -> VOTACOES
## Estado: Funcionando
################################################################
## São todas as votações.
## Mas nem todas tem o mesmo valor.
## Votações com orgao = PLEN são as votações nominais.
## Mas é possível ter votações nominais de pedidos de urgência.
## O que importa são: PEC, PLP, PL
## Para saber a SIGLA é necessário pegar o código da proposicao e buscar ela especificamente.
## Um código de votação como 2552333-8 significa que a proposicao é a 2552333 (sem o que vier após o -)
################################################################

votacoes_df = ufscamara.carregar_votacoes()

ufscamara.salvar_dataframe(votacoes_df, 'votacoes')

votacoes_df = ufscamara.carregar_dataframe('votacoes')

votacoes_df.info()

################################################################
## DOWNLOAD DATA -> VOTACOES_ID
## votacoes/{id}/id
## Estado: Funcionando
################################################################

votacoes_df = ufscamara.carregar_dataframe('votacoes')

## Download PLEN
orgaos = ['PLEN']
votacoes_plenario_ids = votacoes_df[votacoes_df['siglaOrgao'] == 'PLEN'].sort_values("data", ascending=False)
# 24142

resultado = ufscamara.download_arquivos_votacoes_id_v2(votacoes_plenario_ids['id'])

################################################################
## LOAD DATA            -> VOTACOES_ID
## CREATE DATAFRAME     -> VOTACOES_ID
## Estado: Funcionando
################################################################

votacoes_id_df = ufscamara.carregar_votacoes_id()

ufscamara.salvar_dataframe(votacoes_df, 'votacoes_id')

votacoes_id_df = ufscamara.carregar_dataframe('votacoes_id')

################################################################
## DOWNLOAD DATA -> VOTACOES_VOTOS
## votacoes/{id}/votos
## Estado: Funcionando
################################################################

votacoes_df = ufscamara.carregar_dataframe('votacoes')

## Download PLEN
orgaos = ['PLEN']
votacoes_plenario_ids = votacoes_df[votacoes_df['siglaOrgao'] == 'PLEN'].sort_values("data", ascending=False)
# 24142

resultado = ufscamara.download_arquivos_votacoes_votos_v2(votacoes_plenario_ids['id'])

################################################################
## LOAD DATA            -> VOTACOES_VOTOS
## CREATE DATAFRAME     -> VOTACOES_VOTOS
## Estado: Funcionando
################################################################

votos_df = ufscamara.carregar_votacoes_votos()

ufscamara.salvar_dataframe(votos_df, 'votacoes_votos')

votos_df = ufscamara.carregar_dataframe('votacoes_votos')

votos_df.info()

################################################################
## DOWNLOAD DATA -> VOTACOES_ORIENTACOES
## votacoes/{id}/orientacoes
## Estado: Funcionando
################################################################

votacoes_df = ufscamara.carregar_dataframe('votacoes')

## Download PLEN
orgaos = ['PLEN']
votacoes_plenario_ids = votacoes_df[votacoes_df['siglaOrgao'] == 'PLEN'].sort_values("data", ascending=False)
resultado = ufscamara.download_arquivos_votacoes_orientacoes_v2(votacoes_plenario_ids['id'])

################################################################
## LOAD DATA            -> VOTACOES_ORIENTACOES
## CREATE DATAFRAME     -> VOTACOES_ORIENTACOES
## Estado: Funcionando
################################################################

votacoes_orientacoes_df = ufscamara.carregar_votacoes_orientacoes()

ufscamara.salvar_dataframe(votacoes_orientacoes_df, 'votacoes_orientacoes')

votacoes_orientacoes_df = ufscamara.carregar_dataframe('votacoes_orientacoes')

votacoes_orientacoes_df.info()

################################################################
## DOWNLOAD DATA -> PROPOSICOES ID
## proposicoes/{id}
## Estado: Funcionando
################################################################

# TODO:
# A lista de proposições é o id sem o sufixo -XXX ou -XX
# A proposição trás informações de qual é a mãe dela.
# Este inclusive é o link entre a API antiga e a API nova.
# Para ter o tipo de proposicao é preciso fazer busca aqui.
# A partir daqui podemos saber se é: PL, REQ e etc.

votacoes_df = ufscamara.carregar_dataframe('votacoes')
proposicoes_buscar = np.sort(votacoes_df['idProposicao'].unique())

resultado = ufscamara.download_arquivos_proposicoes_id_v2(proposicoes_buscar)

################################################################
## LOAD DATA            -> PROPOSICOES_ID
## CREATE DATAFRAME     -> PROPOSICOES_ID
## Estado: Funcionando
################################################################

proposicoes_id_df = ufscamara.carregar_proposicoes_id()

ufscamara.salvar_dataframe(proposicoes_id_df, 'proposicoes_id')

proposicoes_id_df = ufscamara.carregar_dataframe('proposicoes_id')

proposicoes_id_df.info()

################################################################
## DOWNLOAD DATA        -> PROPOSICOES_TEMAS
## proposicoes/{id}/temas
## Estado: Funcionando
################################################################

votacoes_df = ufscamara.carregar_dataframe('votacoes')
proposicoes_buscar = np.sort(votacoes_df['idProposicao'].unique())

resultado = ufscamara.download_arquivos_proposicoes_temas_v2(proposicoes_buscar)

################################################################
## LOAD DATA            -> PROPOSICOES_TEMAS
## CREATE DATAFRAME     -> PROPOSICOES_TEMAS
## Estado: Funcionando
################################################################

proposicoes_temas_df = ufscamara.carregar_proposicoes_temas()

ufscamara.salvar_dataframe(proposicoes_temas_df, 'proposicoes_temas')

proposicoes_temas_df = ufscamara.carregar_dataframe('proposicoes_temas')

proposicoes_temas_df.info()

################################################################
## DOWNLOAD DATA        -> DEPUTADOS (por legislatura)
## deputados
## Estado:  Funcionando
## VERIFICAR:
##      Talvez possa ser removido, visto que aqui é buscado pelos ids dos votos
##      Deputados não está sendo usado ainda no dataset final
################################################################

votos_df = ufscamara.carregar_dataframe('votacoes_votos')

ids_legislaturas = np.sort(votos_df['deputado_.idLegislatura'].unique())

resultado = ufscamara.download_arquivos_deputados_legislatura_v2(ids_legislaturas)

################################################################
## LOAD DATA            -> DEPUTADOS_LEGISLATURA
## CREATE DATAFRAME     -> DEPUTADOS_LEGISLATURA
## Estado: Funcionando
################################################################

deputados_df = ufscamara.carregar_deputados_legislaturas()

ufscamara.salvar_dataframe(deputados_df, 'deputados_legislatura')

deputados_df = ufscamara.carregar_dataframe('deputados_legislatura')

################################################################
## DOWNLOAD DATA        -> REFERENCIAS_TIPOSPROPOSICAO
## referencias/tiposProposicao
## Estado: Funcionando
################################################################

resultado = ufscamara.download_referencias_tiposproposicao_v2()

################################################################
## LOAD DATA            -> REFERENCIAS_TIPOSPROPOSICAO
## CREATE DATAFRAME     -> REFERENCIAS_TIPOSPROPOSICAO
## Estado: Funcionando
################################################################

tipos_proposicao_df = ufscamara.carregar_referencias_tiposproposicao()

ufscamara.salvar_dataframe(tipos_proposicao_df, 'referencias_tiposproposicao')

tipos_proposicao_df = ufscamara.carregar_dataframe('referencias_tiposproposicao')

################################################################
## Até aqui foi o exemplo de como utilizar as funções da UFSCamara para conseguir os dados.
## Por fim, ainda é necessário juntar os dados de forma que possam ser úteis.
## O uso para montagem e exploração dos dados está como exemplo no outro arquivo de ex_02
################################################################