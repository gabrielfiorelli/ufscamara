# -*- coding: utf-8 -*-

import os

def get_file_list_v2(api_version, file_type, name_filter = ''):
    
    files = []
    if(api_version == 'v2'):
        
        base_folder = 'raw_data_api_v2'
        folder_path = f'{base_folder}/{file_type}/'
        
        print(folder_path)
        
        for file_name in os.listdir(folder_path):
            full_path = os.path.join(folder_path, file_name)
            if name_filter in file_name and file_name.endswith('.json') and os.path.isfile(full_path):
                files.append(full_path)
    
    
    return files

def create_dict(file_list, prefix_pattern):
    result_dict = {}
    
    for file_path in file_list:
        file_name = os.path.basename(file_path) 

        if file_name.startswith(prefix_pattern) and file_name.endswith(".json"):
            dict_key = file_name[len(prefix_pattern):-len(".json")]
            result_dict[dict_key] = file_path
    return result_dict

def get_votacoes_dictionary():
    files = get_file_list_v2('v2', "votacoes")
    files_dict = create_dict(files, "votacoes_")
    return files_dict

def get_votacoes_id_dictionary():
    files = get_file_list_v2('v2', "votacoes_id")
    files_dict = create_dict(files, "votacoes_id_")
    return files_dict

def get_votacoes_votos_dictionary():
    files = get_file_list_v2('v2', "votacoes_votos")
    files_dict = create_dict(files, "votacoes_votos_")
    return files_dict

def get_proposicoes_dictionary():
    files = get_file_list_v2('v2', "proposicoes")
    files_dict = create_dict(files, "proposicoes_")
    return files_dict

def get_proposicoes_id_dictionary():
    files = get_file_list_v2('v2', "proposicoes_id")
    files_dict = create_dict(files, "proposicoes_id_")
    return files_dict

def get_proposicoes_autores_dictionary():
    files = get_file_list_v2('v2', "proposicoes_autores")
    files_dict = create_dict(files, "proposicoes_autores_")
    return files_dict

def get_proposicoes_temas_dictionary():
    files = get_file_list_v2('v2', "proposicoes_temas")
    files_dict = create_dict(files, "proposicoes_temas_")
    return files_dict

def get_votacoes_orientacoes_dictionary():
    files = get_file_list_v2('v2', "votacoes_orientacoes")
    files_dict = create_dict(files, "votacoes_orientacoes_")
    return files_dict

def get_deputados_dictionary():
    files = get_file_list_v2('v2', "deputados")
    files_dict = create_dict(files, "deputados_")
    return files_dict

def get_deputados_id_dictionary():
    files = get_file_list_v2('v2', "deputados_id")
    files_dict = create_dict(files, "deputados_id_")
    return files_dict

def get_deputados_legislaturas_dictionary():
    files = get_file_list_v2('v2', "deputados_legislaturas")
    files_dict = create_dict(files, "deputados_legislaturas_")
    return files_dict

def get_legislaturas_dictionary():
    files = get_file_list_v2('v2', "legislaturas")
    files_dict = create_dict(files, "legislaturas_")
    return files_dict