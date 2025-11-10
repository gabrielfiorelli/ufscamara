# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 00:10:55 2024

@author: BlinkHome
"""

import json
import os
from util.logger import logger

def write_json_content_file_api_v2(json_content, date_part, file_type):
    logger.info('[write_json_content_file] - Starting')
    base_folder = 'raw_data_api_v2'
    
    file_name = f'{base_folder}/{file_type}/{file_type}_{date_part}.json'
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    
    with open(file_name, 'w', encoding='utf-8') as json_file:
        json.dump(json_content, json_file, ensure_ascii=False, indent=4)
    
    logger.info(f'[write_json_content_file] - The content of {file_type} was saved as {file_name}')

def write_json_content_file_api_v1(json_content, year, file_type):
    logger.info('[write_json_content_file] - Starting')
    base_folder = 'raw_data_api_v1'
    
    file_name = f'{base_folder}/{file_type}/{file_type}_{year}.json'
    os.makedirs(os.path.dirname(file_name), exist_ok=True) 
    
    
    
    with open(file_name, 'w', encoding='utf-8') as json_file:
        json.dump(json_content, json_file, ensure_ascii=False, indent=4)
    
    logger.info(f'[write_json_content_file] - The content of {file_type} was saved as {file_name}')

# TODO: Make it generic. The differences atm are:
    # the name of the numeric parameter (prop_id vs year)
    # the folder where the data is being saved
def write_json_proposicoes_file_api_v1(json_content, prop_id, file_type):
    logger.info('[write_json_proposicoes_file] - Starting')
    
    os.makedirs(f'raw_data_api_v1/{file_type}', exist_ok=True)
    
    file_name = f'raw_data_api_v1/{file_type}/{file_type}_{prop_id}.json'
    
    with open(file_name, 'w', encoding='utf-8') as json_file:
        json.dump(json_content, json_file, ensure_ascii=False, indent=4)
    
    logger.info(f'[write_json_proposicoes_file] - The content of {file_type} was saved as {file_name}')
    

def write_json_proposicoes_votos_file_api_v1(json_content, prop_id, file_type):
    logger.info('[write_json_proposicoes_votos_file_api_v1] - Starting')
    
    os.makedirs(f'raw_data_api_v1/{file_type}', exist_ok=True)
    
    file_name = f'raw_data_api_v1/{file_type}/{file_type}_{prop_id}.json'
    
    with open(file_name, 'w', encoding='utf-8') as json_file:
        json.dump(json_content, json_file, ensure_ascii=False, indent=4)
    
    logger.info(f'[write_json_proposicoes_votos_file_api_v1] - The content of {file_type} was saved as {file_name}')

def write_json_proposicoes_votos_errors_file_api_v1(json_content, prop_id, file_type):
    logger.info('[write_json_proposicoes_votos_errors_file_api_v1] - Starting')
    
    os.makedirs(f'raw_data_api_v1/{file_type}', exist_ok=True)
    
    file_name = f'raw_data_api_v1/{file_type}/{file_type}_{prop_id}.json'
    
    with open(file_name, 'w', encoding='utf-8') as json_file:
        json.dump(json_content, json_file, ensure_ascii=False, indent=4)
    
    logger.info(f'[write_json_proposicoes_votos_errors_file_api_v1] - The content of {file_type} was saved as {file_name}')