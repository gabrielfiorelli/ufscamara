# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 00:10:55 2024

@author: BlinkHome
"""

import json
import os
from util.logger import logger

# def create_dict(file_list, prefix_pattern):
#     result_dict = {}
    
#     for file_path in file_list:
#         file_name = os.path.basename(file_path) 

#         if file_name.startswith(prefix_pattern) and file_name.endswith(".json"):
#             dict_key = file_name[len(prefix_pattern):-len(".json")]
#             result_dict[dict_key] = file_path
#     return result_dict

# def get_votacoes_dictionary():
#     files = get_file_list_v2('v2', "votacoes")
#     files_dict = create_dict(files, "votacoes_")
#     return files_dict

# def get_votacoes_id_dictionary():
#     files = get_file_list_v2('v2', "votacoes_id")
#     files_dict = create_dict(files, "votacoes_id_")
#     return files_dict

# def get_votacoes_votos_dictionary():
#     files = get_file_list_v2('v2', "votacoes_votos")
#     files_dict = create_dict(files, "votacoes_votos_")
#     return files_dict

# def get_proposicoes_dictionary():
#     files = get_file_list_v2('v2', "proposicoes")
#     files_dict = create_dict(files, "proposicoes_")
#     return files_dict

# def get_proposicoes_id_dictionary():
#     files = get_file_list_v2('v2', "proposicoes_id")
#     files_dict = create_dict(files, "proposicoes_id_")
#     return files_dict

# def get_proposicoes_autores_dictionary():
#     files = get_file_list_v2('v2', "proposicoes_autores")
#     files_dict = create_dict(files, "proposicoes_autores_")
#     return files_dict

# def get_proposicoes_temas_dictionary():
#     files = get_file_list_v2('v2', "proposicoes_temas")
#     files_dict = create_dict(files, "proposicoes_temas_")
#     return files_dict

# def get_votacoes_orientacoes_dictionary():
#     files = get_file_list_v2('v2', "votacoes_orientacoes")
#     files_dict = create_dict(files, "votacoes_orientacoes_")
#     return files_dict

# def get_deputados_dictionary():
#     files = get_file_list_v2('v2', "deputados")
#     files_dict = create_dict(files, "deputados_")
#     return files_dict

# def get_deputados_id_dictionary():
#     files = get_file_list_v2('v2', "deputados_id")
#     files_dict = create_dict(files, "deputados_id_")
#     return files_dict

# def get_deputados_legislaturas_dictionary():
#     files = get_file_list_v2('v2', "deputados_legislaturas")
#     files_dict = create_dict(files, "deputados_legislaturas_")
#     return files_dict

# def get_legislaturas_dictionary():
#     files = get_file_list_v2('v2', "legislaturas")
#     files_dict = create_dict(files, "legislaturas_")
#     return files_dict

# def get_file_list_v2(api_version, file_type, name_filter = ''):
    
#     files = []
#     if(api_version == 'v2'):
        
#         base_folder = 'raw_data_api_v2'
#         folder_path = f'{base_folder}/{file_type}/'
        
#         print(folder_path)
        
#         for file_name in os.listdir(folder_path):
#             full_path = os.path.join(folder_path, file_name)
#             if name_filter in file_name and file_name.endswith('.json') and os.path.isfile(full_path):
#                 files.append(full_path)
    
    
#     return files

# def check_file_exists_format(file_type, parameter, file_format):
#     file_name = f'raw_data/{file_type}/{file_type}_{parameter}.{file_format}'
    
#     file_exists = os.path.isfile(file_name)
#     return file_exists

# def check_file_exists_api_v1(file_type, parameter):
#     file_name = f'raw_data_api_v1/{file_type}/{file_type}_{parameter}.json'
    
#     file_exists = os.path.isfile(file_name)
#     return file_exists

def get_file_list(folder_path, name_filter):
    files = []
    for file_name in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file_name)
        if name_filter in file_name and file_name.endswith('.json') and os.path.isfile(full_path):
            files.append(full_path)
    return files
    
# def read_json_file_api_v1(name_filter):
#     files = get_file_list(f"raw_data_api_v1/{name_filter}/", name_filter)
#     json_contents = []
    
#     for file in files:
#         with open(file, 'r', encoding='utf-8') as file:
#             try:
#                 json_content = json.load(file)
#                 json_contents.append(json_content)
#             except json.JSONDecodeError as e:
#                 logger.info(f'[read_json_file] - Error decoding JSON from file {file}: {e}')
#     return json_contents


################################################################
## READ API RAW DATA
################################################################

def read_votacoes_json_file_v2():
    data_folder = 'raw_data_api_v2'
    name_filter = 'votacoes'
    files = get_file_list(f"{data_folder}/{name_filter}/", name_filter)
    json_contents = []
    
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            try:
                json_content = json.load(f)
                for obj in json_content:
                    obj["__source_file__"] = os.path.basename(filepath)
                json_contents.extend(json_content)
            except json.JSONDecodeError as e:
                logger.info(f'[read_json_file] - Error decoding JSON from file {filepath}: {e}')
    return json_contents

def read_votacoes_id_json_file_v2():
    data_folder = 'raw_data_api_v2'
    name_filter = 'votacoes_id'
    files = get_file_list(f"{data_folder}/{name_filter}/", name_filter)
    json_contents = []
    
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            try:
                json_content = json.load(f)
                json_contents.append(json_content)
            except json.JSONDecodeError as e:
                logger.info(f'[read_json_file] - Error decoding JSON from file {filepath}: {e}')
    return json_contents

def read_votacoes_votos_json_file_v2():
    data_folder = 'raw_data_api_v2'
    name_filter = 'votacoes_votos'
    files = get_file_list(f"{data_folder}/{name_filter}/", name_filter)
    json_contents = []
    
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            try:
                json_content = json.load(f)
                json_contents.append(json_content)
            except json.JSONDecodeError as e:
                logger.info(f'[read_json_file] - Error decoding JSON from file {filepath}: {e}')
    return json_contents

def read_votacoes_orientacoes_json_file_v2():
    data_folder = 'raw_data_api_v2'
    name_filter = 'votacoes_orientacoes'
    files = get_file_list(f"{data_folder}/{name_filter}/", name_filter)
    json_contents = []
    
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            try:
                json_content = json.load(f)
                json_contents.append(json_content)
            except json.JSONDecodeError as e:
                logger.info(f'[read_json_file] - Error decoding JSON from file {filepath}: {e}')
    return json_contents

def read_proposicoes_temas_json_file_v2():
    data_folder = 'raw_data_api_v2'
    name_filter = 'proposicoes_temas'
    files = get_file_list(f"{data_folder}/{name_filter}/", name_filter)
    json_contents = []
    
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            try:
                json_content = json.load(f)
                json_contents.append(json_content)
            except json.JSONDecodeError as e:
                logger.info(f'[read_json_file] - Error decoding JSON from file {filepath}: {e}')
    return json_contents

def read_proposicoes_json_file_v2():
    data_folder = 'raw_data_api_v2'
    name_filter = 'proposicoes'
    files = get_file_list(f"{data_folder}/{name_filter}/", name_filter)
    json_contents = []
    
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            try:
                json_content = json.load(f)
                json_contents.extend(json_content)
            except json.JSONDecodeError as e:
                logger.info(f'[read_json_file] - Error decoding JSON from file {filepath}: {e}')
    return json_contents

def read_proposicoes_id_json_file_v2():
    data_folder = 'raw_data_api_v2'
    name_filter = 'proposicoes_id'
    files = get_file_list(f"{data_folder}/{name_filter}/", name_filter)
    json_contents = []
    
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            try:
                json_content = json.load(f)
                json_contents.append(json_content)
            except json.JSONDecodeError as e:
                logger.info(f'[read_json_file] - Error decoding JSON from file {filepath}: {e}')
    return json_contents

################################################################
## DEPUTADOS
################################################################

def read_deputados_json_file_v2():
    data_folder = 'raw_data_api_v2'
    name_filter = 'deputados'
    files = get_file_list(f"{data_folder}/{name_filter}/", name_filter)
    
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            try:
                json_content = json.load(f)
            except json.JSONDecodeError as e:
                logger.info(f'[read_json_file] - Error decoding JSON from file {filepath}: {e}')
    return json_content

def read_deputados_legislaturas_json_file_v2():
    data_folder = 'raw_data_api_v2'
    name_filter = 'deputados_legislaturas'
    files = get_file_list(f"{data_folder}/{name_filter}/", name_filter)
    json_contents = []
    
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            try:
                json_content = json.load(f)
                json_contents.extend(json_content)
            except json.JSONDecodeError as e:
                logger.info(f'[read_json_file] - Error decoding JSON from file {filepath}: {e}')
    return json_contents

def read_deputados_id_json_file_v2():
    data_folder = 'raw_data_api_v2'
    name_filter = 'deputados_id'
    files = get_file_list(f"{data_folder}/{name_filter}/", name_filter)
    json_contents = []
    
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            try:
                json_content = json.load(f)
                json_contents.append(json_content)
            except json.JSONDecodeError as e:
                logger.info(f'[read_json_file] - Error decoding JSON from file {filepath}: {e}')
    return json_contents

def read_deputados_id_despesas_json_file_v2():
    data_folder = 'raw_data_api_v2'
    name_filter = 'deputados_id_despesas'
    files = get_file_list(f"{data_folder}/{name_filter}/", name_filter)
    json_contents = []
    
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            try:
                json_content = json.load(f)
                json_contents.extend(json_content)
            except json.JSONDecodeError as e:
                logger.info(f'[read_json_file] - Error decoding JSON from file {filepath}: {e}')
    return json_contents

################################################################
## LEGISLATURAS
################################################################

def read_legislaturas_json_file_v2():
    data_folder = 'raw_data_api_v2'
    name_filter = 'legislaturas'
    files = get_file_list(f"{data_folder}/{name_filter}/", name_filter)
    json_contents = []
    
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            try:
                json_content = json.load(f)
                json_contents.append(json_content)
            except json.JSONDecodeError as e:
                logger.info(f'[read_json_file] - Error decoding JSON from file {filepath}: {e}')
    return json_contents

def read_referencias_tiposproposicao_json_file_v2():
    data_folder = 'raw_data_api_v2'
    name_filter = 'referencias_tiposproposicao'
    files = get_file_list(f"{data_folder}/{name_filter}/", name_filter)
    
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            try:
                json_content = json.load(f)
            except json.JSONDecodeError as e:
                logger.info(f'[read_json_file] - Error decoding JSON from file {filepath}: {e}')
    return json_content