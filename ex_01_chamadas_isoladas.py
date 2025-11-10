# -*- coding: utf-8 -*-
"""
Created on Sat Aug 23 19:02:02 2025

@author: BlinkPC
"""

from util import config_reader
from core.ufscamara import Ufscamara

################################################################
## Starting UFSCAMARA
## Mostra exemplo de como fazer chamada para cada um dos endpoints mapeados no código da Ufscamara.
################################################################

config = config_reader.load_config()
ufscamara = Ufscamara(config)

###############################################################################
##
## VOTACOES
##
###############################################################################

################################################################
## votacoes_params
################################################################

parameters = {
    "dataInicio": '2025-02-04',
    "dataFim": '2025-04-04',
    "ordenarPor": "dataHoraRegistro",
    "itens": 5,
    "pagina": 1,
    "idOrgao": 180
}

resultado = ufscamara.v2.votacoes_params(parameters)

print(resultado)

parameters = {
    "dataInicio": '2025-02-04',
    "dataFim": '2025-04-04',
    "ordenarPor": "dataHoraRegistro",
    "itens": 100,
    "pagina": 1,
    "idOrgao": 180
}

resultado = ufscamara.v2.votacoes_params(parameters, paginate = True)

print(resultado)


################################################################
## votacoes
################################################################

resultado = ufscamara.v2.votacoes(dataInicio='2025-02-04',
                                  dataFim='2025-03-04',
                                  ordenarPor='dataHoraRegistro',
                                  ordem='asc',
                                  itens=10,
                                  pagina=1,
                                  idOrgao=180, #PLEN
                                  paginate=True
                                  )

print(resultado)

################################################################
## votacoes/{id}
################################################################

id_votacao = "2145819-51"
resultado = ufscamara.v2.votacoes_id(id_votacao)

print(resultado)

################################################################
## votacoes/{id}/orientacoes
################################################################

id_votacao = "2145819-51"
resultado = ufscamara.v2.votacoes_id_orientacoes(id_votacao)

print(resultado)

id_votacao = "604844-77"
resultado = ufscamara.v2.votacoes_id_orientacoes(id_votacao)

print(resultado)


################################################################
## votacoes/{id}/votos
################################################################

id_votacao = "2145819-51"
resultado = ufscamara.v2.votacoes_id_votos(id_votacao)

print(resultado)

###############################################################################
##
## PROPOSICOES
##
###############################################################################

################################################################
## proposicoes_params
################################################################

parameters = {
    "ano": 2025,
    "siglaTipo": "PL",
    "ordenarPor": "id",
    "itens": 10,
    "pagina": 1,
    "keywords": ["economia", "futebol"],
    "siglaUfAutor": "SC"
}

resultado = ufscamara.v2.proposicoes_params(parameters)

print(resultado)

parameters = {
    "ano": 2025,
    "siglaTipo": "PL",
    "keywords": ["economia", "futebol"],
    "ordenarPor": "id",
    "itens": 10,
    "pagina": 1
}

resultado = ufscamara.v2.proposicoes_params(parameters, paginate = True)

print(resultado)

################################################################
## proposicoes
################################################################

resultado = ufscamara.v2.proposicoes(ano=2025,
                                     siglaTipo="PL",
                                     keywords=["economia", "futebol"],
                                     siglaUfAutor="SC",
                                     ordenarPor="id",
                                     itens=10,
                                     pagina=1)

print(resultado)

resultado = ufscamara.v2.proposicoes(ano=2025,
                                     siglaTipo="PL",
                                     keywords=["economia", "futebol"],
                                     ordenarPor="id",
                                     itens=10,
                                     pagina=1,
                                     paginate=True)

print(resultado)

resultado = ufscamara.v2.proposicoes(ano=2025,
                                     siglaTipo=None,
                                     ordenarPor="id",
                                     itens=10,
                                     pagina=1,
                                     paginate=True)

print(resultado)

################################################################
## proposicoes/{id}
################################################################

id_proposicao = 2503242
resultado = ufscamara.v2.proposicoes_id(id_proposicao)

print(resultado)

################################################################
## proposicoes/{id}/autores
################################################################

id_proposicao = 2503242
resultado = ufscamara.v2.proposicoes_id_autores(id_proposicao)

print(resultado)

################################################################
## proposicoes/{id}/relacionadas
################################################################

id_proposicao = 2503242
resultado = ufscamara.v2.proposicoes_id_relacionadas(id_proposicao)

print(resultado)

################################################################
## proposicoes/{id}/temas
################################################################

id_proposicao = 2503242
resultado = ufscamara.v2.proposicoes_id_temas(id_proposicao)

print(resultado)


################################################################
## proposicoes/{id}/tramitacoes
################################################################

id_proposicao = 2503242
resultado = ufscamara.v2.proposicoes_id_tramitacoes(id_proposicao)

print(resultado)

################################################################
## proposicoes/{id}/votacoes
################################################################

id_proposicao = 2145819
resultado = ufscamara.v2.proposicoes_id_votacoes(id_proposicao)

print(resultado)

###############################################################################
##
## DEPUTADOS
##
###############################################################################

################################################################
## deputados_params
################################################################

parameters = {
    "siglaUf": "SC",
    "siglaSexo": "F",
    "siglaPartido": "PSDB",
    "idLegislatura": 57,
    "pagina": 1,
    "itens": 100
}

# BUG
# Mesmo passando a siglaUF, se passar a legislatura, acaba por retornar todos os deputados.

resultado = ufscamara.v2.deputados_params(parameters)

print(resultado)

parameters = {
    "idLegislatura": 57,
    "pagina": 1,
    "itens": 100
}

# BUG
# Mesmo passando a siglaUF, se passar a legislatura, acaba por retornar todos os deputados.

resultado = ufscamara.v2.deputados_params(parameters, paginate = True)

print(resultado)

################################################################
## deputados
################################################################

resultado = ufscamara.v2.deputados(siglaUf="SC",
                                   siglaSexo="F",
                                   siglaPartido="PSDB",
                                   idLegislatura=57,
                                   pagina=1,
                                   itens=10)

print(resultado)

################################################################
## deputados/{id}
################################################################

id_deputado = 178966
resultado = ufscamara.v2.deputados_id(id_deputado)

print(resultado)

################################################################
## deputados/{id}/despesas
################################################################

id_deputado = 178966
resultado = ufscamara.v2.deputados_id_despesas(id_deputado)

print(resultado)

id_deputado = 178966
resultado = ufscamara.v2.deputados_id_despesas(id_deputado,
                                               ano=2025,
                                               mes=1,
                                               itens=10,
                                               ordenarPor="valorLiquido",
                                               ordem="DESC",
                                               cnpjCpfFornecedor="35168658000191")

print(resultado)

id_deputado = 178966
resultado = ufscamara.v2.deputados_id_despesas(id_deputado,
                                               ano=2025,
                                               itens=10,
                                               ordenarPor="valorLiquido",
                                               ordem="DESC",
                                               paginate=True)

print(resultado)

################################################################
## deputados/{id}/discursos
################################################################

id_deputado = 178966
resultado = ufscamara.v2.deputados_id_discursos(id_deputado)
#TODO: Se não passar parâmetros, retorna somente últimos 7 dias

print(resultado)

id_deputado = 178966
resultado = ufscamara.v2.deputados_id_discursos(id_deputado,
                                               dataInicio='2025-01-01',
                                               dataFim='2025-10-01',
                                               itens=1,
                                               ordenarPor="dataHoraInicio",
                                               ordem="DESC")

print(resultado)

id_deputado = 178966
resultado = ufscamara.v2.deputados_id_discursos(id_deputado,
                                               dataInicio='2025-01-01',
                                               dataFim='2025-10-01',
                                               itens=10,
                                               pagina=1,
                                               ordenarPor="dataHoraInicio",
                                               ordem="DESC",
                                               paginate=True)

print(resultado)


################################################################
## deputados/{id}/eventos
################################################################

id_deputado = 178966
resultado = ufscamara.v2.deputados_id_eventos(id_deputado)

print(resultado)

id_deputado = 178966
resultado = ufscamara.v2.deputados_id_eventos(id_deputado,
                                               dataInicio='2025-01-01',
                                               dataFim='2025-10-01',
                                               itens=1,
                                               ordenarPor="dataHoraInicio",
                                               ordem="DESC")

print(resultado)

id_deputado = 178966
resultado = ufscamara.v2.deputados_id_eventos(id_deputado,
                                               dataInicio='2025-01-01',
                                               dataFim='2025-10-01',
                                               itens=10,
                                               pagina=1,
                                               ordenarPor="dataHoraInicio",
                                               ordem="DESC",
                                               paginate=True)

print(resultado)

################################################################
## deputados/{id}/frentes
################################################################

id_deputado = 178966
resultado = ufscamara.v2.deputados_id_frentes(id_deputado)

print(resultado)

################################################################
## deputados/{id}/historico
################################################################

id_deputado = 178966
resultado = ufscamara.v2.deputados_id_historico(id_deputado)

print(resultado)

################################################################
## deputados/{id}/mandatos_externos
################################################################

id_deputado = 178966
resultado = ufscamara.v2.deputados_id_mandatosExternos(id_deputado)

print(resultado)

################################################################
## deputados/{id}/ocupacoes
################################################################

id_deputado = 178966
resultado = ufscamara.v2.deputados_id_ocupacoes(id_deputado)

print(resultado)

################################################################
## deputados/{id}/orgaos
################################################################

id_deputado = 178966
resultado = ufscamara.v2.deputados_id_orgaos(id_deputado)

print(resultado)

id_deputado = 178966
resultado = ufscamara.v2.deputados_id_orgaos(id_deputado,
                                            dataInicio='2025-01-01',
                                            dataFim='2025-10-01',
                                            itens=1,
                                            ordenarPor="dataInicio",
                                            ordem="DESC")

print(resultado)

id_deputado = 178966
resultado = ufscamara.v2.deputados_id_orgaos(id_deputado,
                                            dataInicio='2025-01-01',
                                            dataFim='2025-10-01',
                                            itens=10,
                                            pagina=1,
                                            ordenarPor="dataInicio",
                                            ordem="DESC",
                                            paginate=True)

print(resultado)

################################################################
## deputados/{id}/profissoes
################################################################

id_deputado = 178966
resultado = ufscamara.v2.deputados_id_profissoes(id_deputado)

print(resultado)

###############################################################################
##
## ORGÃOS
##
###############################################################################

################################################################
## orgaos
################################################################

resultado = ufscamara.v2.orgaos(dataInicio="2020-01-01",
                                dataFim="2025-04-01",
                                pagina=1,
                                itens=100)

print(resultado)

resultado = ufscamara.v2.orgaos(dataInicio="2020-01-01",
                                dataFim="2025-04-01",
                                itens=100,
                                pagina=1,
                                paginate=True)

print(resultado)

################################################################
## orgaos/{id}
################################################################

orgao_id = 539760
resultado = ufscamara.v2.orgaos_id(orgao_id)

print(resultado)

################################################################
## orgaos/{id}/eventos
################################################################

orgao_id = 539725
resultado = ufscamara.v2.orgaos_id_eventos(orgao_id,
                                            dataInicio='2000-01-01',
                                            dataFim='2025-10-01',
                                            itens=1,
                                            ordenarPor="dataHoraInicio",
                                            ordem="DESC")

print(resultado)

orgao_id = 539725
resultado = ufscamara.v2.orgaos_id_eventos(orgao_id,
                                            dataInicio='2000-01-01',
                                            dataFim='2025-10-01',
                                            itens=5,
                                            pagina=1,
                                            ordenarPor="dataHoraInicio",
                                            ordem="DESC",
                                            paginate=True)

print(resultado)


################################################################
## orgaos/{id}/membros
################################################################

orgao_id = 539725
resultado = ufscamara.v2.orgaos_id_membros(orgao_id,
                                            dataInicio='2000-01-01',
                                            dataFim='2025-10-01',
                                            itens=10,
                                            pagina=1)

print(resultado)

orgao_id = 539725
resultado = ufscamara.v2.orgaos_id_membros(orgao_id,
                                            dataInicio='2000-01-01',
                                            dataFim='2025-10-01',
                                            itens=10,
                                            pagina=1,
                                            paginate=True)

print(resultado)

################################################################
## orgaos/{id}/votacoes
################################################################

orgao_id = 180
resultado = ufscamara.v2.orgaos_id_votacoes(orgao_id,
                                            dataInicio='2025-01-01',
                                            dataFim='2025-10-01',
                                            itens=10,
                                            pagina=1)

print(resultado)

orgao_id = 180
resultado = ufscamara.v2.orgaos_id_votacoes(orgao_id,
                                            dataInicio='2025-01-01',
                                            dataFim='2025-10-01',
                                            itens=100,
                                            pagina=1,
                                            paginate=True)

print(resultado)


###############################################################################
##
## PARTIDOS
##
###############################################################################

################################################################
## partidos
################################################################

resultado = ufscamara.v2.partidos(idLegislatura=57,
                                  dataInicio="2022-01-01",
                                  dataFim="2025-04-01",
                                  pagina=1,
                                  itens=10)

print(resultado)

resultado = ufscamara.v2.partidos(idLegislatura=57,
                                  dataInicio="2022-01-01",
                                  dataFim="2025-04-01",
                                  pagina=1,
                                  itens=10,
                                  paginate=True)

print(resultado)


################################################################
## partidos/{id}
################################################################

partido_id = 37907
resultado = ufscamara.v2.partidos_id(partido_id)

print(resultado)

################################################################
## partidos/{id}/lideres
################################################################

partido_id = 36844
resultado = ufscamara.v2.partidos_id_lideres(partido_id,
                                    itens=10,
                                    pagina=1)

print(resultado)

partido_id = 36844
resultado = ufscamara.v2.partidos_id_lideres(partido_id,
                                    itens=2,
                                    pagina=1,
                                    paginate=True)

print(resultado)

################################################################
## partidos/{id}/membros
################################################################

partido_id = 36844
resultado = ufscamara.v2.partidos_id_membros(partido_id,
                                            idLegislatura=57,   
                                            itens=10,
                                            pagina=1)

print(resultado)

partido_id = 36844
resultado = ufscamara.v2.partidos_id_membros(partido_id,
                                            idLegislatura=57,   
                                            itens=10,
                                            pagina=1,
                                            paginate=True)

print(resultado)

###############################################################################
##
## LEGISLATURAS
##
###############################################################################

################################################################
## legislaturas
################################################################

resultado = ufscamara.v2.legislaturas(pagina=1,
                                      itens=100)

print(resultado)

resultado = ufscamara.v2.legislaturas(pagina=1,
                                      itens=10,
                                      paginate=True)

print(resultado)

################################################################
## legislaturas/{id}
################################################################

id_legislatura = 57
resultado = ufscamara.v2.legislaturas_id(id_legislatura)

print(resultado)

################################################################
## legislaturas/{id}/lideres
################################################################

id_legislatura = 57
resultado = ufscamara.v2.legislaturas_id_lideres(id_legislatura,
                                                 itens=10,
                                                 pagina=1)

print(resultado)

id_legislatura = 57
resultado = ufscamara.v2.legislaturas_id_lideres(id_legislatura,
                                                 itens=100,
                                                 pagina=1,
                                                 paginate=True)

print(resultado)

################################################################
## legislaturas/{id}/mesa
################################################################

id_legislatura = 57

resultado = ufscamara.v2.legislaturas_id_mesa(id_legislatura,
                                         dataInicio="2025-01-01",
                                         dataFim="2025-10-01")

print(resultado)


###############################################################################
##
## BLOCOS
##
###############################################################################

################################################################
## blocos
################################################################

resultado = ufscamara.v2.blocos(idLegislatura=57,
                                pagina=1,
                                itens=100)

print(resultado)

resultado = ufscamara.v2.blocos(idLegislatura=57,
                                pagina=1,
                                itens=5,
                                paginate=True)

print(resultado)

################################################################
## blocos/{id}
################################################################

id_bloco = 589

resultado = ufscamara.v2.blocos_id(id_bloco)

print(resultado)

################################################################
## blocos/{id}/partidos
################################################################

id_bloco = 589

resultado = ufscamara.v2.blocos_id_partidos(id_bloco)

print(resultado)

###############################################################################
##
## FRENTES
##
###############################################################################

################################################################
## frentes
################################################################

resultado = ufscamara.v2.frentes(idLegislatura=57,
                                pagina=1,
                                itens=100)

print(resultado)

resultado = ufscamara.v2.frentes(idLegislatura=57,
                                pagina=1,
                                itens=100,
                                paginate=True)

print(resultado)

################################################################
## frentes/{id}
################################################################

id_frente = 54556

resultado = ufscamara.v2.frentes_id(id_frente)

print(resultado)

################################################################
## frentes/{id}/membros
################################################################

id_frente = 54556

resultado = ufscamara.v2.frentes_id_membros(id_frente)

print(resultado)


###############################################################################
##
## GRUPOS
##
###############################################################################

################################################################
## grupos
################################################################

resultado = ufscamara.v2.grupos(pagina=1,
                                itens=100)

print(resultado)

resultado = ufscamara.v2.grupos(pagina=1,
                                itens=100,
                                paginate=True)

print(resultado)

################################################################
## grupos/{id}
################################################################

id_grupo = 74

resultado = ufscamara.v2.grupos_id(id_grupo)

print(resultado)

################################################################
## grupos/{id}/historico
################################################################

id_grupo = 74

resultado = ufscamara.v2.grupos_id_historico(id_grupo)

print(resultado)


################################################################
## grupos/{id}/membros
################################################################

id_grupo = 74
resultado = ufscamara.v2.grupos_id_membros(id_grupo,
                                           dataInicio="2025-01-01",
                                           dataFim="2025-10-01",
                                           ordem="DESC",
                                           ordenarPor="idLegislatura")

print(resultado)

id_grupo = 74
resultado = ufscamara.v2.grupos_id_membros(id_grupo,
                                           dataInicio="2025-01-01",
                                           dataFim="2025-10-01",
                                           ordem="DESC",
                                           ordenarPor="idLegislatura",
                                           paginate=True)

print(resultado)

###############################################################################
##
## EVENTOS
##
###############################################################################

################################################################
## eventos
################################################################

resultado = ufscamara.v2.eventos(dataInicio="2025-01-01",
                                 dataFim="2025-10-01",
                                 idOrgao=537236,
                                 pagina=1,
                                 itens=10)

print(resultado)

resultado = ufscamara.v2.eventos(dataInicio="2025-01-01",
                                 dataFim="2025-10-01",
                                 idOrgao=537236,
                                 pagina=1,
                                 itens=10,
                                 paginate=True)

print(resultado)

################################################################
## eventos/{id}
################################################################

id_evento = 79206

resultado = ufscamara.v2.eventos_id(id_evento)

print(resultado)

################################################################
## eventos/{id}/deputados
################################################################

id_evento = 79206

resultado = ufscamara.v2.eventos_id_deputados(id_evento)

print(resultado)

################################################################
## eventos/{id}/orgaos
################################################################

id_evento = 79206

resultado = ufscamara.v2.eventos_id_orgaos(id_evento)

print(resultado)

################################################################
## eventos/{id}/pauta
################################################################

id_evento = 79206

resultado = ufscamara.v2.eventos_id_pauta(id_evento)

print(resultado)

################################################################
## eventos/{id}/votacoes
################################################################

id_evento = 79206

resultado = ufscamara.v2.eventos_id_votacoes(id_evento)

print(resultado)

###############################################################################
##
## REFERENCIAS
##
###############################################################################

################################################################
## referencias/tiposproposicao
################################################################

resultado = ufscamara.v2.referencias_tiposProposicao()

print(resultado)

################################################################
## referencias/deputados
################################################################

resultado = ufscamara.v2.referencias_deputados()

print(resultado)

################################################################
## referencias/deputados/codSituacao
################################################################

resultado = ufscamara.v2.referencias_deputados_codSituacao()

print(resultado)

################################################################
## referencias/deputados/codTipoProfissao
################################################################

resultado = ufscamara.v2.referencias_deputados_codTipoProfissao()

print(resultado)

################################################################
## referencias/deputados/siglaUF
################################################################

resultado = ufscamara.v2.referencias_deputados_siglaUF()

print(resultado)

################################################################
## referencias/deputados/tipoDespesa
################################################################

resultado = ufscamara.v2.referencias_deputados_tipoDespesa()

print(resultado)

################################################################
## referencias/proposicoes
################################################################

resultado = ufscamara.v2.referencias_proposicoes()

print(resultado)

################################################################
## referencias/proposicoes/codSituacao
################################################################

resultado = ufscamara.v2.referencias_proposicoes_codSituacao()

print(resultado)

################################################################
## referencias/proposicoes/codTema
################################################################

resultado = ufscamara.v2.referencias_proposicoes_codTema()

print(resultado)

################################################################
## referencias/proposicoes/codTipoAutor
################################################################

resultado = ufscamara.v2.referencias_proposicoes_codTipoAutor()

print(resultado)

################################################################
## referencias/proposicoes/codTipoAutor
################################################################

resultado = ufscamara.v2.referencias_proposicoes_codTipoTramitacao()

print(resultado)

################################################################
## referencias/proposicoes/codSiglaTipo
################################################################

resultado = ufscamara.v2.referencias_proposicoes_siglaTipo()

print(resultado)

################################################################
## referencias/situacoesDeputado
################################################################

resultado = ufscamara.v2.referencias_situacoesDeputado()

print(resultado)

################################################################
## referencias/situacoesEvento
################################################################

resultado = ufscamara.v2.referencias_situacoesEvento()

print(resultado)

################################################################
## referencias/situacoesOrgao
################################################################

resultado = ufscamara.v2.referencias_situacoesOrgao()

print(resultado)

################################################################
## referencias/situacoesProposicao
################################################################

resultado = ufscamara.v2.referencias_situacoesProposicao()

print(resultado)

################################################################
## referencias/tiposAutor
################################################################

resultado = ufscamara.v2.referencias_tiposAutor()

print(resultado)

################################################################
## referencias/tiposEvento
################################################################

resultado = ufscamara.v2.referencias_tiposEvento()

print(resultado)

################################################################
## referencias/tiposOrgao
################################################################

resultado = ufscamara.v2.referencias_tiposOrgao()

print(resultado)

################################################################
## referencias/tiposTramitacao
################################################################

resultado = ufscamara.v2.referencias_tiposTramitacao()

print(resultado)

################################################################
## referencias/orgaos
################################################################

resultado = ufscamara.v2.referencias_orgaos()

print(resultado)

################################################################
## referencias/orgaos/codSituacao
################################################################

resultado = ufscamara.v2.referencias_orgaos_codSituacao()

print(resultado)

################################################################
## referencias/orgaos/codTipoOrgao
################################################################

resultado = ufscamara.v2.referencias_orgaos_codTipoOrgao()

print(resultado)

################################################################
## referencias/situacoesOrgaos
################################################################

resultado = ufscamara.v2.referencias_situacoesOrgao()

print(resultado)

################################################################
## referencias/eventos
################################################################

resultado = ufscamara.v2.referencias_eventos()

print(resultado)

################################################################
## referencias/eventos/codSituacaoEvento
################################################################

resultado = ufscamara.v2.referencias_eventos_codSituacaoEvento()

print(resultado)

################################################################
## referencias/eventos/codTipoEvento
################################################################

resultado = ufscamara.v2.referencias_eventos_codTipoEvento()

print(resultado)

################################################################
## referencias/situacoesEvento
################################################################

resultado = ufscamara.v2.referencias_situacoesEvento()

print(resultado)

################################################################
## referencias/situacoesEvento
################################################################

resultado = ufscamara.v2.referencias_tiposEvento()

print(resultado)
