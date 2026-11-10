# QA Automation — SauceDemo

Projeto de estudos de Quality Assurance aplicado a um e-commerce de demonstração.

## Objetivo
Validar fluxos críticos de autenticação e carrinho de compras utilizando testes manuais e automatizados.

## Tecnologias
- Python
- Pytest
- Playwright
- GitHub Actions

## Escopo dos testes
- Login válido
- Login com senha incorreta
- Login com campos vazios
- Adição de produto ao carrinho
- Casos manuais de remoção e checkout

## Como executar
1. Criar e ativar um ambiente virtual Python.
2. Instalar as dependências: `pip install -r requirements.txt`
3. Instalar o navegador: `python -m playwright install chromium`
4. Executar os testes: `python -m pytest -v`

## Evidências
Os casos manuais, resultados de execução e eventuais defeitos estão documentados na pasta `docs/`.

## Aprendizados
Prática de elaboração de casos de teste, testes positivos e negativos, asserções, automação web e análise de falhas.

## Status
Projeto de aprendizado em desenvolvimento.
