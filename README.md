# UFSCâmara

## Dependencias

pip3 install pandas
pip3 install pyarrow

## API Camâra

https://dadosabertos.camara.leg.br/swagger/api.html
http://www2.camara.leg.br/transparencia/dados-abertos/dados-abertos-legislativo

## Arquivos gerados

### logs

Guarda os logs da execução da aplicação, de forma a tornar mais fácil a validação, identificação e correção de problemas.

### raw_data_api_v2

Guarda os arquivos originais, em formato de json que são coletados da api da Câmara de Deputados.
Em uma primeira execução estes arquivos serão coletados e guardados, em execuções seguintes, os arquivos que já existem serão lidos deste diretório, tornando mais rápida a execução.

Além disto, é possível atualizar os dados rodando novamente a etapa de coleta, adicionando desta forma conteúdo que ainda não estava salvo.

### dataframes

Guarda os dataframes gerados, seja os iniciais, após o download e formatação básica, seja os finais após tratamento.