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
## DOWNLOAD TUDO
###############################################################################

endpoints_para_buscar = [
    #'votacoes',
    #'votacoes_id',
    #'votacoes_votos',
    #'votacoes_orientacoes',
    #'proposicoes',
    #'proposicoes_id',
    #'proposicoes_autores',
    'proposicoes_temas'
    ]

result = ufscamara.download_tudo(endpoints_para_buscar)

################################################################
## DOWNLOAD TUDO - PARTE A PARTE
################################################################

config = config_reader.load_config()
ufscamara = Ufscamara(config)

resultado = ufscamara.download_todos_arquivos_votacao_v2()
resultado = ufscamara.download_todos_arquivos_proposicoes_v2()

votacoes_df = ufscamara.reader.carregar_dataframe('votacoes')
resultado = ufscamara.download_arquivos_votacoes_votos_v2(votacoes_df['id'])