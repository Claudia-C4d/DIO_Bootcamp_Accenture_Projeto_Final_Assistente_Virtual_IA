# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores |
| `perfil_investidor.json` | JSON | Personalizar recomendações |
| `produtos_financeiros.json` | JSON | Sugerir produtos adequados ao perfil |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

[Formatei um dos produtos apresentados no arquivo produtos_financeiros,json, transformando-o em Fundo Imobiliário, com suas características específicas]

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

[ex: Os JSON/CSV são carregados no início da sessão e incluídos no contexto do prompt]

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

[Os dados estão na variável "contexto", e são chamados na função ao iniciar o Ollama]

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
CLIENTE:
- nome: João Silva
- idade: 32 anos
- perfil_investidor: Moderado
...

PRODUTOS DISPONÍVEIS:
- nome: Tesouro Selic
- categoria: renda_fixa
- risco: baixo
- rentabilidade: 100% da Selic
- aporte_minimo: 30.00
- indicado_para: Reserva de emergência e iniciantes
...
