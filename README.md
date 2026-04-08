# 🧪 Desafio QA — SEA Tecnologia

Repositório do desafio técnico para a vaga de Analista de Teste.

## 📁 Estrutura do Projeto

- `docs/` — Documentação dos testes
  - `plano-de-testes.md` — Plano geral de testes
  - `casos-de-teste.md` — Casos de teste detalhados
  - `bugs-reportados.md` — Bugs encontrados
  - `relatorio-final.md` — Relatório final
- `evidencias/` — Prints e vídeos das evidências
- `automacao/` — Scripts de testes automatizados

## 🔗 Links
- **Aplicação testada:** http://analista-teste.seatecnologia.com.br/
- **Protótipo:** https://tinyurl.com/yl58hs4m

## ⚙️ Como rodar os testes automatizados

### Pré-requisitos
- Python 3.13 ou superior
- Google Chrome instalado

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/athyagoz/desafio-qa-sea.git
```

2. Acesse a pasta de automação:
```bash
cd desafio-qa-sea/automacao
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

### Executando os testes
```bash
python -m unittest test_selenium.py -v
```

### O que cada teste faz

| Teste | Descrição |
|-------|-----------|
| test_01_campos_obrigatorios | Valida se campos obrigatórios bloqueiam envio |
| test_02_cpf_invalido | Verifica se CPF inválido é rejeitado |
| test_03_persistencia_dados | Testa se dados são salvos corretamente |
| test_04_navegacao_menu | Verifica navegação do menu lateral |

## Observação

Este projeto foi desenvolvido com foco em demonstrar habilidades em testes manuais e automação. Também foi aplicada uma estrutura inicial com Page Object Model visando boas práticas e evolução contínua.

## 👤 Candidato
Alyson — Processo Seletivo SEA Tecnologia 2026
