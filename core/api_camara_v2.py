
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 24 22:44:56 2025

@author: BlinkPC
"""

from core.v2_api_helpers import build_api_call

################################################################
## VOTACOES
################################################################


def votacoes_params(params: dict, paginate = False):
    """
    Busca votações na API v2 utilizando um dicionário de parâmetros completo.

    Args:
        params (dict): Dicionário contendo os filtros aceitos pela API, como:
            - id (str | int, opcional): ID específico de votação.
            - idProposicao (str | int, opcional): ID da proposição associada.
            - idEvento (str | int, opcional): ID do evento relacionado.
            - idOrgao (str | int, opcional): ID do órgão responsável.
            - dataInicio (str, opcional): Data inicial no formato 'YYYY-MM-DD'.
            - dataFim (str, opcional): Data final no formato 'YYYY-MM-DD'.
            - pagina (int): Página de resultados (default=1).
            - itens (int): Quantidade de registros por página (default=100).
            - ordem (str): 'ASC' ou 'DESC' (default='DESC').
            - ordenarPor (str): Campo de ordenação (default='dataHoraRegistro').
            - paginate (bool, opcional): 
                Se True, ativa a paginação automática e busca todas as páginas disponíveis 
                (padrão: False).

    Returns:
        dict: Resposta JSON da API.

    Example:
        >>> votacoes_params({"dataInicio": "2025-03-01", "dataFim": "2025-03-02"})
    """
    return build_api_call("votacoes", named_params=params, paginate = paginate)

def votacoes(
            id=None,
            idProposicao=None,
            idEvento=None,
            idOrgao=None,
            dataInicio=None,
            dataFim=None,
            pagina=1,
            itens=100,
            ordem="DESC",
            ordenarPor="dataHoraRegistro",
            paginate=False,
            params=None,
            **extra
            ):
    """
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
    """
    
    return build_api_call("votacoes", locals(), exclude=["paginate"], paginate = paginate)

def votacoes_id(id):
    """
    Retorna os detalhes de uma votação específica.

    Args:
        id (str): Identificador único da votação.

    Returns:
        dict: Resposta JSON contendo metadados e resultados da votação.
    """
    return build_api_call("votacoes", subpath=str(id))

def votacoes_id_votos(id):
    """
    Retorna os votos individuais de uma votação específica.

    Args:
        id (str): Identificador único da votação.

    Returns:
        dict: Resposta JSON com a lista de votos por deputado.
    """
    return build_api_call("votacoes", subpath=f"{id}/votos")

def votacoes_id_orientacoes(id):
    """
    Retorna as orientações de bancada para uma votação específica.

    Args:
        id (str): Identificador único da votação.

    Returns:
        dict: Resposta JSON com orientações de governo, maioria, minoria, etc.
    """
    return build_api_call("votacoes", subpath=f"{id}/orientacoes")


################################################################
## PROPOSICOES
################################################################

def proposicoes_params(params: dict, paginate = False):
    """
    Busca proposições na API v2 a partir de um dicionário de parâmetros.

    Essa função é uma interface direta para chamadas personalizadas quando
    já se possui um dicionário de parâmetros pronto, sem precisar declarar
    cada campo individualmente.

    Args:
        params (dict): Dicionário de parâmetros aceitos pela API.
            Exemplos de chaves aceitas:
                - siglaTipo (str, opcional): Sigla do tipo de proposição, ex.: "PL", "PEC", "MPV".
                - numero (int, opcional): Número da proposição.
                - ano (int, opcional): Ano de apresentação.
                - autor (str, opcional): Nome completo ou parcial do autor (entre aspas na API original).
                - idDeputadoAutor (int, opcional): Identificador do deputado autor.
                - siglaPartidoAutor (str, opcional): Sigla do partido do autor, ex.: "PT", "PL".
                - siglaUfAutor (str, opcional): Unidade da Federação do autor, ex.: "SP", "RJ".
                - codTema (int, opcional): Código numérico do tema da proposição.
                - tramitacaoSenado (bool, opcional): Define se a proposição já tramitou no Senado.
                - dataInicio (str, opcional): Data inicial do intervalo de tramitação.
                - dataFim (str, opcional): Data final do intervalo de tramitação.
                - dataApresentacaoInicio (str, opcional): Data de início do intervalo de apresentação.
                - dataApresentacaoFim (str, opcional): Data de fim do intervalo de apresentação.
                - codSituacao (int, opcional): Código da situação atual.
                - pagina (int): Página de resultados (padrão: 1).
                - itens (int): Quantidade de registros por página (padrão: 100).
                - ordem (str): "ASC" ou "DESC" (padrão: "ASC").
                - ordenarPor (str): Campo usado na ordenação (ex.: "id", "ano", "numero").
                - paginate (bool, opcional): 
                    Se True, ativa a paginação automática e busca todas as páginas disponíveis 
                    (padrão: False).

    Returns:
        dict: Objeto JSON retornado pela API, contendo metadados e lista de proposições.

    Example:
        >>> proposicoes_params({
        ...     "siglaTipo": "PL",
        ...     "ano": 2023,
        ...     "ordem": "ASC",
        ...     "ordenarPor": "ano",
        ...     "itens": 10
        ... })
    """
    return build_api_call("proposicoes", named_params=params, paginate = paginate)

def proposicoes(
        id=None,
        siglaTipo=None,
        numero=None,
        ano=None,
        codTipo=None,
        idDeputadoAutor=None,
        autor=None,
        siglaPartidoAutor=None,
        idPartidoAutor=None,
        siglaUfAutor=None,
        keywords=None,
        tramitacaoSenado=None,
        dataInicio=None,
        dataFim=None,
        dataApresentacaoInicio=None,
        dataApresentacaoFim=None,
        codSituacao=None,
        codTema=None,
        pagina=1,
        itens=100,
        ordem="ASC",
        ordenarPor="id",
        paginate=False,
        params=None,
        **extra
    ):
    """
    Lista proposições legislativas (PLs, PECs, MPs, REQs, etc.) com filtros diversos.

    Essa função é o principal ponto de acesso ao endpoint `/proposicoes`.
    Permite buscar proposições com base em tipo, ano, autor, partido, UF,
    tema, situação ou intervalo de datas.

    Args:
        siglaTipo (str, opcional): Sigla do tipo de proposição, ex.: "PL", "PEC", "MPV".
        numero (int, opcional): Número da proposição.
        ano (int, opcional): Ano de apresentação.
        autor (str, opcional): Nome completo ou parcial do autor (entre aspas na API original).
        idDeputadoAutor (int, opcional): Identificador do deputado autor.
        siglaPartidoAutor (str, opcional): Sigla do partido do autor, ex.: "PT", "PL".
        siglaUfAutor (str, opcional): Unidade da Federação do autor, ex.: "SP", "RJ".
        codTema (int, opcional): Código numérico do tema da proposição.
        tramitacaoSenado (bool, opcional): Define se a proposição já tramitou no Senado.
        dataInicio (str, opcional): Data inicial do intervalo de tramitação.
        dataFim (str, opcional): Data final do intervalo de tramitação.
        dataApresentacaoInicio (str, opcional): Data de início do intervalo de apresentação.
        dataApresentacaoFim (str, opcional): Data de fim do intervalo de apresentação.
        codSituacao (int, opcional): Código da situação atual.
        pagina (int): Página de resultados (padrão: 1).
        itens (int): Quantidade de registros por página (padrão: 100).
        ordem (str): "ASC" ou "DESC" (padrão: "ASC").
        ordenarPor (str): Campo usado na ordenação (ex.: "id", "ano", "numero").
        paginate (bool, opcional): 
            Se True, ativa a paginação automática e busca todas as páginas disponíveis 
            (padrão: False).
        params (dict, opcional): Parâmetros adicionais.
        **extra: Campos extras compatíveis com futuras versões da API.

    Returns:
        dict: Resposta JSON com metadados e lista de proposições.

    Example:
        >>> proposicoes(siglaTipo="PL", ano=2023, ordenarPor="ano")
    """
    return build_api_call("proposicoes", locals(), exclude=["paginate"], paginate = paginate)

def proposicoes_id(id):
    """
    Retorna os detalhes completos de uma proposição específica.

    Endpoint: `/proposicoes/{id}`

    Args:
        id (int | str): Identificador único da proposição.

    Returns:
        dict: Dados estruturados da proposição, incluindo tipo, ementa,
        autores, situação atual e data de apresentação.

    Example:
        >>> proposicoes_id(2450476)
    """
    return build_api_call("proposicoes", subpath=f"{id}")

def proposicoes_id_autores(id):
    """
    Retorna a lista de autores de uma proposição específica.

    Endpoint: `/proposicoes/{id}/autores`

    Args:
        id (int | str): Identificador único da proposição.

    Returns:
        dict: JSON contendo nome, partido e UF de cada autor.

    Example:
        >>> proposicoes_id_autores(2450476)
    """
    return build_api_call("proposicoes", subpath=f"{id}/autores")

def proposicoes_id_relacionadas(id):
    """
    Retorna proposições relacionadas à proposição especificada.

    Endpoint: `/proposicoes/{id}/relacionadas`

    Args:
        id (int | str): Identificador único da proposição.

    Returns:
        dict: Lista de proposições relacionadas (por tema, apensamento, etc.).
    """
    return build_api_call("proposicoes", subpath=f"{id}/relacionadas")

def proposicoes_id_temas(id):
    """
    Retorna os temas associados a uma proposição.

    Endpoint: `/proposicoes/{id}/temas`

    Args:
        id (int | str): Identificador único da proposição.

    Returns:
        dict: Lista de objetos com código e nome dos temas.
    """
    return build_api_call("proposicoes", subpath=f"{id}/temas")

def proposicoes_id_tramitacoes(id):
    """
    Retorna o histórico de tramitações de uma proposição.

    Endpoint: `/proposicoes/{id}/tramitacoes`

    Args:
        id (int | str): Identificador único da proposição.

    Returns:
        dict: Lista cronológica de tramitações, incluindo órgão, despacho e situação.
    """
    return build_api_call("proposicoes", subpath=f"{id}/tramitacoes")

def proposicoes_id_votacoes(id):
    """
    Retorna as votações relacionadas a uma proposição.

    Endpoint: `/proposicoes/{id}/votacoes`

    Args:
        id (int | str): Identificador único da proposição.

    Returns:
        dict: Lista de votações que ocorreram sobre a proposição.
    """
    return build_api_call("proposicoes", subpath=f"{id}/votacoes")

################################################################
## DEPUTADOS
################################################################

def deputados_params(params: dict, paginate = False):
    """
    Busca deputados na API v2 utilizando um dicionário de parâmetros.

    Args:
        params (dict): Dicionário com filtros aceitos, como:
            - nome (str, opcional): Nome parcial ou completo do deputado.
            - siglaUf (str, opcional): Estado de origem, ex.: "SP", "RJ".
            - siglaPartido (str, opcional): Partido, ex.: "PT", "PL".
            - idLegislatura (int, opcional): Identificador numérico da legislatura.
            - ordenarPor (str): Campo de ordenação (default="nome").
            - ordem (str): Direção da ordenação ("ASC" ou "DESC").
            - pagina (int): Número da página.
            - itens (int): Quantidade de resultados por página.
            - dataInicio / dataFim (str, opcional): Intervalo de atividade.
            - paginate (bool, opcional): 
                Se True, ativa a paginação automática e busca todas as páginas disponíveis 
                (padrão: False).

    Returns:
        dict: Lista de deputados com informações resumidas (id, nome, partido, UF).
    """
    return build_api_call("deputados", named_params=params, paginate = paginate)

def deputados(
                id=None,
                nome=None,
                idLegislatura=None,
                siglaUf=None,
                siglaPartido=None,
                siglaSexo=None,
                pagina=1,
                itens=100,
                dataInicio=None,
                dataFim=None,
                ordem="DESC",
                ordenarPor="nome",
                paginate=False,
                params=None,
                **extra
            ):
    """
    Lista deputados ativos ou históricos, com filtros por nome, partido, UF e legislatura.

    Endpoint: `/deputados`

    Args:
        nome (str, opcional): Nome parcial ou completo do deputado.
        siglaUf (str, opcional): Estado de origem, ex.: "SP", "RJ".
        siglaPartido (str, opcional): Partido, ex.: "PT", "PL".
        idLegislatura (int, opcional): Identificador numérico da legislatura.
        ordenarPor (str): Campo de ordenação (default="nome").
        ordem (str): Direção da ordenação ("ASC" ou "DESC").
        pagina (int): Número da página.
        itens (int): Quantidade de resultados por página.
        dataInicio / dataFim (str, opcional): Intervalo de atividade.
        paginate (bool, opcional): 
            Se True, ativa a paginação automática e busca todas as páginas disponíveis 
            (padrão: False).

    Returns:
        dict: Lista de deputados com seus metadados (nome, id, partido, UF, etc.).

    Example:
        >>> deputados(siglaUf="SC", siglaPartido="PL", ordenarPor="nome")
    """
    return build_api_call("deputados", locals(), exclude=["paginate"], paginate = paginate)

def deputados_id(id):
    """
    Retorna os dados detalhados de um deputado específico.

    Endpoint: `/deputados/{id}`

    Args:
        id (int | str): Identificador único do deputado.

    Returns:
        dict: Dados pessoais, mandato, partido e links do deputado.
    """
    return build_api_call("deputados", subpath=f"{id}")

def deputados_id_despesas(
                id=None,
                idLegislatura=None,
                ano=None,
                mes=None,
                cnpjCpfFornecedor=None,
                pagina=1,
                itens=100,
                ordem="DESC",
                ordenarPor="ano",
                paginate=False,
                params=None,
                **extra
            ):
    
    """
    Retorna as despesas de um deputado (cota parlamentar).

    Endpoint: `/deputados/{id}/despesas`

    Args:
        id (int | str): Identificador único do deputado.
        idLegislatura (int, opcional): Legislatura de referência.
        ano (int, opcional): Ano das despesas.
        mes (int, opcional): Mês das despesas.
        cnpjCpfFornecedor (str, opcional): CNPJ/CPF do fornecedor.
        ordenarPor (str): Campo de ordenação (padrão="ano").
        paginate (bool, opcional): 
            Se True, ativa a paginação automática e busca todas as páginas disponíveis 
            (padrão: False).

    Returns:
        dict: Lista de despesas detalhadas (valor, tipo, fornecedor, data).
    """
    
    if id is None:
        raise ValueError("Necessário passar um id de deputado.")

    return build_api_call(
        "deputados",
        locals(),
        exclude=["id", "paginate"],
        subpath=f"{id}/despesas",
        paginate = paginate
    )

def deputados_id_discursos(
                id=None,
                idLegislatura=None,
                dataInicio=None,
                dataFim=None,
                pagina=1,
                itens=100,
                ordem="DESC",
                ordenarPor="dataHoraInicio",
                paginate=False,
                params=None,
                **extra
            ):
    """
    Retorna os discursos feitos por um deputado em plenário ou comissões.

    Endpoint: `/deputados/{id}/discursos`

    Args:
        id (int | str): Identificador do deputado.
        dataInicio / dataFim (str, opcional): Intervalo de datas.
        idLegislatura (int, opcional): Legislatura de referência.
        paginate (bool, opcional): 
            Se True, ativa a paginação automática e busca todas as páginas disponíveis 
            (padrão: False).

    Note:
        Caso os parâmetros de data e legislatura não sejam informados,
        a API retorna apenas os discursos feitos nos últimos sete dias.

    Returns:
        dict: Lista de discursos, com texto, data, local e evento associado.
    """
    
    if id is None:
        raise ValueError("Necessário passar um id de deputado.")

    return build_api_call(
        "deputados",
        locals(),
        exclude=["id", "paginate"],
        subpath=f"{id}/discursos",
        paginate = paginate
    )

def deputados_id_eventos(
                id=None,
                dataInicio=None,
                dataFim=None,
                pagina=1,
                itens=10,
                ordem="DESC",
                ordenarPor="dataHoraInicio",
                paginate=False,
                params=None,
                **extra
            ):
    """
    Retorna os eventos dos quais o deputado participou (sessões, comissões, etc).

    Endpoint: `/deputados/{id}/eventos`

    Args:
        id (int | str): Identificador único do deputado.
        dataInicio / dataFim (str, opcional): Intervalo de tempo.
        paginate (bool, opcional): 
            Se True, ativa a paginação automática e busca todas as páginas disponíveis 
            (padrão: False).

    Returns:
        dict: Lista de eventos com data, tipo e local.
    """
    
    if(id is None):
        return "Necessário passar um id de deputado"
    
    return build_api_call(
        "deputados",
        locals(),
        exclude=["id", "paginate"],
        subpath=f"{id}/eventos",
        paginate = paginate
    )

def deputados_id_frentes(id):
    """
    Retorna as frentes parlamentares das quais o deputado faz parte.

    Endpoint: `/deputados/{id}/frentes`

    Args:
        id (int | str): Identificador único do deputado.

    Returns:
        dict: Lista de frentes parlamentares com nome, tema e id correspondente.
    """
    if(id is None):
        return "Necessário passar um id de deputado"
    
    return build_api_call("deputados", subpath=f"{id}/frentes")

def deputados_id_historico(id):
    """
    Um deputado pode, no meio de uma legislatura, mudar de partido ou de nome parlamentar, entrar em licença,
    ser afastado ou substituir outro deputado. Como essas mudanças se refletem em votações, ou na autoria e
    relatoria de proposições, pode se tornar difícil identificar um mesmo parlamentar em diferentes momentos
    de sua atuação na Câmara.

    Retorna uma listagem com as diferentes situações de exercício parlamentar do deputado
    identificado por {id}, mesmo que a alteração registrada não tenha afetado o andamento do mandato.
    """
    
    if(id is None):
        return "Necessário passar um id de deputado"
    
    return build_api_call("deputados", subpath=f"{id}/historico")

def deputados_id_mandatosExternos(id):
    """
    Retorna uma lista em que cada item traz informações básicas sobre um cargo para o qual o parlamentar
    identificado por {id} tenha sido eleito, em sua carreira política fora da Câmara dos Deputados.
    Estes dados são fornecidos pelo Tribunal Superior Eleitoral. A lista vem ordenada cronologicamente, por padrão.
    """
    
    if(id is None):
        return "Necessário passar um id de deputado"
    
    return build_api_call("deputados", subpath=f"{id}/mandatosExternos")

def deputados_id_ocupacoes(id):
    """
    Enumera as atividades profissionais ou ocupacionais que o deputado identificado por {id} já teve em
    sua carreira e declarou à Câmara dos Deputados.
    """
    
    if(id is None):
        return "Necessário passar um id de deputado"
    
    return build_api_call("deputados", subpath=f"{id}/ocupacoes")

def deputados_id_orgaos(
                id=None,
                dataInicio=None,
                dataFim=None,
                pagina=1,
                itens=10,
                ordem="DESC",
                ordenarPor="dataInicio",
                paginate=False,
                params=None,
                **extra
            ):
    """
    Retorna os orgaos dos quais o deputado participou (sessões, comissões, etc).

    Endpoint: `/deputados/{id}/orgaos`

    Args:
        id (int | str): Identificador único do deputado.
        dataInicio / dataFim (str, opcional): Intervalo de tempo.
        paginate (bool, opcional): 
            Se True, ativa a paginação automática e busca todas as páginas disponíveis 
            (padrão: False).

    Returns:
        dict: Lista de eventos com data, tipo e local.
    """
    
    if(id is None):
        return "Necessário passar um id de deputado"
    
    return build_api_call(
        "deputados",
        locals(),
        exclude=["id", "paginate"],
        subpath=f"{id}/orgaos",
        paginate = paginate
    )

def deputados_id_profissoes(id):
    """
    Retorna uma lista de dados sobre profissões que o parlamentar identificado por {id} declarou
    à Câmara que já exerceu ou que pode exercer pela sua formação e/ou experiência.
    """
    
    if(id is None):
        return "Necessário passar um id de deputado"
    
    return build_api_call("deputados", subpath=f"{id}/profissoes")

################################################################
## REFERENCIAS
################################################################

def referencias_deputados():
    """
    Returns
    Retorna, como valor do elemento "dados", um objeto em que cada elemento tem o nome de um parâmetro aplicável ao
    endpoint /deputados. Cada elemento desses tem como valor uma lista de itens (nós em XML) em que cada item
    representa um valor válido que pode ser atribuído ao parâmetro. Em outras palavras: uma requisição a esta URL
    tem como resposta uma versão agregada das respostas de todas as URLs abaixo dela. Assim, em uma só chamada é
    possível obter uma lista de todos os parâmetros que exigem valores predeterminados, e quais são os valores
    válidos para tais parâmetros. Este recurso não é disponível em formato CSV.
    """
    return build_api_call("referencias", subpath="deputados")

def referencias_deputados_codSituacao():
    """
    Retorna uma lista de siglas e descrições dos possíveis estados em que um deputado pode estar em relação ao
    seu exercício parlamentar: Exercício, Fim de Mandato, Afastado, etc.
    """
    return build_api_call("referencias", subpath="deputados/codSituacao")

def referencias_deputados_codTipoProfissao():
    """
    Retorna uma lista dos títulos de profissões registradas na Câmara dos Deputados (em masculino) e seus códigos.
    """
    return build_api_call("referencias", subpath="deputados/codTipoProfissao")

def referencias_deputados_siglaUF():
    """
    Retorna uma lista de siglas e nomes das unidades de federação brasileiras, usados principalmente para
    indicar onde um parlamentar foi eleito.
    """
    return build_api_call("referencias", subpath="deputados/siglaUF")

def referencias_deputados_tipoDespesa():
    """
    Retorna uma lista de códigos e nomes das possíveis despesas de Cota Parlamentar: COMBUSTÍVEIS E LUBRIFICANTES.,
    TELEFONIA, SERVIÇOS POSTAIS, etc.
    """
    return build_api_call("referencias", subpath="deputados/tipoDespesa")

def referencias_proposicoes():
    """
    Retorna, como valor do elemento "dados", um objeto em que cada elemento tem o nome de um parâmetro aplicável
    ao endpoint /proposicoes. Cada elemento desses tem como valor uma lista de itens (nós em XML) em que cada
    item representa um valor válido que pode ser atribuído ao parâmetro.
    Em outras palavras: uma requisição a esta URL tem como resposta uma versão agregada das respostas de todas
    as URLs abaixo dela. Assim, em uma só chamada é possível obter uma lista de todos os parâmetros que
    exigem valores predeterminados, e quais são os tais valores para cada um desses parâmetros.
    Este recurso não é disponível em formato CSV.
    """
    return build_api_call("referencias", subpath="proposicoes")

def referencias_proposicoes_codSituacao():
    """
    Uma lista de identificadores das diversas situações de tramitação em que uma proposição pode se encontrar,
    como Encaminhada à Publicação, Aguardando Análise, Devolvida ao Autor, etc."""
    return build_api_call("referencias", subpath="proposicoes/codSituacao")

def referencias_proposicoes_codTema():
    """
    Uma lista de identificadores numéricos e nome dos temas que uma proposição pode apresentar.
    """
    return build_api_call("referencias", subpath="proposicoes/codTema")

def referencias_proposicoes_codTipoAutor():
    """
    Uma lista de códigos numéricos e descritores dos tipos de parlamentares, órgãos da Câmara e instituições
    que podem ser autores de proposições.
    """
    return build_api_call("referencias", subpath="proposicoes/codTipoAutor")

def referencias_proposicoes_codTipoTramitacao():
    """
    Uma lista de identificadores numéricos, siglas e descrições dos tipos de tramitações em que uma proposição
    pode se encontrar, como Apensação, Despacho, Devolução ao autor, etc.
    """
    return build_api_call("referencias", subpath="proposicoes/codTipoTramitacao")

def referencias_proposicoes_siglaTipo():
    """
    Uma lista de identificadores numéricos, siglas e descrições dos tipos de proposições que existem ou já
    existiram no Congresso, tais como PEC, Requerimento, Emenda de Plenário e outros.
    """
    return build_api_call("referencias", subpath="proposicoes/siglaTipo")

def referencias_situacoesDeputado():
    """
    Retorna uma lista de siglas e descrições dos possíveis estados em que um deputado pode estar em
    relação ao seu exercício parlamentar: Exercício, Fim de Mandato, Afastado, etc.
    """
    return build_api_call("referencias", subpath="situacoesDeputado")

def referencias_situacoesEvento():
    """
    Retorna uma lista de identificadores numéricos, siglas e descrições dos estados em que eventos
    como uma reunião podem se encontrar, como Em Andamento, Cancelada e Encerrada.
    """
    return build_api_call("referencias", subpath="situacoesEvento")

def referencias_situacoesOrgao():
    """
    Retorna uma lista de identificadores numéricos, títulos e descrições das situações possíveis
    para órgãos em operação na Câmara, como Em funcionamento, Extinta, Pronta para criação, etc.
    """
    return build_api_call("referencias", subpath="situacoesOrgao")

def referencias_situacoesProposicao():
    """
    Uma lista de identificadores das diversas situações de tramitação em que uma proposição pode se
    encontrar, como Encaminhada à Publicação, Aguardando Análise, Devolvida ao Autor, etc.
    """
    return build_api_call("referencias", subpath="situacoesProposicao")

def referencias_tiposAutor():
    """
    Uma lista de códigos numéricos e descritores dos tipos de parlamentares, órgãos da Câmara e
    instituições que podem ser autores de proposições.
    """
    return build_api_call("referencias", subpath="tiposAutor")

def referencias_tiposEvento():
    """
    Retorna uma lista de identificadores numéricos, siglas e descrições dos tipos de eventos ocorridos
    na Câmara, tais como Audiência Pública, Comissão Geral e Palestra, entre outros.
    """
    return build_api_call("referencias", subpath="tiposEvento")

def referencias_tiposOrgao():
    """
    Retorna uma lista de identificadores numéricos, siglas e descrições dos tipos de órgãos legislativos
    ou representados na Câmara, tais como as comissões permanentes, CPIs, procuradorias, etc.
    """
    return build_api_call("referencias", subpath="tiposOrgao")

def referencias_tiposProposicao():
    """
    Uma lista de identificadores numéricos, siglas e descrições dos tipos de proposições que existem
    ou já existiram no Congresso, tais como PEC, Requerimento, Emenda de Plenário e outros.
    """
    return build_api_call("referencias", subpath="tiposProposicao")

def referencias_tiposTramitacao():
    """
    Uma lista de identificadores numéricos, siglas e descrições dos tipos de tramitações em que uma
    proposição pode se encontrar, como Apensação, Despacho, Devolução ao autor, etc.
    """
    return build_api_call("referencias", subpath="tiposTramitacao")

def referencias_orgaos():
    """
    Retorna, como valor do elemento "dados", um objeto em que cada elemento tem o nome de um parâmetro
    aplicável ao endpoint /orgaos. Cada elemento desses tem como valor uma lista de itens (nós em XML)
    em que cada item representa um valor válido que pode ser atribuído ao parâmetro.
    Em outras palavras: uma requisição a esta URL tem como resposta uma versão agregada das respostas de
    todas as URLs abaixo dela. Assim, em uma só chamada é possível obter uma lista de todos os
    parâmetros que exigem valores predeterminados, e quais são os tais valores para cada um desses parâmetros.
    Este recurso não é disponível em formato CSV.
    """
    return build_api_call("referencias", subpath="orgaos")

def referencias_orgaos_codSituacao():
    """
    Retorna uma lista de identificadores numéricos, títulos e descrições das situações possíveis para
    órgãos em operação na Câmara, como Em funcionamento, Extinta, Pronta para criação, etc.
    """
    return build_api_call("referencias", subpath="orgaos/codSituacao")

def referencias_orgaos_codTipoOrgao():
    """
    Retorna uma lista de identificadores numéricos, siglas e descrições dos tipos de órgãos legislativos
    ou representados na Câmara, tais como as comissões permanentes, CPIs, procuradorias, etc.
    """
    return build_api_call("referencias", subpath="orgaos/codTipoOrgao")

def referencias_eventos():
    """
    Retorna, como valor do elemento "dados", um objeto em que cada elemento tem o nome de um parâmetro
    aplicável ao endpoint /eventos. Cada elemento desses tem como valor uma lista de itens (nós em XML)
    em que cada item representa um valor válido que pode ser atribuído ao parâmetro.
    Em outras palavras: uma requisição a esta URL tem como resposta uma versão agregada das respostas de
    todas as URLs abaixo dela. Assim, em uma só chamada é possível obter uma lista de todos os parâmetros
    que exigem valores predeterminados, e quais são os tais valores para cada um desses parâmetros.
    Este recurso não é disponível em formato CSV.
    """
    return build_api_call("referencias", subpath="eventos")

def referencias_eventos_codSituacaoEvento():
    """
    Retorna uma lista de identificadores numéricos, siglas e descrições dos estados em que eventos
    como uma reunião podem se encontrar, como Em Andamento, Cancelada e Encerrada.
    """
    return build_api_call("referencias", subpath="eventos/codSituacaoEvento")

def referencias_eventos_codTipoEvento():
    """
    Retorna uma lista de identificadores numéricos, siglas e descrições dos tipos de eventos ocorridos na Câmara,
    tais como Audiência Pública, Comissão Geral e Palestra, entre outros.
    """
    return build_api_call("referencias", subpath="eventos/codTipoEvento")


################################################################
## ORGAOS
################################################################

def orgaos( id=None,
            sigla=None,
            codTipoOrgao=None,
            dataInicio=None,
            dataFim=None,
            pagina=1,
            itens=100,
            ordem="DESC",
            ordenarPor="id",
            paginate=False,
            params=None,
            **extra
        ):
    """
    Lista órgãos legislativos da Câmara dos Deputados.

    Endpoint: `/orgaos`

    Retorna uma lista de informações básicas sobre os órgãos legislativos,
    incluindo identificador, tipo, sigla, situação e período de atividade.

    É possível filtrar a busca por identificadores, tipos, sigla, situação
    ou intervalo de tempo em que os órgãos estiveram ativos.

    Args:
        id (int | str, opcional): Identificador único do órgão.
        sigla (str, opcional): Sigla do órgão (ex.: "PLEN", "CCJ", "CMO").
        codTipoOrgao (int, opcional): Código numérico do tipo de órgão.
        dataInicio (str, opcional): Data inicial do filtro (YYYY-MM-DD).
        dataFim (str, opcional): Data final do filtro (YYYY-MM-DD).
        pagina (int, opcional): Página de resultados (padrão: 1).
        itens (int, opcional): Quantidade de registros por página (padrão: 100).
        ordem (str, opcional): "ASC" ou "DESC" (padrão: "DESC").
        ordenarPor (str, opcional): Campo para ordenação (padrão: "id").
        paginate (bool, opcional): 
            Se True, ativa a paginação automática e busca todas as páginas disponíveis 
            (padrão: False).
        params (dict, opcional): Dicionário adicional de parâmetros.
        **extra: Parâmetros adicionais compatíveis com versões futuras.

    Returns:
        dict: Resposta JSON contendo os órgãos encontrados e metadados de paginação.

    Example:
        >>> orgaos(sigla="CCJ", ordenarPor="sigla")
    """
    
    return build_api_call("orgaos", locals(), exclude=["paginate"], paginate=paginate)

def orgaos_id(id):
    """
    Retorna informações detalhadas sobre um órgão legislativo.

    Endpoint: `/orgaos/{id}`

    Args:
        id (int | str): Identificador único do órgão legislativo.

    Returns:
        dict: Informações completas do órgão, incluindo tipo, situação, data
        de criação e encerramento, membros e vinculações.

    Example:
        >>> orgaos_id(180)
    """
    return build_api_call("orgaos", subpath=f"{id}")

def orgaos_id_eventos(
                    id=None,
                    idTipoEvento=None,
                    dataInicio=None,
                    dataFim=None,
                    pagina=1,
                    itens=10,
                    ordem="DESC",
                    ordenarPor="dataHoraInicio",
                    paginate=False,
                    params=None,
                    **extra
                ):
    """
    Retorna eventos realizados (ou agendados) por um órgão legislativo.

    Endpoint: `/orgaos/{id}/eventos`

    Por padrão, são retornados eventos em andamento ou previstos para
    o mesmo dia, dois dias antes e dois dias depois da requisição.

    É possível alterar esse intervalo com os parâmetros `dataInicio` e `dataFim`,
    bem como filtrar por tipo de evento.

    Args:
        id (int | str): Identificador do órgão.
        idTipoEvento (int, opcional): Código numérico do tipo de evento (ex.: reunião, audiência).
        dataInicio (str, opcional): Data inicial (YYYY-MM-DD).
        dataFim (str, opcional): Data final (YYYY-MM-DD).
        pagina (int, opcional): Página de resultados (padrão: 1).
        itens (int, opcional): Quantidade de registros por página (padrão: 10).
        ordem (str, opcional): "ASC" ou "DESC" (padrão: "DESC").
        ordenarPor (str, opcional): Campo de ordenação (padrão: "dataHoraInicio").
        paginate (bool, opcional): 
            Se True, ativa a paginação automática e busca todas as páginas disponíveis 
            (padrão: False).
        params (dict, opcional): Parâmetros adicionais aceitos pela API.
        **extra: Campos adicionais compatíveis com futuras versões.

    Returns:
        dict: Lista resumida de eventos realizados ou planejados.

    Example:
        >>> orgaos_id_eventos(180, dataInicio="2025-02-01", dataFim="2025-02-05")
    """
    
    if(id is None):
        return "Necessário passar um id de orgão"
    
    return build_api_call(
        "orgaos",
        locals(),
        exclude=["id", "paginate"],
        subpath=f"{id}/eventos",
        paginate=paginate
    )

def orgaos_id_membros(
                    id=None,
                    dataInicio=None,
                    dataFim=None,
                    pagina=1,
                    itens=10,
                    paginate=False,
                    params=None,
                    **extra
                ):
    """
    Retorna os membros (parlamentares) de um órgão legislativo.

    Endpoint: `/orgaos/{id}/membros`

    Retorna uma lista com dados resumidos dos parlamentares que ocuparam
    cargos ou posições no órgão identificado por {id} durante um período.

    Se o período não for especificado, são retornados os membros vigentes
    no momento da requisição. Se o órgão estiver extinto, retorna lista vazia.

    Args:
        id (int | str): Identificador do órgão.
        dataInicio (str, opcional): Data inicial (YYYY-MM-DD).
        dataFim (str, opcional): Data final (YYYY-MM-DD).
        pagina (int, opcional): Página de resultados (padrão: 1).
        itens (int, opcional): Quantidade de registros por página (padrão: 10).
        paginate (bool, opcional): 
            Se True, ativa a paginação automática e busca todas as páginas disponíveis 
            (padrão: False).
        params (dict, opcional): Parâmetros adicionais aceitos pela API.
        **extra: Campos adicionais compatíveis com futuras versões.

    Returns:
        dict: Lista de membros e cargos exercidos no órgão.

    Example:
        >>> orgaos_id_membros(180)
    """
    
    if(id is None):
        return "Necessário passar um id de orgão"
    
    return build_api_call(
        "orgaos",
        locals(),
        exclude=["id","paginate"],
        subpath=f"{id}/membros",
        paginate=paginate
    )

def orgaos_id_votacoes(
                    id=None,
                    idProposicao=None,
                    dataInicio=None,
                    dataFim=None,
                    pagina=1,
                    itens=10,
                    ordenarPor="dataHoraRegistro",
                    ordem="DESC",
                    paginate=False,
                    params=None,
                    **extra
                ):
    """
    Retorna as votações realizadas em eventos de um órgão legislativo.

    Endpoint: `/orgaos/{id}/votacoes`

    Se o órgão for permanente (ex.: Plenário, Comissão Permanente),
    são retornadas, por padrão, as votações dos últimos 30 dias.
    Esse período pode ser alterado com `dataInicio` e/ou `dataFim`.

    Para órgãos temporários (ex.: Comissão Especial), são listadas
    todas as votações realizadas durante sua existência.

    Args:
        id (int | str): Identificador do órgão.
        idProposicao (int, opcional): ID da proposição votada.
        dataInicio (str, opcional): Data inicial (YYYY-MM-DD).
        dataFim (str, opcional): Data final (YYYY-MM-DD).
        pagina (int, opcional): Página de resultados (padrão: 1).
        itens (int, opcional): Quantidade de registros por página (padrão: 10).
        ordenarPor (str, opcional): Campo de ordenação (padrão: "dataHoraRegistro").
        ordem (str, opcional): "ASC" ou "DESC" (padrão: "DESC").
        paginate (bool, opcional): 
            Se True, ativa a paginação automática e busca todas as páginas disponíveis 
            (padrão: False).
        params (dict, opcional): Parâmetros adicionais aceitos pela API.
        **extra: Campos adicionais compatíveis com futuras versões.

    Returns:
        dict: Lista de votações com identificadores, proposições e datas.

    Example:
        >>> orgaos_id_votacoes(180, dataInicio="2025-01-01", dataFim="2025-01-31")
    """
    
    if(id is None):
        return "Necessário passar um id de orgão"
    
    return build_api_call(
        "orgaos",
        locals(),
        exclude=["id","paginate"],
        subpath=f"{id}/votacoes",
        paginate=paginate
    )

################################################################
## PARTIDOS
################################################################

def partidos(
                sigla=None,
                idLegislatura=None,
                dataInicio=None,
                dataFim=None,
                pagina=1,
                itens=100,
                ordem="DESC",
                ordenarPor="sigla",
                paginate=False,
                params=None,
                **extra
            ):
    """
    Lista partidos políticos representados na Câmara dos Deputados.

    Endpoint: `/partidos`

    Retorna informações básicas sobre os partidos políticos que têm ou já tiveram
    deputados em exercício na Câmara. Se não forem passados parâmetros, o serviço
    retorna apenas os partidos com representação ativa no momento da requisição.

    É possível filtrar por sigla, legislatura ou período de tempo em que o partido
    esteve representado. Caso sejam informados intervalos e legislaturas diferentes,
    todos os períodos serão considerados na busca.

    Args:
        sigla (str | list[str], opcional): Sigla ou lista de siglas dos partidos (ex.: "PT", "PL").
        idLegislatura (int | list[int], opcional): Número da legislatura ou lista de legislaturas.
        dataInicio (str, opcional): Data inicial do intervalo (YYYY-MM-DD).
        dataFim (str, opcional): Data final do intervalo (YYYY-MM-DD).
        pagina (int, opcional): Página de resultados (padrão: 1).
        itens (int, opcional): Quantidade de registros por página (padrão: 100).
        ordem (str, opcional): "ASC" ou "DESC" (padrão: "DESC").
        ordenarPor (str, opcional): Campo de ordenação (padrão: "sigla").
        paginate (bool, opcional): 
            Se True, ativa a paginação automática e busca todas as páginas disponíveis 
            (padrão: False).
        params (dict, opcional): Parâmetros adicionais aceitos pela API.
        **extra: Parâmetros extras compatíveis com futuras versões da API.

    Returns:
        dict: Resposta JSON com a lista de partidos e informações básicas.

    Example:
        >>> partidos()
        >>> partidos(sigla="PT", idLegislatura=57)
        >>> partidos(dataInicio="2018-01-01", dataFim="2022-12-31")
    """
    return build_api_call("partidos", locals(), exclude=["paginate"], paginate=paginate)

def partidos_id(id):
    """
    Retorna informações detalhadas sobre um partido político.

    Endpoint: `/partidos/{id}`

    Fornece dados completos sobre o partido identificado por {id},
    incluindo sigla, nome, número eleitoral, data de criação, situação
    e legislaturas em que esteve ativo.

    Args:
        id (int | str): Identificador único do partido.

    Returns:
        dict: Detalhes do partido solicitado.

    Example:
        >>> partidos_id(36844)
    """
    return build_api_call("partidos", subpath=f"{id}")

def partidos_id_lideres(
                    id=None,
                    pagina=1,
                    itens=10,
                    paginate=False,
                    params=None,
                    **extra
                ):
    """
    Lista deputados que ocuparam cargos de liderança no partido.

    Endpoint: `/partidos/{id}/lideres`

    Retorna deputados que exerceram cargos de **líder** ou **vice-líder**
    do partido identificado por {id}, juntamente com o tipo de cargo e
    o período de exercício.

    Por padrão, retorna os líderes atuais; pode-se usar parâmetros de data
    (quando disponíveis) para recuperar líderes históricos.

    Args:
        id (int | str): Identificador único do partido.
        pagina (int, opcional): Página de resultados (padrão: 1).
        itens (int, opcional): Quantidade de registros por página (padrão: 10).
        paginate (bool, opcional): 
            Se True, ativa a paginação automática e busca todas as páginas disponíveis 
            (padrão: False).
        params (dict, opcional): Parâmetros adicionais aceitos pela API.
        **extra: Campos extras compatíveis com futuras versões.

    Returns:
        dict: Lista de líderes e vice-líderes com período e cargo ocupado.

    Example:
        >>> partidos_id_lideres(36844)
    """
    
    if(id is None):
        return "Necessário passar um id de partidos"
    
    return build_api_call(
        "partidos",
        locals(),
        exclude=["id","pagiante"],
        subpath=f"{id}/lideres",
        paginate=paginate
    )

def partidos_id_membros(
                    id=None,
                    idLegislatura=None,
                    dataInicio=None,
                    dataFim=None,
                    pagina=1,
                    itens=10,
                    ordem="DESC",
                    ordenarPor="nome",
                    paginate=False,
                    params=None,
                    **extra
                ):
    """
    Lista os deputados filiados a um partido em determinado período.

    Endpoint: `/partidos/{id}/membros`

    Retorna uma lista de deputados que estão ou estiveram em exercício
    pelo partido identificado por {id}.

    Os filtros `dataInicio`, `dataFim` ou `idLegislatura` permitem delimitar
    o intervalo de filiação ou de exercício parlamentar.

    Este endpoint é funcionalmente equivalente ao serviço `/deputados`
    com filtro por partido, mas é mais adequado para consultar partidos
    extintos ou sem representação atual.

    Args:
        id (int | str): Identificador do partido.
        idLegislatura (int, opcional): Legislatura a ser filtrada.
        dataInicio (str, opcional): Data inicial do período (YYYY-MM-DD).
        dataFim (str, opcional): Data final do período (YYYY-MM-DD).
        pagina (int, opcional): Página de resultados (padrão: 1).
        itens (int, opcional): Número de registros por página (padrão: 10).
        ordem (str, opcional): "ASC" ou "DESC" (padrão: "DESC").
        ordenarPor (str, opcional): Campo de ordenação (padrão: "nome").
        paginate (bool, opcional): 
            Se True, ativa a paginação automática e busca todas as páginas disponíveis 
            (padrão: False).
        params (dict, opcional): Parâmetros adicionais aceitos pela API.
        **extra: Campos adicionais compatíveis com futuras versões.

    Returns:
        dict: Lista de deputados vinculados ao partido no período solicitado.

    Example:
        >>> partidos_id_membros(36844, idLegislatura=57)
        >>> partidos_id_membros(36844, dataInicio="2019-01-01", dataFim="2023-01-01")
    """
    
    if(id is None):
        return "Necessário passar um id de partidos"
    
    return build_api_call(
        "partidos",
        locals(),
        exclude=["id","paginate"],
        subpath=f"{id}/membros",
        paginate=paginate
    )

################################################################
## LEGISLATURAS
################################################################

def legislaturas(
                id=None,
                data=None,
                pagina=1,
                itens=100,
                ordem="DESC",
                ordenarPor="id",
                paginate=False,
                params=None,
                **extra
            ):
    """
    Legislatura é o nome dado ao período de trabalhos parlamentares entre uma eleição e outra.

    Este serviço retorna uma lista em que cada item contém as informações básicas sobre um desses períodos.

    Os números que identificam as legislaturas são sequenciais, desde a primeira que ocorreu.
    """
    return build_api_call("legislaturas", locals(), exclude=["paginate"], paginate=paginate)

def legislaturas_id(id):
    """
    Retorna informações adicionais sobre o período de atividades da Câmara identificado por {id}.
    """
    return build_api_call("legislaturas", subpath=f"{id}")

def legislaturas_id_lideres(
                    id=None,
                    pagina=1,
                    itens=10,
                    paginate=False,
                    params=None,
                    **extra
                ):
    """
    Retorna uma lista de parlamentares que ocuparam cargos de liderança ao longo da legislatura {id}.
    Cada item identifica um parlamentar, uma bancada (partido, bloco ou lideranças de situação e oposição),
    o título de liderança exercido e o período de exercício do parlamentar nesta posição.
    """
    
    if(id is None):
        return "Necessário passar um id de legislatura"
    
    return build_api_call(
        "legislaturas",
        locals(),
        exclude=["id","paginate"],
        subpath=f"{id}/lideres",
        paginate=paginate
    )

def legislaturas_id_mesa(
                    id=None,
                    dataInicio=None,
                    dataFim=None,
                    params=None,
                    **extra
                ):
    """
    Retorna uma lista com dados básicos sobre todos os deputados que ocuparam algum posto na Mesa
    Diretora da Câmara em algum período de tempo dentro da legislatura identificada por {id}.

    Normalmente, cada legislatura tem duas Mesas Diretoras, com presidente, dois vice-presidentes,
    quatro secretários parlamentares e os suplentes dos secretários.
    """
    
    if(id is None):
        return "Necessário passar um id de legislatura"
    
    return build_api_call(
        "legislaturas",
        locals(),
        exclude=["id"],
        subpath=f"{id}/mesa"
    )

################################################################
## BLOCOS
################################################################

def blocos(
    id=None,
    idLegislatura=None,
    pagina=1,
    itens=100,
    ordem="DESC",
    ordenarPor="nome",
    paginate=False,
    params=None,
    **extra
):
    """
    Lista os blocos parlamentares registrados na Câmara dos Deputados.

    Endpoint: `/blocos`

    Permite buscar blocos específicos por legislatura, nome, sigla ou intervalo
    de tempo em que estiveram ativos.

    Args:
        id (int, opcional: Número identificador de um bloco)
        idLegislatura (int, opcional): Número da legislatura (ex.: 57).
        pagina (int): Número da página (padrão: 1).
        itens (int): Quantidade de registros por página (padrão: 100).
        ordem (str): "ASC" ou "DESC" (padrão: "DESC").
        ordenarPor (str): Campo de ordenação (padrão: "nome").
        paginate (bool, opcional): 
            Se True, ativa a paginação automática e busca todas as páginas disponíveis 
            (padrão: False).
        params (dict, opcional): Parâmetros adicionais aceitos pela API.
        **extra: Campos adicionais compatíveis com futuras versões.

    Returns:
        dict: Resposta JSON com metadados e lista de blocos parlamentares.

    Example:
        >>> blocos(idLegislatura=57, ordenarPor="nome")
    """
    return build_api_call("blocos", locals(), exclude=["paginate"], paginate=paginate)


def blocos_id(id):
    """
    Retorna os detalhes de um bloco parlamentar específico.

    Endpoint: `/blocos/{id}`

    Args:
        id (int | str): Identificador único do bloco.

    Returns:
        dict: Informações detalhadas sobre o bloco parlamentar,
        incluindo nome, sigla, legislatura e situação.

    Example:
        >>> blocos_id(2829)
    """
    return build_api_call("blocos", subpath=f"{id}")


def blocos_id_partidos(id):
    """
    Retorna a lista de partidos que compõem um bloco parlamentar.

    Endpoint: `/blocos/{id}/partidos`

    Args:
        id (int | str): Identificador único do bloco parlamentar.

    Returns:
        dict: Lista de partidos integrantes do bloco, com sigla, nome e id.

    Example:
        >>> blocos_id_partidos(2829)
    """
    if id is None:
        raise ValueError("Necessário passar um id de bloco parlamentar.")

    return build_api_call("blocos", subpath=f"{id}/partidos")

################################################################
## FRENTES
################################################################

def frentes(
    idLegislatura=None,
    pagina=1,
    itens=100,
    paginate=False,
    params=None,
    **extra
):
    """
    Lista as frentes parlamentares registradas na Câmara dos Deputados.

    Endpoint: `/frentes`

    Permite buscar frentes parlamentares por legislatura, estado, partido ou nome.

    Args:
        idLegislatura (int, opcional): Identificador da legislatura (ex.: 57).
        pagina (int): Número da página (padrão: 1).
        itens (int): Quantidade de registros por página (padrão: 100).
        paginate (bool, opcional): 
            Se True, ativa a paginação automática e busca todas as páginas disponíveis 
            (padrão: False).
        params (dict, opcional): Dicionário adicional de parâmetros aceitos.
        **extra: Campos adicionais compatíveis com futuras versões.

    Returns:
        dict: Resposta JSON com metadados e lista de frentes parlamentares.

    Example:
        >>> frentes(idLegislatura=57)
    """
    return build_api_call("frentes", locals(), exclude=["paginate"], paginate=paginate)


def frentes_id(id):
    """
    Retorna as informações detalhadas de uma frente parlamentar específica.

    Endpoint: `/frentes/{id}`

    Args:
        id (int | str): Identificador único da frente parlamentar.

    Returns:
        dict: Informações completas sobre a frente, incluindo nome,
        descrição, legislatura e data de criação.

    Example:
        >>> frentes_id(207593)
    """
    return build_api_call("frentes", subpath=f"{id}")


def frentes_id_membros(id):
    """
    Retorna a lista de membros de uma frente parlamentar específica.

    Endpoint: `/frentes/{id}/membros`

    Args:
        id (int | str): Identificador único da frente parlamentar.

    Returns:
        dict: Lista de deputados membros da frente, incluindo nome, partido, UF e cargo.

    Example:
        >>> frentes_id_membros(207593)
    """
    if id is None:
        raise ValueError("Necessário passar um id de frente parlamentar.")

    return build_api_call("frentes", subpath=f"{id}/membros")

################################################################
## GRUPOS
################################################################

def grupos(pagina=1,
           itens=100,
           ordem="DESC",
           ordenarPor="id",
           paginate=False,
           params=None,
           **extra
):
    """
    Este endpoint retorna uma lista em que cada item representa um dos grupos interparlamentares em que a Câmara teve representantes.
    As informações incluem nome, a resolução que criou o grupo e seu ano de publicação, e as mais recentes informações sobre situação, presidente e ofício de instalação.

    Endpoint: `/grupos`

    Args:
        pagina (int): Número da página (padrão: 1).
        itens (int): Quantidade de registros por página (padrão: 100).
        ordem (str): "ASC" ou "DESC" (padrão: "DESC").
        ordenarPor (str): Campo de ordenação (padrão: "id").
        paginate (bool, opcional): 
            Se True, ativa a paginação automática e busca todas as páginas disponíveis 
            (padrão: False).
        params (dict, opcional): Dicionário adicional de parâmetros aceitos.
        **extra: Campos adicionais compatíveis com futuras versões.

    Returns:
        dict: Resposta JSON com metadados e lista de grupos parlamentares.

    Example:
        >>> grupos(pagina=1)
    """
    return build_api_call("grupos", locals(), exclude=["paginate"], paginate=paginate)

def grupos_id(id):
    """
    Todo o conjunto de informações disponíveis sobre o grupo parlamentar identificado por {id}.
    Além dos retornados por /grupos, há dados sobre o projeto de resolução que levou à criação do grupo,
    identificadores do mais recente documento e/ou ofício de instalação do grupo, datas de sua apresentação e de sua publicação, e identificação do autor do ofício.

    Endpoint: `/grupos/{id}`

    Args:
        id (int | str): Identificador único do grupo.

    Returns:
        dict: 

    Example:
        >>> grupos_id(74)
    """
    return build_api_call("grupos", subpath=f"{id}")

def grupos_id_historico(id):
    """
    Uma lista contendo todos os "retratos" das informações sujeitas a mudanças sobre o grupo parlamentar identificado por {id} — por exemplo,
    todos os ofícios de instalação dos grupos apresentados a cada legislatura desde sua criação, e eventuais substituições de presidentes.

    Endpoint: `/grupos/{id}/historico`

    Args:
        id (int | str): Identificador único do grupo.

    Returns:
        dict: 

    Example:
        >>> grupos_id_historico(74)
    """
    return build_api_call("grupos", subpath=f"{id}/historico")

def grupos_id_membros(id=None,
                      dataInicio="2000-01-01",
                      dataFim="2025-01-01",
                      ordem="DESC",
                      ordenarPor="idLegislatura",
                      paginate=False,
                      params=None,
                      **extra
                ):
    """
    Retorna uma lista de deputados ou senadores que são ou foram participantes do grupo interparlamentar identificado por {id}.
    Podem ser utilizados os parâmetros dataInicio e/ou dataFim para definir de qual período se deseja saber quem foram os participantes.
    
    Se nenhum parâmetro de tempo for utilizado, são retornados os integrantes registrados no momento da requisição (inclusive deputados e senadores que podem não estar em exercício).
    A lista será vazia se o grupo {id} ainda não tiver sido instalado na legislatura atual.
    """
    
    if(id is None):
        return "Necessário passar um id de grupo"
    
    return build_api_call(
        "grupos",
        locals(),
        exclude=["id","paginate"],
        subpath=f"{id}/membros",
        paginate=paginate
    )

################################################################
## EVENTOS
################################################################

def eventos(id=None,
            codTipoEvento=None,
            codSituacao=None,
            codTipoOrgao=None,
            idOrgao=None,
            dataInicio=None,
            dataFim=None,
            horaInicio=None,
            horaFim=None,
            pagina=1,
            itens=100,
            ordem="DESC",
            ordenarPor="dataHoraInicio",
            paginate=False,
            params=None,
            **extra
):
    """
    Retorna uma lista cujos elementos trazem informações básicas sobre eventos dos órgãos legislativos da Câmara,
    previstos ou já ocorridos, em um certo intervalo de tempo.

    Esse intervalo pode ser configurado pelos parâmetros de data e hora listados abaixo.
    Se nenhum for passado, são listados eventos dos cinco dias anteriores, dos cinco dias seguintes e do próprio dia em que é feita a requisição.
    
    Endpoint: `/eventos`

    Args:
        pagina (int): Número da página (padrão: 1).
        itens (int): Quantidade de registros por página (padrão: 100).
        ordem (str): "ASC" ou "DESC" (padrão: "DESC").
        ordenarPor (str): Campo de ordenação (padrão: "id").
        paginate (bool, opcional): 
            Se True, ativa a paginação automática e busca todas as páginas disponíveis 
            (padrão: False).
        params (dict, opcional): Dicionário adicional de parâmetros aceitos.
        **extra: Campos adicionais compatíveis com futuras versões.

    Returns:
        dict: Resposta JSON com metadados e lista de grupos parlamentares.

    Example:
        >>> 
    """
    return build_api_call("eventos", locals(), exclude=["paginate"], paginate=paginate)

def eventos_id(id):
    """
    Retorna um conjunto detalhado de informações sobre o evento da Câmara identificado por id.
    
    Endpoint: `/eventos/{id}`

    Args:
        id (int | str): Identificador único do evento.

    Returns:
        dict: 

    Example:
        >>> eventos_id(78938)
    """
    return build_api_call("eventos", subpath=f"{id}")

def eventos_id_deputados(id):
    """
    Retorna uma lista de dados resumidos sobre deputados participantes do evento identificado por {id}.
    Se o evento já ocorreu, a lista identifica os deputados que efetivamente registraram presença no evento.
    Se o evento ainda não ocorreu, a lista mostra os deputados que devem participar do evento,
    por serem convidados ou por serem membros do(s) órgão(s) responsável pelo evento.
    
    Endpoint: `/eventos/{id}/deputados`

    Args:
        id (int | str): Identificador único do evento.

    Returns:
        dict: 

    Example:
        >>> eventos_id_deputados(79206)
    """
    return build_api_call("eventos", subpath=f"{id}/deputados")

def eventos_id_orgaos(id):
    """
    Retorna uma lista em que cada item é um conjunto mínimo de dados sobre o(s) órgão(s) responsável(veis)
    pelo evento identificado por {id}.
    Atualmente, mas provisoriamente, esta informação já vem incorporada ao retorno de /eventos/{id},
    mas este endpoint facilita a importação destes dados em planilhas eletrônicas.
    
    Endpoint: `/eventos/{id}/orgaos`

    Args:
        id (int | str): Identificador único do evento.

    Returns:
        dict: 

    Example:
        >>> eventos_id_orgaos(79206)
    """
    return build_api_call("eventos", subpath=f"{id}/orgaos")

def eventos_id_pauta(id):
    """
    Se o evento {id} for de caráter deliberativo (uma reunião ordinária, por exemplo) este serviço
    retorna a lista de proposições previstas para avaliação pelos parlamentares.
    
    Cada item identifica, se as informações estiverem disponíveis, a proposição avaliada,
    o regime de preferência para avaliação, o relator e seu parecer,
    o resultado da apreciação e a votação realizada.
    
    Endpoint: `/eventos/{id}/pauta`

    Args:
        id (int | str): Identificador único do evento.

    Returns:
        dict: 

    Example:
        >>> eventos_id_pauta(79206)
    """
    return build_api_call("eventos", subpath=f"{id}/pauta")

def eventos_id_votacoes(id):
    """
    Retorna uma lista de dados básicos sobre votações que tenham sido realizadas no evento identificado por {id}.
    Votações só ocorrem em eventos de caráter deliberativo. Dados complementares sobre cada votação listada
    podem ser obtidos no recurso /votacoes/{id}.
    
    É comum ocorrer timeout nesta chamada.
    
    Endpoint: `/eventos/{id}/votacoes`

    Args:
        id (int | str): Identificador único do evento.

    Returns:
        dict: 

    Example:
        >>> eventos_id_votacoes(79206)
    """
    return build_api_call("eventos", subpath=f"{id}/votacoes")