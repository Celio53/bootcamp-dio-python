# 📅 Cronograma Semanal de Estudos (30 Dias)

> **Regra de Ouro:** 1 hora diária consistente = **30 min Teoria/DIO** + **30 min Prática no VS Code/WSL**.

---

## 🗓️ Semana 1: Fundamentos de Python e Estruturas de Dados

* **Foco na Trilha DIO:** Sintaxe inicial, controle de fluxo e coleções em Python.
* **Objetivo:** Adquirir fluência na linguagem e saber estruturar coleções de dados em memória.

### 📋 Roteiro Diário

* [ ] **Dia 01: Primeiros Passos & Ambiente**
  * **Teoria (30 min):** Introdução à linguagem Python, variáveis, tipos primitivos (`int`, `float`, `str`, `bool`) e operadores aritméticos na DIO.
  * **Prática (30 min):** Configurar o ambiente no VS Code com terminal WSL, criar o script `dia01.py` e testar operações e formatação de strings (`f-strings`).
* [ ] **Dia 02: Entrada de Dados e Operadores Lógicos**
  * **Teoria (30 min):** Operadores lógicos (`and`, `or`, `not`), de comparação e entrada com `input()`.
  * **Prática (30 min):** Criar um simulador de triagem básica de chamado de SAC (classificação por urgência).
* [ ] **Dia 03: Estruturas Condicionais**
  * **Teoria (30 min):** Controle de fluxo com `if`, `elif`, `else` e condicionais aninhadas.
  * **Prática (30 min):** Script para categorizar tempo de resposta de atendimento ou elegibilidade de benefício de funcionário.
* [ ] **Dia 04: Estruturas de Repetição (for e while)**
  * **Teoria (30 min):** Laços `for` (com função `range()`), `while`, comandos `break` e `continue`.
  * **Prática (30 min):** Iterar sobre listas de notas de satisfação (CSAT) e calcular a média manualmente.
* [ ] **Dia 05: Tuplas e Métodos de Strings**
  * **Teoria (30 min):** Imutabilidade de tuplas, desempacotamento e principais métodos de manipulação de texto (`split`, `strip`, `lower`, `replace`).
  * **Prática (30 min):** Higienizar nomes e textos de feedbacks de clientes/colaboradores.
* [ ] **Dia 06: Listas e List Comprehensions**
  * **Teoria (30 min):** Métodos de listas (`append`, `extend`, `pop`, `sort`, `slicing`).
  * **Prática (30 min):** Filtrar e transformar listas numéricas usando laços tradicionais e *list comprehension*.
* [ ] **Dia 07: Dicionários e Conjuntos (Sets)**
  * **Teoria (30 min):** Estruturas chave-valor (dicionários), métodos (`keys`, `values`, `items`) e remoção de duplicatas com `set`.
  * **Prática (30 min):** Criar um dicionário simulando dados de um colaborador ou ticket de suporte e extrair métricas de contagem.

---

## 🗓️ Semana 2: Programação Orientada a Objetos (POO) e Manipulação de Arquivos

* **Foco na Trilha DIO:** Paradigma de Orientação a Objetos e persistência de dados em arquivos.
* **Objetivo:** Organizar códigos em estruturas reutilizáveis e manipular arquivos de texto e tabelas CSV.

### 📋 Roteiro Diário

* [ ] **Dia 08: Introdução à POO (Classes e Objetos)**
  * **Teoria (30 min):** O que são classes, atributos e o método construtor `__init__`.
  * **Prática (30 min):** Criar a classe `Colaborador` ou `Atendimento` com atributos básicos e instanciar objetos.
* [ ] **Dia 09: Métodos de Instância e Encapsulamento**
  * **Teoria (30 min):** Comportamentos de classes, parâmetros `self`, atributos públicos e convenções de atributos privados.
  * **Prática (30 min):** Implementar métodos como `atualizar_status()` ou `calcular_tempo_atendimento()`.
* [ ] **Dia 10: Herança e Polimorfismo**
  * **Teoria (30 min):** Reutilização de código com herança de classes e sobrescrita de métodos.
  * **Prática (30 min):** Criar classes derivadas (ex: `AtendimentoCritico` herdando de `Atendimento`).
* [ ] **Dia 11: Tratamento de Exceções (Erros)**
  * **Teoria (30 min):** Blocos `try`, `except`, `else` e `finally`; boas práticas para não quebrar a execução.
  * **Prática (30 min):** Criar funções com validação robusta para evitar erros de divisão por zero ou conversão de tipo inválida.
* [ ] **Dia 12: Funções Avançadas (Decoradores e Geradores)**
  * **Teoria (30 min):** Conceito básico de funções como cidadãos de primeira classe, `*args`, `**kwargs`, decoradores simples e geradores com `yield`.
  * **Prática (30 min):** Criar um decorador simples que calcula o tempo de execução de uma função.
* [ ] **Dia 13: Leitura e Escrita de Arquivos de Texto (`open`, `.txt`)**
  * **Teoria (30 min):** Gerenciador de contexto `with open()`, modos de abertura (`'r'`, `'w'`, `'a'`).
  * **Prática (30 min):** Gravar logs de eventos e relatórios de texto automáticos gerados pelo terminal.
* [ ] **Dia 14: Manipulação de Arquivos Tabulares (`.csv`)**
  * **Teoria (30 min):** Módulo nativo `csv`, uso de `csv.reader` e `csv.DictWriter`.
  * **Prática (30 min):** Ler uma planilha `.csv` de histórico de atendimentos e gerar um novo `.csv` apenas com os casos pendentes.

---

## 🗓️ Semana 3: Análise e Manipulação de Dados com Pandas

* **Foco na Trilha DIO:** O ecossistema Pandas para análise exploratória de dados.
* **Objetivo:** Carregar, tratar, filtrar e sumarizar datasets tabulares do mundo real.

### 📋 Roteiro Diário

* [ ] **Dia 15: Introdução ao Pandas (Series e DataFrames)**
  * **Teoria (30 min):** Arquitetura do Pandas, diferenças entre Series (1D) e DataFrames (2D).
  * **Prática (30 min):** Criar DataFrames a partir de dicionários e explorar colunas e índices no Jupyter Notebook.
* [ ] **Dia 16: Leitura e Inspeção Inicial de Dados**
  * **Teoria (30 min):** `pd.read_csv()`, `pd.read_excel()`, métodos `.head()`, `.tail()`, `.info()` e `.describe()`.
  * **Prática (30 min):** Carregar um dataset público (ou fictício de RH/SAC) e inspecionar os tipos de colunas e volume de registros.
* [ ] **Dia 17: Tratamento de Dados Ausentes (Valores Nulos)**
  * **Teoria (30 min):** Identificação de nulos com `.isna()`, `.isnull()`, estratégias de exclusão (`.dropna()`) e imputação (`.fillna()`).
  * **Prática (30 min):** Tratar dados faltantes em campos de feedback de clientes ou datas de admissão.
* [ ] **Dia 18: Filtros e Seleção Condicional**
  * **Teoria (30 min):** Indexação com `.loc[]`, `.iloc[]` e máscaras booleanas com operadores lógicos (`&`, `|`).
  * **Prática (30 min):** Filtrar apenas atendimentos com nota menor que 5 ou colaboradores de um departamento específico.
* [ ] **Dia 19: Transformação e Criação de Novas Colunas**
  * **Teoria (30 min):** Operações vetorizadas, manipulação de texto em colunas (`.str.upper()`, `.str.contains()`) e aplicação de funções com `.apply()`.
  * **Prática (30 min):** Criar colunas de classificação de risco de desligamento ou faixa de tempo de resolução de chamados.
* [ ] **Dia 20: Agrupamentos e Agregações com `groupby`**
  * **Teoria (30 min):** O paradigma Split-Apply-Combine, métodos `.groupby()`, `.agg()`, `.sum()`, `.mean()`, `.count()`.
  * **Prática (30 min):** Calcular a média de tempo de atendimento por canal (Chat, E-mail, Telefone) ou rotatividade por setor.
* [ ] **Dia 21: Mesclagem e Combinação de Bases (`merge` e `concat`)**
  * **Teoria (30 min):** Equivalentes a JOINs de SQL no Pandas (`merge`, `left`, `inner`) e concatenação de tabelas.
  * **Prática (30 min):** Unir uma tabela de colaboradores com uma tabela de pesquisas de clima organizacional.

---

## 🗓️ Semana 4: Visualização de Dados, IA Generativa & Projeto Integrado

* **Foco na Trilha DIO:** Visualização gráfica, introdução à IA Generativa e integração de projeto final.
* **Objetivo:** Plotar insights visuais, utilizar IA como copilot de produtividade analítica e consolidar um projeto ponta a ponta.

### 📋 Roteiro Diário

* [ ] **Dia 22: Visualização de Dados com Matplotlib**
  * **Teoria (30 min):** Conceitos fundamentais de figuras, eixos (`plt.subplots()`), gráficos de linhas e dispersão.
  * **Prática (30 min):** Plotar a evolução temporal do volume de chamados ou contratações.
* [ ] **Dia 23: Visualização Estatística com Seaborn**
  * **Teoria (30 min):** Vantagens do Seaborn, gráficos categóricos (`barplot`, `countplot`) e distribuições (`histplot`, `boxplot`).
  * **Prática (30 min):** Criar gráficos de distribuição de satisfação (CSAT) segmentados por setor/atendente.
* [ ] **Dia 24: IA Generativa & Engenharia de Prompt para Análise**
  * **Teoria (30 min):** Modelos de linguagem (LLMs), formulação de prompts para geração de código analítico e explicação de anomalias estatísticas.
  * **Prática (30 min):** Usar o Gemini ou Copilot para gerar rotinas de limpeza de dados e sugerir perguntas exploratórias sobre um dataset.
* [ ] **Dia 25: Definição do Projeto Integrador Ponta a Ponta**
  * **Teoria (30 min):** Estrutura de um projeto de dados: Problema de Negócio -> Coleta/Carga -> Limpeza -> Análise -> Insights.
  * **Prática (30 min):** Definir o tema do seu projeto (exemplo: *Análise de Eficiência do Atendimento ao Cliente e Satisfação do Usuário* ou *Análise de Turn-over no RH*).
* [ ] **Dia 26: Projeto Integrador - Carga e Limpeza de Dados**
  * **Teoria (30 min):** Boas práticas de documentação em notebooks e reprodutibilidade do código.
  * **Prática (30 min):** Escrever o script/notebook executando o carregamento dos dados, remoção de duplicatas e tratamento de nulos.
* [ ] **Dia 27: Projeto Integrador - Análise Exploratória & Gráficos**
  * **Teoria (30 min):** Identificação de correlações e padrões ocultos nos dados.
  * **Prática (30 min):** Gerar 3 a 4 gráficos-chave que contem visualmente a situação identificada.
* [ ] **Dia 28: Projeto Integrador - Storytelling com Dados**
  * **Teoria (30 min):** Metodologia de Storytelling com Dados (contexto, público-alvo, clímax dos dados e chamada para ação).
  * **Prática (30 min):** Redigir os principais insights de negócio em linguagem clara para gestores, conectando causa e efeito.
* [ ] **Dia 29: Projeto Integrador - Refinamento e Revisão**
  * **Teoria (30 min):** Limpeza e formatação de código (PEP 8, comentários claros e modularização).
  * **Prática (30 min):** Revisar todo o script/notebook, garantindo execução fluida do início ao fim sem erros.
* [ ] **Dia 30: Apresentação Final & Próximos Passos**
  * **Teoria (30 min):** Como apresentar projetos de tecnologia em entrevistas e portfólio no GitHub/LinkedIn.
  * **Prática (30 min):** Escrever o relatório final do projeto, atualizar seu repositório no GitHub e celebrar a conclusão dos 30 dias!
