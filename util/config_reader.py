import json
import os

# Caminho relativo para o config.json, considerando que o script principal está na raiz do projeto
CONFIG_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config_v2.json")

def load_config():
    """
    Lê o arquivo config.json e retorna o conteúdo como um dicionário.
    """
    if not os.path.exists(CONFIG_FILE):
        raise FileNotFoundError(f"Arquivo de configuração não encontrado: {CONFIG_FILE}")
    
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        config = json.load(f)
    
    return config