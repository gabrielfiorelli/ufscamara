# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 23:19:37 2024

@author: BlinkHome
"""
import pandas as pd

def proposicao_from_json_to_df(json_data):
    
    df = pd.DataFrame()
    
    for content in json_data:
        proposicoes = content['proposicoes']['proposicao']
        
        internal = pd.DataFrame(proposicoes)
        df = pd.concat([df, internal], ignore_index=True)
    
    df.rename(columns={'codProposicao': 'cod_proposicao', 'nomeProposicao': 'nome_proposicao', 'dataVotacao': 'data_votacao'}, inplace=True)
    
    return df

def proposicao_detail_from_json_to_df(json_data):
    
    df = pd.DataFrame()
    
    for content in json_data:
        internal =  pd.json_normalize(content)
        df = pd.concat([df, internal], ignore_index=True)
    
    return df