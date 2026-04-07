# 🧪 Casos de Teste — SEA Tecnologia

## Legenda de Status
| Status | Significado |
|--------|-------------|
| ✅ Passou | Comportamento correto |
| ❌ Falhou | Bug encontrado |
| ⏳ Pendente | Ainda não executado |

## Legenda de Prioridade
| Prioridade | Significado |
|------------|-------------|
| 🔴 Alta | Deve ser testado primeiro |
| 🟡 Média | Testado após os de alta prioridade |
| 🟢 Baixa | Testado por último |

---

## CT-001 — Conformidade Visual com o Protótipo
- **Prioridade:** 🟡 Média
- **Pré-condições:**
  - Ter acesso à aplicação: http://analista-teste.seatecnologia.com.br/
  - Ter acesso ao protótipo: https://tinyurl.com/yl58hs4m
  - Navegador Google Chrome versão 134 ou superior
- **Dados de teste:** Nenhum — apenas observação visual

| # | Item Verificado | Esperado | Obtido | Status |
|---|----------------|----------|--------|--------|
| CT-001-01 | Fonte tipográfica | Fonte grossa conforme protótipo | Fonte fina | ❌ |
| CT-001-02 | Cor do tema azul | Azul acinzentado (#5B7FA6) | Azul claro | ❌ |
| CT-001-03 | Stepper — quantidade | 9 ícones | 9 ícones | ✅ |
| CT-001-04 | Stepper — labels | Item 1, Item 2... Item 9 | ITEM 1 repetido 9x | ❌ |
| CT-001-05 | Stepper — capitalização | Capitalização normal | MAIÚSCULO | ❌ |
| CT-001-06 | Stepper — estado | Só 1º ativo, demais cinza | Todos ativos | ❌ |
| CT-001-07 | Botões de navegação | Presentes no fluxo | Ausentes | ❌ |

**Resultado geral:** ❌ Falhou
**Bugs relacionados:** BUG-001, BUG-002, BUG-003, BUG-004

---

## CT-002 — Validação de Campos Obrigatórios
- **Prioridade:** 🔴 Alta
- **Pré-condições:**
  - Aplicação acessível no navegador
  - Estar na tela principal com o botão "+ Adicionar Funcionário" visível
- **Dados de teste:** Nenhum — formulário deve ser enviado vazio

**Passos:**
1. Acessar http://analista-teste.seatecnologia.com.br/
2. Clicar em "+ Adicionar Funcionário"
3. Não preencher nenhum campo
4. Clicar em Salvar

| # | Campo | Resultado Esperado | Resultado Obtido | Status |
|---|-------|--------------------|-----------------|--------|
| CT-002-01 | Nome vazio | Mensagem "Preencha este campo" | Mensagem exibida corretamente | ✅ |
| CT-002-02 | CPF vazio | Mensagem "Preencha este campo" | Mensagem exibida corretamente | ✅ |
| CT-002-03 | Data vazia | Mensagem "Preencha este campo" | Mensagem exibida corretamente | ✅ |

**Resultado geral:** ✅ Passou

---

## CT-003 — Validação de CPF
- **Prioridade:** 🔴 Alta
- **Pré-condições:**
  - Estar na tela de cadastro de funcionário
  - Campo Nome preenchido com "João Teste"
- **Dados de teste:**

| Cenário | CPF usado |
|---------|-----------|
| CPF inválido | 111.111.111-11 |
| CPF com todos dígitos iguais | 000.000.000-00 |
| CPF válido | 529.982.247-25 |
| CPF vazio | (em branco) |

**Passos:**
1. Acessar o formulário de cadastro
2. Preencher Nome com "João Teste"
3. Inserir cada CPF da tabela acima
4. Tentar salvar em cada cenário

| # | Cenário | CPF | Resultado Esperado | Resultado Obtido | Status |
|---|---------|-----|--------------------|-----------------|--------|
| CT-003-01 | CPF inválido | 111.111.111-11 | Mensagem "CPF inválido" | CPF aceito sem validação | ❌ |
| CT-003-02 | Todos dígitos iguais | 000.000.000-00 | Mensagem "CPF inválido" | CPF aceito sem validação | ❌ |
| CT-003-03 | CPF válido | 529.982.247-25 | Aceitar normalmente | Campo não aceita CPF completo | ❌ |
| CT-003-04 | CPF vazio | (em branco) | Mensagem "Preencha este campo" | Mensagem exibida | ✅ |
| CT-003-05 | Máscara automática | Digitar 52998224725 | Formatar para 529.982.247-25 | Sem formatação automática | ❌ |

**Resultado geral:** ❌ Falhou
**Bugs relacionados:** BUG-005, BUG-006

---

## CT-004 — Validação de Data
- **Prioridade:** 🔴 Alta
- **Pré-condições:**
  - Estar na tela de cadastro de funcionário
  - Campos Nome e CPF preenchidos
- **Dados de teste:**

| Cenário | Data usada |
|---------|-----------|
| Data inválida | 32/13/2024 |
| Data futura | 01/01/2099 |
| Data válida | 01/01/1990 |
| Data vazia | (em branco) |

| # | Cenário | Data | Resultado Esperado | Resultado Obtido | Status |
|---|---------|------|--------------------|-----------------|--------|
| CT-004-01 | Data inválida | 32/13/2024 | Bloquear entrada | Limitou para 31/12/2024 | ✅ |
| CT-004-02 | Data futura | 01/01/2099 | Aceitar ou alertar | Aceito | ✅ |
| CT-004-03 | Data válida | 01/01/1990 | Aceitar | Aceito corretamente | ✅ |
| CT-004-04 | Data vazia | (em branco) | Mensagem de erro | Mensagem exibida | ✅ |

**Resultado geral:** ✅ Passou

---

## CT-005 — Adicionar EPI e Atividades
- **Prioridade:** 🟡 Média
- **Pré-condições:**
  - Estar na tela de cadastro de funcionário
  - Campos obrigatórios preenchidos (Nome, CPF, Data, RG)
- **Dados de teste:**
  - Atividade: Ativid 01
  - EPI: Capacete de segurança
  - Número CA: 12345

**Passos:**
1. Preencher os campos obrigatórios
2. Selecionar atividade no dropdown
3. Selecionar EPI no dropdown
4. Informar número do CA
5. Clicar em "Adicionar EPI"
6. Clicar em "Adicionar outra atividade"

| # | Item | Resultado Esperado | Resultado Obtido | Status |
|---|------|--------------------|-----------------|--------|
| CT-005-01 | Checkbox "não usa EPI" | Presente e funcional | Presente e funcional | ✅ |
| CT-005-02 | Dropdown atividade | Nome completo visível | Texto truncado "Ativid 01" | ❌ |
| CT-005-03 | Dropdown EPI | Funcional | Funcional | ✅ |
| CT-005-04 | Campo número CA | Obrigatoriedade indicada | Sem indicação visual | ❌ |
| CT-005-05 | Botão "Adicionar EPI" | Funcional | Funcional | ✅ |
| CT-005-06 | Botão "Adicionar outra atividade" | Funcional | Funcional | ✅ |

**Resultado geral:** ✅ Passou parcialmente
**Bugs relacionados:** BUG-007

---

## CT-006 — Persistência de Dados
- **Prioridade:** 🔴 Alta
- **Pré-condições:**
  - Aplicação acessível
  - Nenhum cadastro anterior com os mesmos dados
- **Dados de teste:**
  - Nome: Funcionário Teste QA
  - CPF: 529.982.247-25
  - RG: 1234567
  - Data de nascimento: 01/01/1990
  - Cargo: Cargo 01
  - Atividade: Ativid 01
  - EPI: Capacete de segurança
  - Número CA: 12345

**Passos:**
1. Preencher todos os campos com os dados de teste
2. Clicar em Salvar
3. Verificar se o funcionário aparece na lista
4. Recarregar a página
5. Verificar se o funcionário ainda aparece

| # | Verificação | Esperado | Obtido | Status |
|---|-------------|----------|--------|--------|
| CT-006-01 | Funcionário aparece na lista | Sim | Sim | ✅ |
| CT-006-02 | Dados corretos no card | Nome, CPF e cargo corretos | CPF truncado no card | ❌ |
| CT-006-03 | Dados persistem após recarregar | Sim | Sim | ✅ |

**Resultado geral:** ✅ Passou parcialmente
**Bugs relacionados:** BUG-009

---

## CT-007 — Recuperação de Dados
- **Prioridade:** 🟡 Média
- **Pré-condições:**
  - Ter pelo menos um funcionário cadastrado
  - Usar os dados cadastrados no CT-006
- **Dados de teste:** Mesmos do CT-006

**Passos:**
1. Acessar a tela principal
2. Localizar o funcionário "Funcionário Teste QA" na lista
3. Verificar se as informações estão corretas e completas

| # | Verificação | Esperado | Obtido | Status |
|---|-------------|----------|--------|--------|
| CT-007-01 | Funcionário visível na lista | Sim | Sim | ✅ |
| CT-007-02 | Nome correto | Funcionário Teste QA | Correto | ✅ |
| CT-007-03 | CPF correto e completo | 529.982.247-25 | CPF truncado | ❌ |
| CT-007-04 | Cargo correto | Cargo 01 | Correto | ✅ |

**Resultado geral:** ✅ Passou parcialmente
**Bugs relacionados:** BUG-009

---

## CT-008 — Edição de Registro
- **Prioridade:** 🔴 Alta
- **Pré-condições:**
  - Ter pelo menos um funcionário cadastrado
  - Usar os dados cadastrados no CT-006
- **Dados de teste:**
  - Nome atualizado: Funcionário Editado QA

**Passos:**
1. Localizar funcionário na lista
2. Clicar no botão "..." no card
3. Selecionar opção "Editar"
4. Alterar o nome para "Funcionário Editado QA"
5. Salvar
6. Verificar se a alteração foi aplicada

| # | Verificação | Esperado | Obtido | Status |
|---|-------------|----------|--------|--------|
| CT-008-01 | Menu "..." abre ao clicar | Menu com opções aparece | Nenhuma ação | ❌ |
| CT-008-02 | Opção "Editar" disponível | Sim | Não testado | ❌ |
| CT-008-03 | Dados salvos após edição | Nome atualizado na lista | Não testado | ❌ |

**Resultado geral:** ❌ Falhou
**Bugs relacionados:** BUG-008

---

## CT-009 — Exclusão de Registro
- **Prioridade:** 🔴 Alta
- **Pré-condições:**
  - Ter pelo menos um funcionário cadastrado
  - Usar os dados cadastrados no CT-006
- **Dados de teste:** Nenhum adicional

**Passos:**
1. Localizar funcionário na lista
2. Clicar no botão "..." no card
3. Selecionar opção "Excluir"
4. Confirmar exclusão
5. Verificar se o registro foi removido

| # | Verificação | Esperado | Obtido | Status |
|---|-------------|----------|--------|--------|
| CT-009-01 | Menu "..." abre ao clicar | Menu com opções aparece | Nenhuma ação | ❌ |
| CT-009-02 | Opção "Excluir" disponível | Sim | Não testado | ❌ |
| CT-009-03 | Registro removido da lista | Sim | Não testado | ❌ |
| CT-009-04 | Mensagem de confirmação | "Deseja excluir?" | Não testado | ❌ |

**Resultado geral:** ❌ Falhou
**Bugs relacionados:** BUG-008

---

## CT-010 — Navegação entre Menus e Links
- **Prioridade:** 🔴 Alta
- **Pré-condições:**
  - Estar na tela principal da aplicação
  - Nenhum modal ou popup aberto
- **Dados de teste:** Nenhum

**Passos:**
1. Clicar em cada ícone do menu lateral
2. Verificar se redireciona para "Em breve"
3. Clicar no botão "Próximo passo"
4. Verificar se avança para próxima etapa

| # | Item | Resultado Esperado | Resultado Obtido | Status |
|---|------|--------------------|-----------------|--------|
| CT-010-01 | Ícone menu 1 | Tela "Em breve" | Nenhuma ação | ❌ |
| CT-010-02 | Ícone menu 2 | Tela "Em breve" | Nenhuma ação | ❌ |
| CT-010-03 | Ícone menu 3 | Tela "Em breve" | Nenhuma ação | ❌ |
| CT-010-04 | Ícone menu 4 | Tela "Em breve" | Nenhuma ação | ❌ |
| CT-010-05 | Ícone menu 5 | Tela "Em breve" | Nenhuma ação | ❌ |
| CT-010-06 | Botão "Próximo passo" | Próxima etapa | Nenhuma ação | ❌ |

**Resultado geral:** ❌ Falhou
**Bugs relacionados:** BUG-010, BUG-011

---

## CT-011 — Compatibilidade com Navegadores
- **Prioridade:** 🟡 Média
- **Pré-condições:**
  - Ter Chrome, Edge e Firefox instalados
  - Conexão com internet estável
- **Dados de teste:** Nenhum

| # | Navegador | Versão | Resultado Esperado | Resultado Obtido | Status |
|---|-----------|--------|--------------------|-----------------|--------|
| CT-011-01 | Google Chrome | 134+ | Funcionar corretamente | Funciona | ✅ |
| CT-011-02 | Microsoft Edge | 134+ | Funcionar corretamente | Funciona | ✅ |
| CT-011-03 | Mozilla Firefox | 136+ | Funcionar corretamente | Não testado | ⏳ |

**Resultado geral:** ✅ Passou parcialmente

---

## 📊 Resumo Final

| Status | Quantidade |
|--------|------------|
| ✅ Passou | 6 |
| ❌ Falhou | 5 |
| ⏳ Pendente | 0 |
| **Total** | **11** |

## 📊 Distribuição por Prioridade

| Prioridade | Total | Passou | Falhou |
|------------|-------|--------|--------|
| 🔴 Alta | 7 | 3 | 4 |
| 🟡 Média | 4 | 3 | 1 |
| **Total** | **11** | **6** | **5** |
