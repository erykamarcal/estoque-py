
# Sistema de Controle de Estoque de Uniformes

Aplicação simples de linha de comando desenvolvida em Python para praticar lógica de programação, estruturas de dados e organização de código.

O sistema permite consultar e administrar um estoque de uniformes, registrando peças por nome, tamanho e cor.

## Funcionalidades

- **Visualizar estoque:** lista as peças cadastradas, suas características e quantidades, além de exibir o total de unidades.
- **Cadastrar peça:** adiciona uma nova combinação de peça, tamanho e cor ao estoque.
- **Adicionar quantidade:** registra a entrada de unidades de uma peça existente.
- **Remover quantidade:** registra a saída de unidades, impedindo a remoção de uma quantidade maior que a disponível.
- **Buscar por categoria:** filtra os itens por categoria.

## Tecnologias e conceitos

- Python 3
- Programação estruturada e funções
- Listas e dicionários
- Estruturas condicionais e de repetição
- List comprehensions
- Manipulação de strings
- Tratamento de exceções com `try/except`
- Entrada e saída de dados pelo terminal
- Biblioteca padrão `datetime`

## Como executar

1. Certifique-se de ter o Python 3 instalado.
2. Clone este repositório:

   ```bash
   git clone https://github.com/SEU-USUARIO/estoque-uniformes.git
   ```

3. Acesse a pasta do projeto:

   ```bash
   cd estoque-uniformes
   ```

4. Execute o programa:

   ```bash
   python estoque-uniformes.py
   ```

   No Windows, também é possível utilizar:

   ```bash
   py estoque-uniformes.py
   ```

## Observações

- O estoque inicial é definido diretamente no código.
- Os dados são mantidos em memória durante a execução. Ao encerrar o programa, as alterações realizadas não são salvas.
- O projeto não utiliza banco de dados nem bibliotecas externas.

## Objetivo de aprendizagem

Projeto desenvolvido como prática introdutória de Python, com o objetivo de compreender a sintaxe da linguagem, trabalhar com estruturas de dados e aplicar conceitos de lógica de programação em uma situação prática.

Também representa um primeiro passo no aprofundamento em Python, com interesse em explorar futuramente scripts e automações.

## Possíveis melhorias

- Persistir os dados em arquivos JSON.
- Separar o código em módulos.
- Implementar validações mais completas para os campos.
- Criar testes automatizados.
- Explorar a automação de tarefas com Python.

---

Projeto de estudos — Python.
