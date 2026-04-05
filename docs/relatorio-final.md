# Relatório Final de Testes — SEA Tecnologia

## 1. Informações Gerais
| Campo | Detalhe |
|-------|---------|
| **Candidato** | Alyson |
| **Vaga** | Analista de Teste |
| **Aplicação testada** | http://analista-teste.seatecnologia.com.br/ |
| **Protótipo de referência** | https://tinyurl.com/yl58hs4m |
| **Data de início** | 05/04/2026 |
| **Data de entrega** | 12/04/2026 |
| **Navegadores testados** | Google Chrome, Microsoft Edge |

---

## 2. Resumo Executivo

A aplicação web da SEA Tecnologia foi submetida a um processo completo de
testes manuais e automatizados. Foram executados 11 casos de teste cobrindo
conformidade visual, validações de formulário, persistência de dados,
navegação e compatibilidade com navegadores.

Ao todo foram identificados **11 bugs**, sendo **8 de severidade Alta**,
**3 de severidade Média** e **0 de severidade Baixa**. Os principais
problemas encontrados estão relacionados à navegação da aplicação, validação
de CPF e divergências visuais em relação ao protótipo.

---

## 3. Resultado dos Casos de Teste

| Caso de Teste | Descrição | Resultado |
|---------------|-----------|-----------|
| CT-001 | Conformidade visual com protótipo | ❌ Falhou |
| CT-002 | Validação de campos obrigatórios | ✅ Passou |
| CT-003 | Validação de CPF inválido | ❌ Falhou |
| CT-004 | Validação de data inválida | ✅ Passou |
| CT-005 | Adicionar EPI e atividades | ✅ Passou |
| CT-006 | Persistência de dados | ✅ Passou |
| CT-007 | Recuperação de dados | ✅ Passou |
| CT-008 | Edição de registro | ❌ Falhou |
| CT-009 | Exclusão de registro | ❌ Falhou |
| CT-010 | Navegação entre menus e links | ❌ Falhou |
| CT-011 | Compatibilidade com navegadores | ✅ Passou |

**Total:** 6 Passou ✅ | 5 Falhou ❌

---

## 4. Resumo dos Bugs Encontrados

| # | Descrição | Severidade |
|---|-----------|------------|
| BUG-001 | Fonte tipográfica divergente do protótipo | 🟡 Média |
| BUG-002 | Cor azul divergente do protótipo | 🟡 Média |
| BUG-003 | Botões de navegação ausentes no formulário | 🔴 Alta |
| BUG-004 | Stepper com labels e estados incorretos | 🔴 Alta |
| BUG-005 | CPF inválido aceito sem validação | 🔴 Alta |
| BUG-006 | Campo CPF sem máscara de formatação | 🟡 Média |
| BUG-007 | Label truncada no dropdown de atividade | 🟡 Média |
| BUG-008 | Menu de opções (...) não funciona | 🔴 Alta |
| BUG-009 | Card do funcionário com informações incompletas | 🔴 Alta |
| BUG-010 | Menu lateral não funciona | 🔴 Alta |
| BUG-011 | Botão "Próximo passo" não funciona | 🔴 Alta |

**Total:** 11 bugs | 🔴 Alta: 8 | 🟡 Média: 3

---

## 5. Testes Automatizados

Foram implementados 4 testes automatizados utilizando **Selenium WebDriver**
com **Python**, cobrindo as funcionalidades mais críticas da aplicação:

| Teste Automatizado | Resultado |
|--------------------|-----------|
| Validação de campos obrigatórios | ✅ Passou |
| Validação de CPF inválido | ✅ BUG-005 Confirmado |
| Persistência de dados | ✅ Passou |
| Navegação do menu lateral | ✅ BUG-010 Confirmado |

---

## 6. Análise Geral de Qualidade

### Pontos Positivos ✅
- Validação de campos obrigatórios funcionando corretamente
- Campo de data bloqueia datas inválidas
- Seção de EPI e atividades presente e funcional
- Dados dos funcionários são salvos corretamente
- Aplicação compatível com Chrome e Edge

### Pontos Negativos ❌
- Navegação completamente comprometida (menu lateral e botão próximo passo)
- Impossível editar ou excluir funcionários
- CPF não possui validação nem máscara
- Stepper diverge completamente do protótipo
- Divergências visuais em relação ao protótipo (fonte e cores)

---

## 7. Sugestões de Melhorias

1. **Validação de CPF:** Implementar validação completa do CPF, incluindo
   dígitos verificadores e máscara automática `000.000.000-00`

2. **Navegação:** Corrigir o menu lateral e o botão "Próximo passo" para
   que funcionem corretamente e levem às telas esperadas

3. **Stepper:** Corrigir os labels para exibir nomes únicos e distintos,
   com capitalização normal e apenas o item atual ativo

4. **Menu de opções (...):** Implementar o menu de ações para permitir
   edição e exclusão de funcionários

5. **Design:** Ajustar fonte e paleta de cores para ficarem em conformidade
   com o protótipo no Figma

6. **Card do funcionário:** Exibir todas as informações completas no card
   da lista de funcionários

---

## 8. Conclusão

A aplicação apresenta uma base funcional com o cadastro e listagem de
funcionários operando corretamente. Porém, diversas funcionalidades críticas
ainda precisam ser implementadas ou corrigidas antes de uma entrega em
produção, especialmente a navegação entre telas, a edição/exclusão de
registros e a validação do CPF.

Recomenda-se a correção prioritária dos bugs de severidade Alta antes de
avançar para novas funcionalidades.

---

## 9. Evidências
Todos os prints e evidências estão disponíveis na pasta
`/evidencias/prints/` deste repositório.

O código dos testes automatizados está disponível em `/automacao/test_selenium.py`.

