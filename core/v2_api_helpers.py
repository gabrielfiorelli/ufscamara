# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 15:32:56 2025

@author: BlinkPC
"""

def build_params(defaults: dict = None, overrides: dict = None, exclude: list = None) -> dict:

    params = {}
    combined = {**(defaults or {}), **(overrides or {})}

    for key, value in combined.items():
        if exclude and key in exclude:
            continue
        if value is not None:
            if isinstance(value, (list, tuple, set)):
                params[key] = ",".join(str(v) for v in value)
            else:
                params[key] = value
    return params


def build_api_call(endpoint: str,
                   named_params: dict = None,
                   exclude: list = None,
                   subpath: str = None,
                   paginate: bool = False):
    """
    Executa uma chamada GET genérica para a API da Câmara, com suporte a paginação automática.

    Args:
        endpoint (str): Caminho base do endpoint (ex: "deputados", "votacoes").
        named_params (dict, opcional): Parâmetros capturados via locals().
        exclude (list, opcional): Campos a ignorar.
        subpath (str, opcional): Caminho adicional (ex: "123/votos").
        paginate (bool, opcional): Se True, busca automaticamente todas as páginas.

    Returns:
        dict | list: Se paginate=False, retorna o JSON original.
                     Se paginate=True, retorna uma lista com todos os dados concatenados.
    """
    from util import config_reader
    from core.http_client import http_client
    from core.v2_api_helpers import build_params
    
    config = config_reader.load_config()
    _http = http_client(timeout = config["technical_config"]["timeout"],
                        max_retries = config["technical_config"]["max_retries"],
                        retry_wait = config["technical_config"]["retry_wait"])
    
    base_url = config["api_info"]["base_url"]

    # Monta a URL completa
    api_full_url = f"{base_url}{endpoint}"
    if subpath:
        api_full_url = f"{api_full_url}/{subpath}"

    # Monta parâmetros
    named_params = (named_params or {}).copy()


    exclude = exclude or []
    for key in ["base_url", "endpoint", "api_full_url", "extra", "paginate"]:
        named_params.pop(key, None)
    for key in exclude:
        named_params.pop(key, None)
        
    extra_params = named_params.pop("params", None)
    params = build_params(overrides=named_params)

    if extra_params and isinstance(extra_params, dict):
        params.update(extra_params)
        
    if paginate:
        return _http.get_all_pages(api_full_url, params=params or None)
    else:
        return _http.get(api_full_url, params=params or None)
