# Plano de Testes — SEA Tecnologia

## 1. Objetivo
Avaliar a qualidade da aplicação web disponível em
http://analista-teste.seatecnologia.com.br/ verificando
conformidade com o protótipo, validações de formulário,
persistência de dados e compatibilidade com navegadores.

## 2. Escopo

### O que será testado:
- Conformidade visual com o protótipo (Figma)
- Validações do formulário (CPF, data, campos obrigatórios)
- Funcionalidade de adicionar EPI e atividades
- Persistência de dados (salvar funcionário)
- Recuperação de dados (buscar funcionário)
- Edição e exclusão de registros
- Navegação entre menus e links
- Compatibilidade com navegadores

### O que não será testado:
- Back-end e banco de dados diretamente
- Performance e carga
- Segurança avançada (pentest)

## 3. Tipos de Teste
| Tipo | Descrição |
|------|-----------|
| Teste Manual | Execução humana seguindo casos de teste |
| Teste Automatizado | Scripts em Cypress para funcionalidades críticas |
| Teste Visual | Comparação com protótipo no Figma |
| Teste de Compatibilidade | Verificação em diferentes navegadores |

## 4. Ferramentas Utilizadas
| Ferramenta | Finalidade |
|------------|-----------|
| Cypress | Automação de testes |
| Figma | Referência de protótipo |
| Chrome DevTools | Inspeção de elementos |
| Google Chrome | Navegador principal |
| Mozilla Firefox | Teste de compatibilidade |
| Microsoft Edge | Teste de compatibilidade |
| GitHub | Versionamento e entrega |

## 5. Critérios de Entrada
- Aplicação disponível e acessível via navegador
- Protótipo disponível no Figma
- Ambiente de testes configurado

## 6. Critérios de Saída
- Todos os casos de teste executados
- Bugs documentados com evidências
- Relatório final elaborado

## 7. Cronograma
| Etapa | Prazo |
|-------|-------|
| Compreensão dos requisitos | Dia 1 |
| Planejamento dos testes | Dia 1-2 |
| Execução dos testes manuais | Dia 2-4 |
| Execução dos testes automatizados | Dia 4-5 |
| Reporte de bugs e melhorias | Dia 5-6 |
| Relatório final | Dia 7 |

## 8. Riscos
| Risco | Impacto | Mitigação |
|-------|---------|-----------|
| Aplicação fora do ar | Alto | Registrar evidência e tentar novamente |
| Protótipo inacessível | Médio | Usar prints salvos como referência |
| Funcionalidade incompleta | Médio | Documentar como bug e seguir os testes |

## 9. Ambiente de Testes
- **Sistema Operacional:** Windows 10/11
- **Navegadores:** Chrome, Firefox, Edge
- **Resolução:** 1920x1080
- **URL da aplicação:** http://analista-teste.seatecnologia.com.br/
- **URL do protótipo:** https://tinyurl.com/yl58hs4m
