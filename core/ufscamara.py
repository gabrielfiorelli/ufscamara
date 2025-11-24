# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 21:09:29 2025

@author: BlinkPC
"""

from core import api_camara_v2
from data import data_manager
from util import json_file_writer as fw
from util import file_utils as fu
from util.logger import logger
from datetime import date
from dateutil.relativedelta import relativedelta
import time
import os

class Ufscamara:
    class_name = 'Ufscamara'
    def __init__(self, config: dict):
        """
        config deve conter algo como:
        {
            "start_year": 2000,
            "api_version": "v2",
            "technical_config": {
                "RESULTS_PER_PAGE": 100,
                "IS_DEBUG": False,
                "MAX_RETRIES": 3,
                "SECONDS_TO_WAIT": 2,
                "RETRY_WAIT": 10
            }
        }
        """
        self.config = config
        self.tc = config["technical_config"]
        self.create_folders()
        self.v2 = api_camara_v2
        self.data_manager = data_manager.DataManager(config)

    def create_folders(self):
        folders = [
            "raw_data_api_v2/votacoes",
            "raw_data_api_v2/votacoes_id",
            "raw_data_api_v2/votacoes_votos",
            "raw_data_api_v2/votacoes_orientacoes",
            "raw_data_api_v2/proposicoes",
            "raw_data_api_v2/proposicoes_id",
            "raw_data_api_v2/proposicoes_autores",
            "raw_data_api_v2/proposicoes_temas",
            "raw_data_api_v2/deputados",
            "raw_data_api_v2/deputados_legislaturas",
            "raw_data_api_v2/deputados_id",
            "raw_data_api_v2/deputados_id_despesas",
            "raw_data_api_v2/legislaturas",
            "raw_data_api_v2/referencias_tiposproposicao",
            "dataframes",
            "logs"
        ]
        
        for folder in folders:
            os.makedirs(folder, exist_ok=True)

    def format_date(self, date):
        return date.strftime("%Y-%m-%d")
    
    def download_tudo(self, endpoints = None):
        
        ################################################################
        ## Votacoes
        ################################################################
        
        if('votacoes' in endpoints):
            logger.info(f'[{self.class_name}] - Buscando todas as votacoes')
            # Busca mes a mes
            result = self.download_todos_arquivos_votacao_v2()
            logger.info(f'[{self.class_name}] - Resultado de votacoes: {result}')
        
        logger.info(f'[{self.class_name}] - Filtrando ids de votacoes')
        votacoes_ids = self.data_manager.carregar_votacoes()["id"].unique().tolist()
        
        if('votacoes_id' in endpoints):
            logger.info(f'[{self.class_name}] - Buscando todas as votacoes.detalhes')
            # Busca por ID de votacao
            result = self.download_arquivos_votacoes_id_v2(votacoes_ids)
            logger.info(f'[{self.class_name}] - Resultado de votacoes.detalhes: {result}')
        
        if('votacoes_votos' in endpoints):
            logger.info(f'[{self.class_name}] - Buscando todas as votacoes.votos')
            # Busca por ID de votacao
            result = self.download_arquivos_votacoes_votos_v2(votacoes_ids)
            logger.info(f'[{self.class_name}] - Resultado de votacoes.votos: {result}')
        
        if('votacoes_orientacoes' in endpoints):
            logger.info(f'[{self.class_name}] - Buscando todas as votacoes.orientacoes')
            # Busca por ID de votacao
            result = self.download_arquivos_votacoes_orientacoes_v2(votacoes_ids)
            logger.info(f'[{self.class_name}] - Resultado de votacoes.votos: {result}')
        
        ################################################################
        ## Proposicoes
        ################################################################
        
        if('proposicoes' in endpoints):
            logger.info(f'[{self.class_name}] - Buscando todas as orientacoes')
            # Busca ano a ano
            result = self.download_todos_arquivos_proposicoes_v2(ano_inicio=1989)
            logger.info(f'[{self.class_name}] - Resultado de proposicoes: {result}')
        
        logger.info(f'[{self.class_name}] - Filtrando ids de proposicoes')
        proposicoes_ids = self.data_manager.carregar_proposicoes()["id"].unique().tolist()
            
        if('proposicoes_id' in endpoints):
            logger.info(f'[{self.class_name}] - Buscando todas as proposicoes.id')
            # Busca por ID de proposicao
            result = self.download_arquivos_proposicoes_id_v2(proposicoes_ids)
            logger.info(f'[{self.class_name}] - Resultado de proposicoes.id: {result}')
            
        if('proposicoes_autores' in endpoints):
            logger.info(f'[{self.class_name}] - Buscando todas as proposicoes.autores')
            # Busca por ID de proposicao
            result = self.download_arquivos_proposicoes_autores_v2(proposicoes_ids)
            logger.info(f'[{self.class_name}] - Resultado de proposicoes.autores: {result}')
            
        if('proposicoes_temas' in endpoints):
            logger.info(f'[{self.class_name}] - Buscando todas as proposicoes.temas')
            # Busca por ID de proposicao
            result = self.download_arquivos_proposicoes_temas_v2(proposicoes_ids)
            logger.info(f'[{self.class_name}] - Resultado de proposicoes.temas: {result}')
            
        ################################################################
        ## Deputados
        ################################################################
    
        if('deputados' in endpoints):
            logger.info(f'[{self.class_name}] - Buscando todos os deputados')
            # Busca id legislatura
            result = self.download_arquivos_deputados_v2(dataInicio = "1989-01-01")
            logger.info(f'[{self.class_name}] - Resultado de deputados: {result}')
            
        deputados_ids = self.data_manager.carregar_deputados()["id"].unique().tolist()
        
        if('deputados_id' in endpoints):
            logger.info(f'[{self.class_name}] - Buscando todas os deputados.id')
            # Busca por ID de deputados
            result = self.download_arquivos_deputados_id_v2(deputados_ids)
            logger.info(f'[{self.class_name}] - Resultado de deputados.id: {result}')
            
        if('deputados_id_despesas' in endpoints):
            logger.info(f'[{self.class_name}] - Buscando todas os deputados.id.despsas')
            # Busca por ID de deputados
            anos = list(range(1989, date.today().year + 1))
            result = self.download_arquivos_deputados_id_despesas_v2(ids = deputados_ids,
                                                                     anos = anos)
            logger.info(f'[{self.class_name}] - Resultado de deputados.id.despesas: {result}')
        
        ################################################################
        ## Legislaturas
        ################################################################
        
        if('legislaturas' in endpoints):
            logger.info(f'[{self.class_name}] - Buscando todas as legislaturas')
            # Busca por IDs de Legislatura
            result = self.download_todos_arquivos_legislaturas_v2()
            logger.info(f'[{self.class_name}] - Resultado de votacoes: {result}')
        
            
        return None
    
    # As of 2025-09-06 there was two different limits in the API:
    # 1. start_date and end_date should be in the same year.
    # 2. the difference between stard_date and end_date should be less than 3 months.
    # Por esta razão. A busca foi feita dia a dia.
    # De forma a evitar problemas com o tamanho da resposta da requisição.
    # O lado negativo, é que isto torna o processo mais lento.
    #TODO: Deveria ser um método para baixar todas as votações. Desta forma, toda esta lógica acima ficaria em apenas um lugar.
    #TODO: Este método que sabe pegar todas, usa o método que pega dia a dia, apenas acontece que a iteração segue uma lógica pré definida.
    def download_todos_arquivos_votacao_v2(self):
        
        start_date = date(1989, 1, 1)
        end_date = date.today()
        
        result = self.download_arquivos_votacao_v2(start_date, end_date)
            
        return result
    
    # As of 2025-09-06 there was two different limits in the API:
    # 1. start_date and end_date should be in the same year.
    # 2. the difference between stard_date and end_date should be less than 3 months.
    # Por esta razão. A busca foi feita dia a dia.
    # De forma a evitar problemas com o tamanho da resposta da requisição.
    # O lado negativo, é que isto torna o processo mais lento.
    #TODO: Deveria ser um método para baixar todas as votações. Desta forma, toda esta lógica acima ficaria em apenas um lugar.
    #TODO: Este método que sabe pegar todas, usa o método que pega dia a dia, apenas acontece que a iteração segue uma lógica pré definida.
    def download_arquivos_votacao_v2(self,  id=None,
                                            idProposicao=None,
                                            idEvento=None,
                                            idOrgao=None,
                                            dataInicio=None,
                                            dataFim=None):
        type_name = 'votacoes'
        
        datas_verificadas = 0
        datas_ja_existentes = 0
        datas_baixadas = 0
        datas_vazias = 0
        
        logger.info(f'[{self.class_name}] - Downloading {type_name}')
        
        votacoes_dict = fu.get_votacoes_dictionary()
        
        # Loop mes a mes
        delta = relativedelta(months=1)
        current = dataInicio
        total_months = (dataFim.year - dataInicio.year) * 12 + (dataFim.month - dataInicio.month)
        
        while current <= dataFim:
            datas_verificadas += 1
            month_str = current.strftime("%Y_%m")
            
            logger.info(
                f'[{self.class_name}] - Downloading month {month_str}. '
                f'{datas_verificadas} of {total_months} '
                f'({datas_verificadas / total_months * 100:.2f}%);'
            )
            
            if(month_str in votacoes_dict):
                logger.info(f'[{self.class_name}] - Arquivo de {month_str} já existe.')
                datas_ja_existentes += 1
                current += delta
                continue
        
            first_day = current.replace(day=1)
            next_month = current + relativedelta(months=1)
            last_day = next_month - relativedelta(days=1)
        
            dados_api = self.v2.votacoes(id=id,
                                               idProposicao=idProposicao,
                                               idEvento=idEvento,
                                               idOrgao=idOrgao,
                                               dataInicio=first_day.strftime("%Y-%m-%d"),
                                               dataFim=last_day.strftime("%Y-%m-%d"),
                                               pagina=1,
                                               itens=20,
                                               ordem="ASC",
                                               ordenarPor="dataHoraRegistro")
            
            if (dados_api is None):
                datas_vazias += 1
                logger.info(f'[{self.class_name}] - Orientacoes não encontradas para {first_day}')
                logger.info(f'[{self.class_name}] - Waiting {self.tc["seconds_to_wait"]} seconds')
                current += delta
                time.sleep(self.tc["seconds_to_wait"])
                continue
            
            fw.write_json_content_file_api_v2(dados_api, month_str, type_name)
            datas_baixadas += 1
        
            current += delta
        
        result = {
            "datas_verificadas": datas_verificadas,
            "datas_ja_existentes": datas_ja_existentes,
            "datas_baixadas": datas_baixadas,
        }
            
        return result
    
    def download_arquivos_votacoes_id_v2(self, ids_votacoes=None):
        type_name = 'votacoes_id'
        
        ids_verificados = 0
        ids_ja_existentes = 0
        ids_baixados = 0
        ids_nao_encontrados = 0
        
        total = len(ids_votacoes)
        votos_dict = fu.get_votacoes_id_dictionary()
        
        for id_votacao in ids_votacoes:
            ids_verificados += 1
            progresso = (ids_verificados / total) * 100
            
            logger.info(f'[{self.class_name}] - Processando {ids_verificados}/{total} ({progresso:.2f}%), próximo id {id_votacao}')

            
            if(id_votacao in votos_dict):
                logger.info(f'[{self.class_name}] - detalhes de {id_votacao} já existem.')
                ids_ja_existentes += 1
                continue
            
            logger.info(f'[{self.class_name}] - Download dos detalhes da votacao {id_votacao}')
        
            result = self.v2.votacoes_id(id_votacao)
            
            if(result is None):
                logger.warning(f'[{self.class_name}] - Falha na requisição para {id_votacao}, ignorando.')
                logger.info(f'[{self.class_name}] - Waiting {self.tc["seconds_to_wait"]} seconds')
                time.sleep(self.tc["seconds_to_wait"])
                continue

            result = result.get("dados") if isinstance(result, dict) else None
            has_data = bool(result) 
            
            id_proposicao = id_votacao.split("-")[0]
            
            result = {
                "idProposicao": id_proposicao,
                "idVotacao": id_votacao,
                "dados": result if has_data else {}
            }
            
            fw.write_json_content_file_api_v2(result, id_votacao, type_name)
            
            logger.info(f'[{self.class_name}] - Waiting {self.tc["seconds_to_wait"]} seconds')
            time.sleep(self.tc["seconds_to_wait"])
        
        result = {
                "ids_verificados": ids_verificados,
                "ids_ja_existentes": ids_ja_existentes,
                "ids_baixados": ids_baixados,
                "ids_nao_encontrados": ids_nao_encontrados,
            }
        
        return result
    
    def download_arquivos_votacoes_votos_v2(self, ids_votacoes=None):
        type_name = 'votacoes_votos'
        
        ids_verificados = 0
        ids_ja_existentes = 0
        ids_baixados = 0
        ids_nao_encontrados = 0
        
        total = len(ids_votacoes)
        votos_dict = fu.get_votacoes_votos_dictionary()
        
        for id_votacao in ids_votacoes:
            ids_verificados += 1
            progresso = (ids_verificados / total) * 100
            
            logger.info(f'[{self.class_name}] - Processando {ids_verificados}/{total} ({progresso:.2f}%), próximo id {id_votacao}')
            
            if(id_votacao in votos_dict):
                logger.info(f'[{self.class_name}] - Votos de {id_votacao} já existem.')
                ids_ja_existentes += 1
                continue
            
            logger.info(f'[{self.class_name}] - Download dos votos da votacao {id_votacao}')
        
            votos = self.v2.votacoes_id_votos(id_votacao)
            id_proposicao = id_votacao.split("-")[0]
            
            if votos is None:
                logger.warning(f'[{self.class_name}] - Falha na requisição para {id_votacao}, ignorando.')
                logger.info(f'[{self.class_name}] - Waiting {self.tc["seconds_to_wait"]} seconds')
                time.sleep(self.tc["seconds_to_wait"])
                continue
            
            dados = votos.get("dados") if isinstance(votos, dict) else None
            has_data = bool(dados)
            
            votos_payload = {
                "idProposicao": id_proposicao,
                "idVotacao": id_votacao,
                "votos": dados if has_data else []
            }
            
            if has_data:
                ids_baixados += 1
                logger.info(f'[{self.class_name}] - Votos encontrados para {id_votacao} ({len(dados)} registros).')
            else:
                ids_nao_encontrados += 1
                logger.info(f'[{self.class_name}] - Nenhum voto encontrado para {id_votacao}.')
            
            fw.write_json_content_file_api_v2(votos_payload, id_votacao, type_name)
            
            logger.info(f'[{self.class_name}] - Waiting {self.tc["seconds_to_wait"]} seconds')
            time.sleep(self.tc["seconds_to_wait"])
        
        result = {
                "ids_verificados": ids_verificados,
                "ids_ja_existentes": ids_ja_existentes,
                "ids_baixados": ids_baixados,
                "ids_nao_encontrados": ids_nao_encontrados
            }
        
        return result
    
    def download_arquivos_votacoes_orientacoes_v2(self, ids_votacoes=None):
        type_name = 'votacoes_orientacoes'
        
        ids_verificados = 0
        ids_ja_existentes = 0
        ids_baixados = 0
        ids_nao_encontrados = 0
        
        total = len(ids_votacoes)
        votacoes_dict = fu.get_votacoes_orientacoes_dictionary()
        
        for id_votacao in ids_votacoes:
            ids_verificados += 1
            progresso = (ids_verificados / total) * 100
            
            logger.info(f'[{self.class_name}] - Processando {ids_verificados}/{total} ({progresso:.2f}%), próximo id {id_votacao}')
            
            if(id_votacao in votacoes_dict):
                logger.info(f'[{self.class_name}] - Orientacoes de {id_votacao} já existem.')
                ids_ja_existentes += 1
                continue
            
            logger.info(f'[{self.class_name}] - Download das orientacoes da votacao {id_votacao}')
        
            orientacoes = self.v2.votacoes_id_orientacoes(id_votacao)
            id_proposicao = id_votacao.split("-")[0]
            
            if (orientacoes is None):
                ids_nao_encontrados += 1
                logger.info(f'[{self.class_name}] - Orientacoes não encontradas para {id_votacao}')
                logger.info(f'[{self.class_name}] - Waiting {self.tc["seconds_to_wait"]} seconds')
                time.sleep(self.tc["seconds_to_wait"])
                continue
            
            
            orientacoes = orientacoes.get("dados") if isinstance(orientacoes, dict) else None
            has_data = bool(orientacoes)
            
            orientacoes_payload = {
                "idProposicao": id_proposicao,
                "idVotacao": id_votacao,
                "orientacoes": orientacoes if has_data else []
            }
            
            if has_data:
                ids_baixados += 1
                logger.info(f'[{self.class_name}] - Orientacoes encontrados para {id_votacao} ({len(orientacoes)} registros).')
            else:
                ids_nao_encontrados += 1
                logger.info(f'[{self.class_name}] - Nenhum orientacao encontrado para {id_votacao}.')
        
            fw.write_json_content_file_api_v2(orientacoes_payload, id_votacao, type_name)
            
            logger.info(f'[{self.class_name}] - Waiting {self.tc["seconds_to_wait"]} seconds')
            time.sleep(self.tc["seconds_to_wait"])
        
        result = {
                "ids_verificados": ids_verificados,
                "ids_ja_existentes": ids_ja_existentes,
                "ids_baixados": ids_baixados,
                "ids_nao_encontrados": ids_nao_encontrados
            }
        
        return result
    
    def download_todos_arquivos_proposicoes_v2(self,
                                               siglaTipo=None,
                                               codTipo=None,
                                               idDeputadoAutor=None,
                                               autor=None,
                                               siglaPartidoAutor=None,
                                               idPartidoAutor=None,
                                               siglaUfAutor=None,
                                               keywords=None,
                                               tramitacaoSenado=None,
                                               codSituacao=None,
                                               codTema=None,
                                               ano_inicio=1989,
                                               ano_fim=date.today().year + 1):
        type_name = 'proposicoes'

        anos_verificados = 0
        anos_ja_existentes = 0
        anos_baixados = 0
        anos_nao_encontrados = 0
        
        file_dict = fu.get_proposicoes_dictionary()
        
        for ano_busca in range(ano_inicio, ano_fim):
            anos_verificados += 1
            
            if(str(ano_busca) in file_dict):
                logger.info(f'[{self.class_name}] - Proposicoes do {ano_busca} já existem.')
                anos_ja_existentes += 1
                continue
            
            resultados_ano = self.v2.proposicoes(siglaTipo=siglaTipo,
                                                       codTipo=codTipo,
                                                       idDeputadoAutor=idDeputadoAutor,
                                                       autor=autor,
                                                       siglaPartidoAutor=siglaPartidoAutor,
                                                       idPartidoAutor=idPartidoAutor,
                                                       siglaUfAutor=siglaUfAutor,
                                                       keywords=keywords,
                                                       tramitacaoSenado=tramitacaoSenado,
                                                       codSituacao=codSituacao,
                                                       codTema=codTema,
                                                       ano=ano_busca,
                                                       pagina=1,
                                                       itens=100,
                                                       ordem="ASC",
                                                       ordenarPor="id",
                                                       paginate=True)
            
            if(resultados_ano is None):
                anos_nao_encontrados += 1
                logger.info(f'[{self.class_name}] - Proposicoes não encontradas para ano {ano_busca}')
                logger.info(f'[{self.class_name}] - Waiting {self.tc["seconds_to_wait"]} seconds')
                time.sleep(self.tc["seconds_to_wait"])
                continue
                 
            print(f"TODO: salvar resultado do ano {ano_busca}")
            
            anos_baixados =+ 1
            
            fw.write_json_content_file_api_v2(resultados_ano, ano_busca, type_name)
            logger.info(f'[{self.class_name}] - Waiting {self.tc["seconds_to_wait"]} seconds')
            time.sleep(self.tc["seconds_to_wait"])
        
        result = {
                "anos_verificados": anos_verificados,
                "anos_ja_existentes": anos_ja_existentes,
                "anos_baixados": anos_baixados,
                "anos_nao_encontrados": anos_nao_encontrados
            }
        
        return result
    
    def download_arquivos_proposicoes_id_v2(self, ids=None):
        type_name = 'proposicoes_id'
        
        ids_verificados = 0
        ids_ja_existentes = 0
        ids_baixados = 0
        ids_nao_encontrados = 0
        
        total = len(ids)
        file_dict = fu.get_proposicoes_id_dictionary()
        
        for _id in ids:
            ids_verificados += 1
            progresso = (ids_verificados / total) * 100
            id_str = str(_id)
            
            logger.info(f'[{self.class_name}] - Processando {ids_verificados}/{total} ({progresso:.2f}%), próximo id {id_str}')

            if(id_str in file_dict):
                logger.info(f'[{self.class_name}] - detalhes de {id_str} já existem.')
                ids_ja_existentes += 1
                continue
            
            logger.info(f'[{self.class_name}] - Download dos detalhes da votacao {id_str}')
        
            response = self.v2.proposicoes_id(_id)
            
            if(response is None):
                logger.warning(f'[{self.class_name}] - Falha na requisição para {id_str}, ignorando.')
                logger.info(f'[{self.class_name}] - Waiting {self.tc["seconds_to_wait"]} seconds')
                time.sleep(self.tc["seconds_to_wait"])
                continue

            response = response.get("dados") if isinstance(response, dict) else None
            
            fw.write_json_content_file_api_v2(response, id_str, type_name)
            
            logger.info(f'[{self.class_name}] - Waiting {self.tc["seconds_to_wait"]} seconds')
            time.sleep(self.tc["seconds_to_wait"])
        
        result = {
                "ids_verificados": ids_verificados,
                "ids_ja_existentes": ids_ja_existentes,
                "ids_baixados": ids_baixados,
                "ids_nao_encontrados": ids_nao_encontrados,
            }
        
        return result
    
    def download_arquivos_proposicoes_autores_v2(self, ids=None):
        type_name = 'proposicoes_autores'
        
        ids_verificados = 0
        ids_ja_existentes = 0
        ids_baixados = 0
        ids_nao_encontrados = 0
        
        total = len(ids)
        file_dict = fu.get_proposicoes_autores_dictionary()
           
        for _id in ids:
            ids_verificados += 1
            progresso = (ids_verificados / total) * 100
            id_str = str(_id)
            
            logger.info(f'[{self.class_name}] - Processando {ids_verificados}/{total} ({progresso:.2f}%), próximo id {id_str}')
            
            if(id_str in file_dict):
                logger.info(f'[{self.class_name}] - Autores da proposicao {id_str} já existe.')
                ids_ja_existentes += 1
                continue
            
            logger.info(f'[{self.class_name}] - Download de autores da proposicao {id_str}')
        
            response = self.v2.proposicoes_id_autores(id_str)
            
            if(response is None):
                logger.info(f'[{self.class_name}] - Falha para a proposicao {id_str}')
                continue
            
            response = response.get("dados", [])

            if (response is None or len(response) == 0):
                ids_nao_encontrados += 1
                logger.info(f'[{self.class_name}] - Proposicao não encontrada {id_str}')
                logger.info(f'[{self.class_name}] - Waiting {self.tc["seconds_to_wait"]} seconds')
                time.sleep(self.tc["seconds_to_wait"])
                continue
            
            response = {
                "idProposicao": int(id_str),
                "autores": response
            }
            
            logger.info(f'[{self.class_name}] - Salvando autores da proposicao {id_str}')
            
            fw.write_json_content_file_api_v2(response, id_str, type_name)
            logger.info(f'[{self.class_name}] - Waiting {self.tc["seconds_to_wait"]} seconds')
            time.sleep(self.tc["seconds_to_wait"])
        
        result = {
                "ids_verificados": ids_verificados,
                "ids_ja_existentes": ids_ja_existentes,
                "ids_baixados": ids_baixados,
                "ids_nao_encontrados": ids_nao_encontrados,
            }
        
        return result
    
    def download_arquivos_proposicoes_temas_v2(self, ids=None):
        type_name = 'proposicoes_temas'
        
        ids_verificados = 0
        ids_ja_existentes = 0
        ids_baixados = 0
        ids_nao_encontrados = 0
        
        total = len(ids)
        file_dict = fu.get_proposicoes_temas_dictionary()
           
        for _id in ids:
            ids_verificados += 1
            progresso = (ids_verificados / total) * 100
            id_str = str(_id)
            
            logger.info(f'[{self.class_name}] - Processando {ids_verificados}/{total} ({progresso:.2f}%), próximo id {id_str}')
            
            if(id_str in file_dict):
                logger.info(f'[{self.class_name}] - Temas da proposicao {id_str} já existe.')
                ids_ja_existentes += 1
                continue
            
            logger.info(f'[{self.class_name}] - Download de temas da proposicao {id_str}')
        
            temas = self.v2.proposicoes_id_temas(id_str)
            
            if(temas is None):
                logger.info(f'[{self.class_name}] - Falha para a proposicao {id_str}')
                continue
            
            temas = temas.get("dados") if isinstance(temas, dict) else None
            has_data = bool(temas)
            
            temas_payload = {
                "idProposicao": id_str,
                "temas": temas if has_data else []
            }
            
            if has_data:
                ids_baixados += 1
                logger.info(f'[{self.class_name}] - Temas encontrados para {id_str} ({len(temas)} registros).')
            else:
                ids_nao_encontrados += 1
                logger.info(f'[{self.class_name}] - Nenhum tema encontrado para {id_str}.')
            
            fw.write_json_content_file_api_v2(temas_payload, id_str, type_name)
            logger.info(f'[{self.class_name}] - Waiting {self.tc["seconds_to_wait"]} seconds')
            time.sleep(self.tc["seconds_to_wait"])
        
        result = {
                "ids_verificados": ids_verificados,
                "ids_ja_existentes": ids_ja_existentes,
                "ids_baixados": ids_baixados,
                "ids_nao_encontrados": ids_nao_encontrados,
            }
        
        return result
    
    ################################################################
    ## DEPUTADOS
    ################################################################
    
    def download_arquivos_deputados_v2(self, id=None,
                                             nome=None,
                                             idLegislatura=None,
                                             siglaUf=None,
                                             siglaPartido=None,
                                             siglaSexo=None,
                                             dataInicio=None,
                                             pagina=1,
                                             itens=100):
        type_name = 'deputados'

        
        result = self.v2.deputados(id=None,
                                   nome=None,
                                   idLegislatura=None,
                                   siglaUf=None,
                                   siglaPartido=None,
                                   siglaSexo=None,
                                   dataInicio=dataInicio,
                                   ordenarPor="id",
                                   pagina=1,
                                   itens=100,
                                   paginate=True)
        
        fw.write_json_content_file_api_v2(result, 'all', type_name)
        
        result = {
                "resultados_retornados": len(result)
            }
        
        return result
    
    def download_arquivos_deputados_legislatura_v2(self, ids=None):
        type_name = 'deputados_legislaturas'
        
        ids_verificados = 0
        ids_ja_existentes = 0
        ids_baixados = 0
        ids_nao_encontrados = 0
        
        total = len(ids)
        legislaturas_dict = fu.get_deputados_legislaturas_dictionary()
           
        for _id in ids:
            ids_verificados += 1
            progresso = (ids_verificados / total) * 100
            id_str = str(_id)
            
            logger.info(f'[{self.class_name}] - Processando {ids_verificados}/{total} ({progresso:.2f}%), próximo id {id_str}')
            
            if(id_str in legislaturas_dict):
                logger.info(f'[{self.class_name}] - Deputados das legislatura {_id} já existe.')
                ids_ja_existentes += 1
                continue
            
            logger.info(f'[{self.class_name}] - Download da listagem de deputados da legislatura {_id}')
            
            dados = self.v2.deputados(idLegislatura = _id,
                                            itens = self.tc["results_per_page"],
                                            pagina=1,
                                            ordem="ASC",
                                            ordenarPor="id",
                                            paginate=True)
            
            if(dados is None):
                logger.info(f'[{self.class_name}] - Falha para o deputado {_id}')
                continue
            
            if (len(dados) == 0):
                ids_nao_encontrados += 1
                logger.info(f'[{self.class_name}] - Legislatura não encontrado {_id}')
                logger.info(f'[{self.class_name}] - Waiting {self.tc["seconds_to_wait"]} seconds')
                time.sleep(self.tc["seconds_to_wait"])
                continue
            
            fw.write_json_content_file_api_v2(dados, _id, type_name)
            logger.info(f'[{self.class_name}] - Waiting {self.tc["seconds_to_wait"]} seconds')
            time.sleep(self.tc["seconds_to_wait"])
        
        result = {
                "ids_verificados": ids_verificados,
                "ids_ja_existentes": ids_ja_existentes,
                "ids_baixados": ids_baixados,
                "ids_nao_encontrados": ids_nao_encontrados
            }
        
        return result
    
    def download_arquivos_deputados_id_v2(self, ids):
        type_name = 'deputados_id'
        
        ids_verificados = 0
        ids_ja_existentes = 0
        ids_baixados = 0
        ids_nao_encontrados = 0
        
        total = len(ids)
        deputados_dict = fu.get_deputados_id_dictionary()
           
        for _id in ids:
            ids_verificados += 1
            progresso = (ids_verificados / total) * 100
            id_str = str(_id)
            
            logger.info(f'[{self.class_name}] - Processando {ids_verificados}/{total} ({progresso:.2f}%), próximo id {id_str}')
            
            if(id_str in deputados_dict):
                logger.info(f'[{self.class_name}] - Deputado {id_str} já existe.')
                ids_ja_existentes += 1
                continue
            
            logger.info(f'[{self.class_name}] - Download do deputado {id_str}')
        
            dados = self.v2.deputados_id(_id)
            
            if(dados is None):
                logger.info(f'[{self.class_name}] - Falha para o deputado {id_str}')
                continue
            
            dados = dados.get("dados", [])

            if (dados is None or len(dados) == 0):
                ids_nao_encontrados += 1
                logger.info(f'[{self.class_name}] - Deputado não encontrado {id_str}')
                logger.info(f'[{self.class_name}] - Waiting {self.tc["seconds_to_wait"]} seconds')
                time.sleep(self.tc["seconds_to_wait"])
                continue
            
            fw.write_json_content_file_api_v2(dados, _id, type_name)
            logger.info(f'[{self.class_name}] - Waiting {self.tc["seconds_to_wait"]} seconds')
            time.sleep(self.tc["seconds_to_wait"])
        
        result = {
                "ids_verificados": ids_verificados,
                "ids_ja_existentes": ids_ja_existentes,
                "ids_baixados": ids_baixados,
                "ids_nao_encontrados": ids_nao_encontrados
            }
        
        return result
    
    # Pode ser melhorado.
    # Está fazendo iteração em todos os anos.
    # O ideal é pegar apenas os anos em que o deputado ficou ativo.
    def download_arquivos_deputados_id_despesas_v2(self,
                                                   ids=None,
                                                   anos=None,
                                                   ordem="DESC",
                                                   ordenarPor="ano"
                                                   ):
        type_name = 'deputados_id_despesas'
        
        ids_verificados = 0
        ids_ja_existentes = 0
        ids_baixados = 0
        ids_nao_encontrados = 0
        
        total = len(ids)
        deputados_id_despesas_dict = fu.get_deputados_id_despesas_dictionary()
           
        for _id in ids:
            ids_verificados += 1
            progresso = (ids_verificados / total) * 100
            id_str = str(_id)
            
            logger.info(f'[{self.class_name}] - Processando {ids_verificados}/{total} ({progresso:.2f}%), próximo id {id_str}')
            
            if(id_str in deputados_id_despesas_dict):
                logger.info(f'[{self.class_name}] - Dados para o deputado {id_str} já existe.')
                ids_ja_existentes += 1
                continue
            
            logger.info(f'[{self.class_name}] - Download do deputado {id_str}')
        
            dados = self.v2.deputados_id_despesas(id=_id,
                                                  ano=anos,
                                                  ordem=ordem,
                                                  ordenarPor=ordenarPor,
                                                  paginate=True)
            
            if(dados is None):
                logger.info(f'[{self.class_name}] - Falha para o deputado {id_str}')
                continue

            if (dados is None or len(dados) == 0):
                ids_nao_encontrados += 1
                logger.info(f'[{self.class_name}] - Deputado não encontrado {id_str}')
                logger.info(f'[{self.class_name}] - Waiting {self.tc["seconds_to_wait"]} seconds')
                time.sleep(self.tc["seconds_to_wait"])
                continue
            
            fw.write_json_content_file_api_v2(dados, _id, type_name)
            logger.info(f'[{self.class_name}] - Waiting {self.tc["seconds_to_wait"]} seconds')
            time.sleep(self.tc["seconds_to_wait"])
        
        result = {
                "ids_verificados": ids_verificados,
                "ids_ja_existentes": ids_ja_existentes,
                "ids_baixados": ids_baixados,
                "ids_nao_encontrados": ids_nao_encontrados
            }
        
        return result
    
    ################################################################
    ## LEGISLATURAS
    ################################################################
    
    def download_arquivos_legislaturas_v2(self, ids_legislaturas):
        type_name = 'legislaturas'
        
        ids_verificados = 0
        ids_ja_existentes = 0
        ids_baixados = 0
        ids_nao_encontrados = 0
        arquivos_existentes = []
        
        legislaturas_dict = fu.get_legislaturas_dictionary()
           
        for id_legislatura in ids_legislaturas:
            
            if(id_legislatura.astype(str) in legislaturas_dict):
                logger.info(f'[{self.class_name}] - Legislatura {id_legislatura} já existe.')
                ids_ja_existentes += 1
                continue
            
            logger.info(f'[{self.class_name}] - Download da legislatura {id_legislatura}')
        
            dados = self.v2.legislaturas_id(id_legislatura)
            
            if(dados is None):
                logger.info(f'[{self.class_name}] - Falha para a legislatura {id_legislatura}')
                continue
            
            dados = dados.get("dados", [])

            if (dados is None or len(dados) == 0):
                ids_nao_encontrados += 1
                logger.info(f'[{self.class_name}] - Legislatura não encontrada {id_legislatura}')
                logger.info(f'[{self.class_name}] - Waiting {self.tc["seconds_to_wait"]} seconds')
                time.sleep(self.tc["seconds_to_wait"])
                continue
            
            fw.write_json_content_file_api_v2(dados, id_legislatura, type_name)
            logger.info(f'[{self.class_name}] - Waiting {self.tc["seconds_to_wait"]} seconds')
            time.sleep(self.tc["seconds_to_wait"])
        
        result = {
                "ids_verificados": ids_verificados,
                "ids_ja_existentes": ids_ja_existentes,
                "ids_baixados": ids_baixados,
                "ids_nao_encontrados": ids_nao_encontrados,
                "arquivos_existentes": arquivos_existentes
            }
        
        return result
    
    def download_referencias_tiposproposicao_v2(self):
        type_name = 'referencias_tiposproposicao'
        
        logger.info(f'[{self.class_name}] - Download dos tipos de proposicao')
    
        dados = self.v2.referencias_tiposproposicao()
        
        if(dados is None):
            logger.info(f'[{self.class_name}] - Falha para tipos de proposicao')
            result = {
                    "erro": "dados é NULL"
                }
            return result
        
        dados = dados.get("dados", [])

        if (dados is None or len(dados) == 0):
            result = {
                    "erro": "dados está vazio"
                }
            return result
        
        fw.write_json_content_file_api_v2(dados, "ALL", type_name)
        logger.info(f'[{self.class_name}] - Waiting {self.tc["seconds_to_wait"]} seconds')
        time.sleep(self.tc["seconds_to_wait"])
        
        result = {
                "ids_baixados": len(dados)
            }
        
        return result
    
    def download_todos_arquivos_legislaturas_v2(self):
        result = None
        #TODO
            
        return result