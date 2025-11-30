# UFSCâmara

## Dependencias

* pip3 install pandas
* pip3 install pyarrow

## API Camâra

https://dadosabertos.camara.leg.br/swagger/api.html
http://www2.camara.leg.br/transparencia/dados-abertos/dados-abertos-legislativo

## Arquivos gerados

### logs

Guarda os logs da execução da aplicação, de forma a tornar mais fácil a validação, identificação e correção de problemas.

### raw_data_api_v2

Guarda os arquivos originais, em formato de JSON que são coletados da API da Câmara dos Deputados.  
Em uma primeira execução esses arquivos serão coletados e guardados. Em execuções seguintes, os arquivos que já existem serão lidos deste diretório, tornando a execução mais rápida.

Além disso, é possível atualizar os dados rodando novamente a etapa de coleta, adicionando desta forma conteúdo que ainda não estava salvo.

### dataframes

Guarda os dataframes gerados, seja os iniciais, após o download e formatação básica, seja os finais apóss tratamento.

----

# UFSCAMARA – Guia Básico de Uso

Este documento apresenta o uso essencial da biblioteca **UFSCAMARA**, incluindo:
- como configurar o ambiente  
- como criar a instância principal  
- como baixar dados da API v2 da Câmara  
- como carregar e salvar DataFrames  
- e como fazer chamadas diretas à API  

Este é o **primeiro arquivo que alguém deve ler** ao acessar o repositório.

---

## 1. Instalação e Estrutura Básica

A biblioteca assume a seguinte estrutura:

```
ufscamara/
 ├── core/           ← lógica principal e orquestração
 ├── data/           ← leitura/escrita e montagem de DataFrames
 ├── util/           ← utilidades (logger, config, file utils)
 ├── raw_data_api_v2 ← dados brutos baixados da API
 ├── dataframes/     ← DataFrames salvos
 ├── logs/           ← logs automáticos
 └── ex_*.py         ← exemplos de uso
```

---

## 2. Configuração

O arquivo `config.json` na raiz do projeto tem a seguinte estrutura:


```json
{
    "api_version": "v2",
    "technical_config": {
        "RESULTS_PER_PAGE": 100,
        "IS_DEBUG": false,
        "MAX_RETRIES": 3,
        "SECONDS_TO_WAIT": 2,
        "RETRY_WAIT": 10
    }
}
```

Carregue essa configuração no seu script Python:

```python
from util import config_reader
config = config_reader.load_config()
```

---

## 3. Consultar Parâmetros Disponíveis em Endpoints

Seguindo este exemplo é possível verificar a documentação doc string das chamadas diretas da API.

```
?ufscamara.v2.votacoes
```

```
Signature:
ufscamara.v2.votacoes(
    id=None,
    idProposicao=None,
    idEvento=None,
    idOrgao=None,
    dataInicio=None,
    dataFim=None,
    pagina=1,
    itens=100,
    ordem='DESC',
    ordenarPor='dataHoraRegistro',
    paginate=False,
    params=None,
    **extra,
)
Docstring:
Lista votações realizadas no Plenário ou em Comissões.

Args:
    id (str | int, opcional): ID específico de votação.
    idProposicao (str | int, opcional): ID da proposição associada.
    idEvento (str | int, opcional): ID do evento relacionado.
    idOrgao (str | int, opcional): ID do órgão responsável.
    dataInicio (str, opcional): Data inicial no formato 'YYYY-MM-DD'.
    dataFim (str, opcional): Data final no formato 'YYYY-MM-DD'.
    pagina (int): Página de resultados (default=1).
    itens (int): Quantidade de registros por página (default=100).
    ordem (str): 'ASC' ou 'DESC' (default='DESC').
    ordenarPor (str): Campo de ordenação (default='dataHoraRegistro').
    paginate (bool, opcional): 
        Se True, ativa a paginação automática e busca todas as páginas disponíveis 
        (padrão: False).
    params (dict, opcional): Parâmetros adicionais.
    **extra: Parâmetros adicionais opcionais.

Returns:
    dict: Resposta JSON com a lista de votações.

Example:
    >>> votacoes(dataInicio="2025-02-04", dataFim="2025-02-04", idOrgao=180)
```

## 4. Criando a Instância Principal

```python
from core.ufscamara import Ufscamara
ufscamara = Ufscamara(config)
```

Essa instância:
- prepara as pastas internas
- inicializa o logger
- configura a camada de download
- inicializa o `data_manager` (para transformar JSON → DataFrames)

---

## 5. Baixando Dados da API

Ao utilizar os métodos de download, oodos os dados brutos são salvos em:

```
raw_data_api_v2/<endpoint>/
```

### 5.1. Operações de Download de Dados

A biblioteca oferece métodos para realizar o download de dados diretamente da API da Câmara dos Deputados, organizados por tipo de recurso (votações, votos, proposições, deputados etc.).

Esses métodos estão disponíveis na instância da classe `Ufscamara` e seguem um padrão simples: você pode definir parâmetros como data de início/fim, IDs específicos, ou deixar em branco para buscar todos os registros disponíveis.

A seguir, dois exemplos básicos de uso:

#### Exemplo 1: Download de votações realizadas no plenário
```python
from datetime import date

# Busca todas as votações realizadas no Plenário desde 1989 até hoje
ufscamara.download_arquivos_votacao_v2(
    dataInicio=date(1989, 1, 1),
    dataFim=date.today(),
    idOrgao=180  # Plenário
)

```

#### Exemplo 2: Download dos votos das votações realizadas no plenário

Primeiro, carregamos o DataFrame de votações previamente baixado

```
votacoes_df = ufscamara.data_manager.carregar_votacoes()
ids = votacoes_df["id"].tolist()
```

Em seguida, baixamos os votos correspondentes a cada votação

```
ufscamara.download_arquivos_votacoes_votos_v2(ids)
```

---

## 5. Carregar DataFrames


O data_manager possui vários métodos para o carregamento padrão dos dados baixados.
Cada endpoint da API é mapeado para um método diferente aqui:


### 5.1 Exemplos

```python
df = ufscamara.data_manager.carregar_votacoes()
```


```python
df = ufscamara.data_manager.carregar_votacoes_id()
```

---

## 6. Salvando DataFrames

Após fazer alterações, limpezas, junções com outras partes dos dados disponibilizados, o recomendado é salvar o dataframe final, de forma que possa ser carregado depois quando necessário.

```python
ufscamara.data_manager.salvar_dataframe(df, "nome_do_arquivo")
```

Carregar depois:

```python
df = ufscamara.data_manager.carregar_dataframe("nome_do_arquivo")
```

---

## 7. Chamadas Diretas à API (avançado)

Além dos métodos de download, também é possível acessar diretamente os endpoints da api e verificar a documentação de cada um deles

Você pode usar diretamente a API v2:

```python
from core import api_camara_v2
resultado = api_camara_v2.votacoes(
    dataInicio="2024-01-01",
    dataFim="2024-01-31"
)
```

Outras chamadas:

```python
api_camara_v2.votacoes_id()
api_camara_v2.votacoes_id_votos()
api_camara_v2.votacoes_id_orientacoes()
api_camara_v2.proposicoes_id()
api_camara_v2.proposicoes_id_temas()
api_camara_v2.deputados()
api_camara_v2.legislaturas_id()
```

Para verificar a documentação:

?api_camara_v2.votacoes_id

---

## 8. Exemplos Rápidos de Análises

Contar votações por ano:

```python
v = ufscamara.data_manager.carregar_votacoes()
v["ano"] = pd.to_datetime(v["data"]).dt.year
v.groupby("ano")["id"].nunique()
```

Contar votos por votação:

```python
votos = ufscamara.data_manager.carregar_votacoes_votos()
votos.groupby("idVotacao")["tipoVoto"].count()
```

---

## 9. Fluxo Completo Recomendado

1. Criar instância `Ufscamara`  
2. Baixar primeiro os dados que são de endpoints de listagens (filtros de busca)
3. Baixar os dados dos endpoints que precisam de iteração (buscas para cada id)  
5. Carregar DataFrames básico 
6. Unificar os dados e fazer tratamentos desejados
7. Salvar DataFrames tratados  
8. Fazer análises e gráficos  

---

## 10. Exemplos completos

Veja os exemplos em:

- `ex_01_chamadas_isoladas.py`  
- `ex_02_download_dataset.py`  
- `ex_02_montagem_dataset.py`  
- `ex_03_download_tudo.py`  

Esses arquivos mostram o uso real das chamadas e organização de dados.
