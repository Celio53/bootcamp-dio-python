# 📚 Recursos e Materiais de Apoio

Guia consolidado de materiais, documentações, ferramentas e links organizados por semana e contexto de aprendizado.

---

## 🎓 Plataforma Principal

* **Trilha Oficial na DIO:** [Santander Bootcamp - Dados com Python e IA](https://web.dio.me/track/a0568308-55de-4e1b-9de6-89aed90a6796)
  * *Observação:* Acesse com o e-mail cadastrado na bolsa aprovada pelo Santander.
* **Ambiente Local Recomendado:**
  * **Editor:** [VS Code](https://code.visualstudio.com/) com extensões *Python* e *Jupyter*.
  * **Terminal/Sistema:** WSL2 (Ubuntu no Windows) ou terminal nativo do Python 3.
  * **Gerenciador de Ambientes:** `python -m venv .venv` para isolamento de dependências.

---

## 🗓️ Materiais por Semana

### 🔹 Semana 1: Fundamentos de Python e Estruturas de Dados
* **Módulos DIO:**
  * Introdução ao Ambiente Python e Primeiros Comandos.
  * Tipos de Operadores com Python.
  * Estruturas Condicionais e de Repetição em Python.
  * Conhecendo Estruturas de Dados em Python (Listas, Tuplas, Conjuntos, Dicionários).
* **Documentação & Guias Rápidos:**
  * [Python.org - Tutorial Oficial (em Português)](https://docs.python.org/pt-br/3/tutorial/index.html)
  * [W3Schools - Python Data Types & Collections](https://www.w3schools.com/python/)
* **Comandos Úteis de Terminal:**
  ```bash
  # Criar e ativar ambiente virtual
  python -m venv .venv
  source .venv/bin/activate  # No WSL / Linux
  # .venv\Scripts\Activate.ps1 # No Windows PowerShell
  ```

---

### 🔹 Semana 2: Programação Orientada a Objetos (POO) e Manipulação de Arquivos
* **Módulos DIO:**
  * Aprendendo o Conceito de Herança com Python.
  * Aplicando Encapsulamento em Python.
  * Polimorfismo e Interfaces.
  * Manipulação de Arquivos em Python (`open`, leitura, gravação e boas práticas).
  * Gerenciamento de Pacotes e Boas Práticas (PEP 8).
* **Documentação & Guias Rápidos:**
  * [Documentação Python - Classes](https://docs.python.org/pt-br/3/tutorial/classes.html)
  * [Documentação Python - Módulo nativo `csv`](https://docs.python.org/pt-br/3/library/csv.html)
  * [Real Python - Reading and Writing CSV Files in Python](https://realpython.com/python-csv/)

---

### 🔹 Semana 3: Análise e Manipulação de Dados com Pandas
* **Módulos DIO:**
  * Introdução ao ecossistema de análise de dados.
  * Trabalhando com Pandas: Series e DataFrames.
  * Limpeza, tratamento e transformação de dados tabulares.
  * Agrupamento e agregação com `groupby`.
* **Documentação & Guias Rápidos:**
  * [Pandas Official Documentation](https://pandas.pydata.org/docs/)
  * [Pandas Cheat Sheet (Folha de Consulta Rápida)](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
  * [10 Minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
* **Datasets Recomendados para Prática com seu Background:**
  * Bases públicas de RH / People Analytics (ex: desligamento de colaboradores - *Employee Churn* no Kaggle).
  * Bases de chamados de atendimento ao cliente (tempo de resolução, canal de contato, nota de satisfação CSAT).

---

### 🔹 Semana 4: Visualização de Dados, IA Generativa & Projeto Integrado
* **Módulos DIO:**
  * Visualização de dados com Matplotlib e Seaborn.
  * Introdução à Inteligência Artificial Generativa e Engenharia de Prompt.
  * Projeto Prático Final Integrador.
* **Documentação & Guias Rápidos:**
  * [Matplotlib - Exemplos e Tutoriais](https://matplotlib.org/stable/tutorials/index.html)
  * [Seaborn - Galeria de Gráficos e Estilos](https://seaborn.pydata.org/examples/index.html)
  * [Guia de Engenharia de Prompt da Anthropic / OpenAI / Google](https://www.promptingguide.ai/pt)
  * [Google AI Studio (Gemini API)](https://aistudio.google.com/)
* **Livro Recomendado para Storytelling:**
  * *Storytelling com Dados: Um guia sobre visualização de dados para profissionais de negócios* (Cole Nussbaumer Knaflic).

---

## 💡 Dicas de Produtividade para a Rotina de 1h/dia

1. **Método 30/30:** Bloqueie na sua agenda 30 minutos ininterruptos para aula/quiz na DIO e, em seguida, abra o VS Code para codificar por mais 30 minutos.
2. **Versionamento:** Ao final de cada semana, realize um commit com suas anotações e códigos para registrar sua evolução no GitHub.
3. **Foco Prático:** Sempre que aprender um comando de código, imagine: *"Como eu usaria isso para resolver uma dor real no SAC ou no RH?"*
