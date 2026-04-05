# Bugs Reportados — SEA Tecnologia

## Legenda de Severidade
| Severidade | Significado |
|------------|-------------|
| 🔴 Alta | Impacta funcionalidade principal |
| 🟡 Média | Impacta experiência do usuário |
| 🟢 Baixa | Impacto visual ou cosmético |

---

## BUG-001 — Fonte tipográfica divergente do protótipo
- **Tipo:** Design
- **Severidade:** 🟡 Média
- **Onde:** Toda a aplicação
- **Passos para reproduzir:**
  1. Acessar a aplicação
  2. Comparar a fonte com o protótipo no Figma
- **Resultado esperado:** Fonte grossa conforme protótipo
- **Resultado obtido:** Fonte fina diferente do protótipo
- **Evidência:** `evidencias/prints/BUG001-fonte.png`

---

## BUG-002 — Cor azul divergente do protótipo
- **Tipo:** Design
- **Severidade:** 🟡 Média
- **Onde:** Cabeçalho, botões e elementos da aplicação
- **Passos para reproduzir:**
  1. Acessar a aplicação
  2. Comparar as cores com o protótipo no Figma
- **Resultado esperado:** Azul acinzentado conforme protótipo
- **Resultado obtido:** Azul claro diferente do protótipo
- **Evidência:** `evidencias/prints/BUG002-cores.png`

---

## BUG-003 — Botões de navegação ausentes no formulário
- **Tipo:** Funcionalidade
- **Severidade:** 🔴 Alta
- **Onde:** Formulário de cadastro de funcionário
- **Passos para reproduzir:**
  1. Clicar em "+ Adicionar Funcionário"
  2. Verificar se há botões de Próximo/Passo
- **Resultado esperado:** Botões de navegação entre etapas do formulário
- **Resultado obtido:** Botões ausentes, sem como navegar entre etapas
- **Evidência:** `evidencias/prints/BUG003-botoes-ausentes.png`

---

## BUG-004 — Stepper com labels e estados incorretos
- **Tipo:** Design e Funcionalidade
- **Severidade:** 🔴 Alta
- **Onde:** Barra de progresso (stepper) no topo da aplicação
- **Passos para reproduzir:**
  1. Acessar a aplicação
  2. Observar o stepper no topo
  3. Comparar com o protótipo
- **Resultado esperado:**
  - Labels únicos: Item 1, Item 2... Item 9
  - Capitalização normal
  - Apenas 1º ícone ativo (azul), demais cinza
- **Resultado obtido:**
  - Todos com label "ITEM 1" em maiúsculo
  - Todos os ícones ativos (azul igual)
- **Evidência:** `evidencias/prints/BUG004-stepper.png`

---

## BUG-005 — CPF inválido aceito sem validação
- **Tipo:** Validação
- **Severidade:** 🔴 Alta
- **Onde:** Campo CPF do formulário de cadastro
- **Passos para reproduzir:**
  1. Acessar o formulário de cadastro
  2. Digitar CPF inválido: `111.111.111-11`
  3. Tentar salvar
- **Resultado esperado:** Mensagem de erro "CPF inválido"
- **Resultado obtido:** Sistema aceitou o CPF sem validar
- **Evidência:** `evidencias/prints/BUG005-cpf-invalido.png`

---

## BUG-006 — Campo CPF sem máscara de formatação
- **Tipo:** Usabilidade
- **Severidade:** 🟡 Média
- **Onde:** Campo CPF do formulário de cadastro
- **Passos para reproduzir:**
  1. Acessar o formulário de cadastro
  2. Digitar números no campo CPF
- **Resultado esperado:** Formatação automática `000.000.000-00`
- **Resultado obtido:** Números sem máscara `11111111111`
- **Evidência:** `evidencias/prints/BUG006-cpf-mascara.png`

---

## BUG-007 — Label truncada no dropdown de atividade
- **Tipo:** Usabilidade
- **Severidade:** 🟡 Média
- **Onde:** Dropdown "Selecione a atividade" na seção de EPI
- **Passos para reproduzir:**
  1. Acessar o formulário de cadastro
  2. Observar o dropdown de atividade
- **Resultado esperado:** Nome completo da atividade
- **Resultado obtido:** Texto cortado "Ativid 01"
- **Evidência:** `evidencias/prints/BUG007-label-truncada.png`

---

## BUG-008 — Menu de opções (...) não funciona
- **Tipo:** Funcionalidade
- **Severidade:** 🔴 Alta
- **Onde:** Botão `...` no card do funcionário
- **Passos para reproduzir:**
  1. Ter um funcionário cadastrado na lista
  2. Clicar no botão `...` no card do funcionário
- **Resultado esperado:** Abrir menu com opções de Editar/Excluir
- **Resultado obtido:** Nenhuma ação ao clicar
- **Impacto:** Impossível editar ou excluir funcionários
- **Evidência:** `evidencias/prints/BUG008-menu-nao-funciona.png`

---

## BUG-009 — Card do funcionário com informações incompletas
- **Tipo:** Funcionalidade
- **Severidade:** 🔴 Alta
- **Onde:** Card do funcionário na lista
- **Passos para reproduzir:**
  1. Cadastrar funcionário com todos os dados
  2. Verificar card na lista
- **Resultado esperado:** CPF completo, atividade e cargo exibidos como texto
- **Resultado obtido:** CPF truncado e ícone azul no lugar de atividade e cargo
- **Evidência:** `evidencias/prints/BUG009-card-incompleto.png`

---

## BUG-010 — Menu lateral não funciona
- **Tipo:** Navegação
- **Severidade:** 🔴 Alta
- **Onde:** Ícones do menu lateral esquerdo
- **Passos para reproduzir:**
  1. Acessar a tela principal
  2. Clicar em cada ícone do menu lateral
- **Resultado esperado:** Navegar para tela "Em breve"
- **Resultado obtido:** Nenhuma ação ao clicar
- **Evidência:** `evidencias/prints/BUG010-menu-lateral.png`

---

## BUG-011 — Botão "Próximo passo" não funciona
- **Tipo:** Navegação
- **Severidade:** 🔴 Alta
- **Onde:** Botão "Próximo passo" no rodapé da tela
- **Passos para reproduzir:**
  1. Acessar a tela principal
  2. Clicar no botão "Próximo passo"
- **Resultado esperado:** Avançar para próxima etapa
- **Resultado obtido:** Nenhuma ação ao clicar
- **Evidência:** `evidencias/prints/BUG011-proximo-passo.png`

---

## 📊 Resumo Geral

| Severidade | Quantidade |
|------------|------------|
| 🔴 Alta    | 8 |
| 🟡 Média   | 3 |
| 🟢 Baixa   | 0 |
| **Total**   | **11** |
