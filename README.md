# basometro_v2_ufsc

## Dependencias

### camaraPy
https://github.com/RodrigoMenegat/camaraPy/tree/master

pip3 install camarapy
pip3 install pandas
pip3 install pyarrow

O pacote camaraPy é um wrapper para as APIs da Câmara dos Deputados.

## API Camâra

https://dadosabertos.camara.leg.br/swagger/api.html
http://www2.camara.leg.br/transparencia/dados-abertos/dados-abertos-legislativo


## Arquivos gerados

### logs

Guarda os logs da execução da aplicação, de forma a tornar mais fácil a validação, identificação e correção de problemas.

### raw_data

Guarda os arquivos originais, em formato de json que são coletados da api da Câmara de Deputados.
Em uma primeira execução estes arquivos serão coletados e guardados, em execuções seguintes, os arquivos que já existem serão lidos deste diretório, tornando mais rápida a execução.

Além disto, é possível atualizar os dados rodando novamente a etapa de coleta, adicionando desta forma conteúdo que ainda não estava salvo.

### data

Guarda os dados em formato intermediário, como dataframes já com alguns tratamentos de dados.
Dentre eles:
* Listar

### trajectory_data
Guarda os dados no formato final, em formato de trajetórias, seguindo o padrão de TID para cada trajetória identificada.

Em caso de necessidade de alterar apenas o período das trajetórias por exemplo, basta atualizar apenas esta pasta.