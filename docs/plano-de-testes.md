# 🧪 Casos de Teste — SEA Tecnologia

## Legenda de Status
| Status | Significado |
|--------|-------------|
| ✅ Passou | Comportamento correto |
| ❌ Falhou | Bug encontrado |
| ⏳ Pendente | Ainda não executado |

---

## CT-001 — Conformidade Visual com o Protótipo

**Objetivo:** Verificar se a aplicação reflete o design proposto no protótipo.

| # | Item Verificado | Esperado | Obtido | Status |
|---|----------------|----------|--------|--------|
| 1 | Fonte tipográfica | Fonte grossa conforme protótipo | Fonte fina | ❌ |
| 2 | Cor do tema azul | Azul acinzentado | Azul claro | ❌ |
| 3 | Stepper — quantidade de itens | 9 itens | 9 itens | ✅ |
| 4 | Stepper — labels | Item 1, Item 2... Item 9 | ITEM 1 repetido 9x | ❌ |
| 5 | Stepper — capitalização | Capitalização normal | MAIÚSCULO | ❌ |
| 6 | Stepper — estado dos ícones | Só 1º ativo, demais cinza | Todos ativos (azul) | ❌ |
| 7 | Botões de navegação (Próximo/Passo) | Presentes no fluxo | Ausentes | ❌ |

**Resultado:** ❌ Falhou

---

## CT-002 — Validação de Campos Obrigatórios

**Objetivo:** Verificar se o formulário bloqueia o envio quando campos obrigatórios estão vazios.

**Passos:**
1. Acessar a aplicação
2. Clicar em "+ Adicionar Funcionário"
3. Não preencher nenhum campo
4. Clicar em Salvar

**Resultado Esperado:** Mensagens de erro indicando campos obrigatórios.

**Resultado Obtido:** Mensagem "Preencha este campo" exibida corretamente no campo Nome.

**Status:** ✅ Passou

---

## CT-003 — Validação de CPF

**Objetivo:** Verificar se o sistema valida corretamente o CPF informado.

| # | Cenário | CPF Informado | Resultado Esperado | Resultado Obtido | Status |
|---|---------|--------------|-------------------|-----------------|--------|
| 1 | CPF inválido | 111.111.111-11 | Mensagem de erro | CPF aceito sem validação | ❌ |
| 2 | CPF sem máscara | 11111111111 | Formatação automática | Sem máscara | ❌ |
| 3 | CPF incompleto | 123.456.789 | Bloquear ou alertar | Aceito truncado | ❌ |

**Status:** ❌ Falhou — BUG-005 e BUG-006 confirmados

---

## CT-004 — Validação de Data

**Objetivo:** Verificar se o sistema valida corretamente as datas informadas.

| # | Cenário | Data Informada | Resultado Esperado | Resultado Obtido | Status |
|---|---------|---------------|-------------------|-----------------|--------|
| 1 | Data inválida | 32/13/2024 | Mensagem de erro | Data bloqueada, limitou para 31/12/2024 | ✅ |
| 2 | Data válida | 01/01/1990 | Aceitar | Aceito corretamente | ✅ |

**Status:** ✅ Passou

---

## CT-005 — Adicionar EPI e Atividades

**Objetivo:** Verificar se é possível adicionar EPIs e atividades ao cadastro.

**Resultado Obtido:**
- ✅ Checkbox "O trabalhador não usa EPI" presente
- ✅ Dropdown "Selecione a atividade" presente
- ✅ Dropdown "Selecione o EPI" presente
- ✅ Campo "Informe o número do CA" presente
- ✅ Botão "Adicionar EPI" presente
- ✅ Botão "Adicionar outra atividade" presente
- ⚠️ Label do dropdown truncada "Ativid 01" — BUG-007

**Status:** ✅ Passou parcialmente

---

## CT-006 — Persistência de Dados

**Objetivo:** Verificar se os dados do funcionário são salvos corretamente.

**Passos:**
1. Preencher o formulário com dados válidos
2. Clicar em Salvar
3. Verificar se o funcionário aparece na lista

**Resultado Obtido:** Funcionário salvo e exibido na lista corretamente.

**Status:** ✅ Passou

---

## CT-007 — Recuperação de Dados

**Objetivo:** Verificar se é possível visualizar um funcionário cadastrado.

**Resultado Obtido:** Funcionário visível na lista com nome, CPF e cargo.

**Status:** ✅ Passou

---

## CT-008 — Edição de Registro

**Objetivo:** Verificar se é possível editar os dados de um funcionário.

**Passos:**
1. Localizar um funcionário na lista
2. Clicar no menu de opções (...)
3. Selecionar "Editar"

**Resultado Obtido:** Menu (...) não responde ao clique. Impossível editar.

**Status:** ❌ Falhou — BUG-008

---

## CT-009 — Exclusão de Registro

**Objetivo:** Verificar se é possível excluir um funcionário.

**Passos:**
1. Localizar um funcionário na lista
2. Clicar no menu de opções (...)
3. Selecionar "Excluir"

**Resultado Obtido:** Menu (...) não responde ao clique. Impossível excluir.

**Status:** ❌ Falhou — BUG-008

---

## CT-010 — Navegação entre Menus e Links

**Objetivo:** Verificar se todos os links levam ao componente "Em breve".

| # | Item | Resultado Esperado | Resultado Obtido | Status |
|---|------|--------------------|-----------------|--------|
| 1 | Menu lateral — ícones | Tela "Em breve" | Nenhuma ação | ❌ |
| 2 | Botão "Próximo passo" | Próxima etapa | Nenhuma ação | ❌ |

**Status:** ❌ Falhou — BUG-010 e BUG-011

---

## CT-011 — Compatibilidade com Navegadores

**Objetivo:** Verificar se a aplicação funciona nos principais navegadores.

| # | Navegador | Resultado |
|---|-----------|-----------|
| 1 | Google Chrome | ✅ Funciona corretamente |
| 2 | Microsoft Edge | ✅ Funciona corretamente |
| 3 | Mozilla Firefox | ⏳ Não testado |

**Status:** ✅ Passou

---

## 📊 Resumo Final

| Status | Quantidade |
|--------|------------|
| ✅ Passou | 6 |
| ❌ Falhou | 5 |
| ⏳ Pendente | 0 |
| **Total** | **11** |
