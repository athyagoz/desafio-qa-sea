#  Casos de Teste — SEA Tecnologia

## Legenda de Status
| Status | Significado |
|--------|-------------|
| Passou | Comportamento correto |
| Falhou | Bug encontrado |
| Pendente | Ainda não executado |

---

## CT-001 — Conformidade Visual com o Protótipo

**Objetivo:** Verificar se a aplicação reflete o design proposto no protótipo.

| # | Item Verificado | Esperado | Obtido | Status |
|---|----------------|----------|--------|--------|
| 1 | Fonte tipográfica | Fonte grossa conforme protótipo | Fonte fina |
| 2 | Cor do tema azul | Azul acinzentado | Azul claro |
| 3 | Stepper — quantidade de itens | 9 itens | 9 itens |
| 4 | Stepper — labels | Item 1, Item 2... Item 8 | ITEM 1 repetido 9x |
| 5 | Stepper — capitalização | Capitalização normal | MAIÚSCULO |
| 6 | Stepper — estado dos ícones | Só 1º ativo, demais cinza | Todos ativos (azul) |
| 7 | Botões de navegação (Próximo/Passo) | Presentes no fluxo | Ausentes |

---

## CT-002 — Validação de Campos Obrigatórios

**Objetivo:** Verificar se o formulário bloqueia o envio quando campos obrigatórios estão vazios.

**Pré-condição:** Acessar o formulário de cadastro de funcionário.

**Passos:**
1. Acessar a aplicação
2. Não preencher nenhum campo
3. Clicar em Salvar/Enviar

**Resultado Esperado:** Mensagens de erro indicando campos obrigatórios.

| Status | Resultado Obtido |
|--------|-----------------|
| Pendente | |

---

## 🪪 CT-003 — Validação de CPF

**Objetivo:** Verificar se o sistema valida corretamente o CPF informado.

**Pré-condição:** Acessar o formulário de cadastro.

| # | Cenário | CPF Informado | Resultado Esperado | Status |
|---|---------|--------------|-------------------|--------|
| 1 | CPF inválido | 111.111.111-11 | Mensagem de erro | 
| 2 | CPF com letras | ABC.DEF.GHI-JK | Bloquear entrada | 
| 3 | CPF válido | 123.456.789-09 | Aceitar | 
| 4 | CPF vazio | (em branco) | Mensagem de erro |

---

## CT-004 — Validação de Data

**Objetivo:** Verificar se o sistema valida corretamente as datas informadas.

| # | Cenário | Data Informada | Resultado Esperado | Status |
|---|---------|---------------|-------------------|--------|
| 1 | Data inválida | 32/13/2024 | Mensagem de erro | 
| 2 | Data futura | 01/01/2099 | Aceitar ou bloquear | 
| 3 | Data válida | 01/01/1990 | Aceitar | 
| 4 | Campo vazio | (em branco) | Mensagem de erro | 

---

## CT-005 — Adicionar EPI e Atividades

**Objetivo:** Verificar se é possível adicionar EPIs e atividades ao cadastro.

**Passos:**
1. Acessar o formulário de cadastro
2. Localizar o campo/botão de adicionar EPI
3. Adicionar um EPI
4. Localizar o campo/botão de adicionar atividade
5. Adicionar uma atividade

| Status | Resultado Obtido |
|--------|-----------------|
| Pendente | |

---

##  CT-006 — Persistência de Dados

**Objetivo:** Verificar se os dados do funcionário são salvos corretamente.

**Passos:**
1. Preencher o formulário com dados válidos
2. Clicar em Salvar
3. Verificar se o funcionário aparece na lista

| Status | Resultado Obtido |
|--------|-----------------|
| Pendente | |

---

##  CT-007 — Recuperação de Dados

**Objetivo:** Verificar se é possível buscar e visualizar um funcionário cadastrado.

**Passos:**
1. Ter um funcionário já cadastrado
2. Buscar pelo funcionário
3. Verificar se os dados aparecem corretamente

| Status | Resultado Obtido |
|--------|-----------------|
| Pendente | |

---

## CT-008 — Edição de Registro

**Objetivo:** Verificar se é possível editar os dados de um funcionário.

**Passos:**
1. Localizar um funcionário na lista
2. Clicar no menu de opções (...)
3. Selecionar "Editar"
4. Alterar algum dado
5. Salvar e verificar se a alteração foi aplicada

| Status | Resultado Obtido |
|--------|-----------------|
|  Pendente | |

---

##  CT-009 — Exclusão de Registro

**Objetivo:** Verificar se é possível excluir um funcionário.

**Passos:**
1. Localizar um funcionário na lista
2. Clicar no menu de opções (...)
3. Selecionar "Excluir"
4. Confirmar a exclusão
5. Verificar se o registro foi removido da lista

| Status | Resultado Obtido |
|--------|-----------------|
|  Pendente | |

---

## CT-010 — Navegação entre Menus e Links

**Objetivo:** Verificar se todos os links levam ao componente "Em breve".

**Passos:**
1. Clicar em cada item do menu lateral/superior
2. Verificar se redireciona para o componente "Em breve"

| # | Link/Menu | Resultado Esperado | Status |
|---|-----------|-------------------|--------|
| 1 | Menu item 1 | Componente "Em breve" | 
| 2 | Menu item 2 | Componente "Em breve" | 
| 3 | Menu item 3 | Componente "Em breve" | 

---

## CT-011 — Compatibilidade com Navegadores

**Objetivo:** Verificar se a aplicação funciona nos principais navegadores.

| # | Navegador | Versão | Resultado Esperado | Status |
|---|-----------|--------|--------------------|--------|
| 1 | Google Chrome | Mais recente | Funcionar corretamente | 
| 2 | Mozilla Firefox | Mais recente | Funcionar corretamente | 
| 3 | Microsoft Edge | Mais recente | Funcionar corretamente | 
