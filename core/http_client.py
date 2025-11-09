# -*- coding: utf-8 -*-
"""
Created on Sun Aug 24 22:43:35 2025

@author: BlinkPC
"""

import time
import json
import requests
from requests.exceptions import RequestException, Timeout
from util.logger_config import logger

class http_client:
    def __init__(self, timeout=60, max_retries=3, retry_wait=30, headers=None):
        self.timeout = timeout
        self.max_retries = max_retries
        self.retry_wait = retry_wait
        self.session = requests.Session()
        default_headers = {
            "Accept": "application/json",
            "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                           "AppleWebKit/537.36 (KHTML, like Gecko) "
                           "Chrome/139.0.0.0 Safari/537.35")
        }
        
        config_json = json.dumps(
            {
                "timeout": self.timeout,
                "max_retries": self.max_retries,
                "retry_wait": self.retry_wait
            },
            indent=4
        )

        logger.info(f"[http_client] - Inicializado com configurações: {config_json}")
        
        if headers:
            default_headers.update(headers)
        self.session.headers.update(default_headers)

    def get(self, url, params=None):
        
        logger.info(f'[http_client] - URL {url}.')
        logger.info(f'[http_client] - Params {params}.')

        attempt = 0
        success = False
        
        prepared = requests.Request("GET", url, params=params).prepare()
        full_url = prepared.url

        logger.info(f"[http_client] GET {full_url}")
        
        while (not success and attempt < self.max_retries):
            try:
                #response = requests.get(url, headers=self.s.headers, params=params, timeout=self.timeout)
                response = self.session.get(full_url, timeout=self.timeout)
                response.raise_for_status()  # lança erro se status_code != 200
                success = True
                return response.json()
            except Timeout:
                attempt += 1
                logger.warning(f'[http_client] - Timeout na requisição. Tentativa {attempt}/{self.max_retries}. Aguardando {self.retry_wait}s antes de retry...')
                time.sleep(self.retry_wait)
            except RequestException as e:
                attempt += 1
                logger.warning(f'[http_client] - Erro na requisição: {e}. Tentativa {attempt}/{self.max_retries}. Aguardando {self.retry_wait}s...')
                time.sleep(self.retry_wait)

        if (not success):
            logger.error(f'[http_client] - Falha na requisição após {self.max_retries} tentativas. Pulando.')

        # Se chegou aqui, tudo falhou
        return None 
    
    def get_all_pages(self, url, params=None):
        """
        Executa GET em todas as páginas de um endpoint da API da Câmara,
        seguindo os links "next" retornados pela resposta JSON.
    
        Usa o mesmo retry, timeout e sessão configurados no método `get`.
        """
        all_data = []
        next_url = url
        current_params = params
        page = 1
    
        logger.info(f"[http_client] - Iniciando paginação para {url}")
    
        while next_url:
            # 🔹 Reaproveita o teu próprio get() (para manter retry, logs, etc)
            response = self.get(next_url, params=current_params)
    
            if not response or "dados" not in response:
                logger.warning(f"[http_client] - Resposta inesperada na página {page}. Encerrando paginação.")
                break
    
            # 🔹 Acumula os dados
            qtd = len(response["dados"])
            all_data.extend(response["dados"])
            logger.info(f"[http_client] - Página {page}: {qtd} registros coletados.")
    
            # 🔹 Busca link da próxima página
            next_link = next((l["href"] for l in response.get("links", []) if l.get("rel") == "next"), None)
            next_url = next_link
            current_params = None  # o link já traz a query completa
            page += 1
    
        logger.info(f"[http_client] - Paginação concluída ({len(all_data)} registros totais).")
        return all_data