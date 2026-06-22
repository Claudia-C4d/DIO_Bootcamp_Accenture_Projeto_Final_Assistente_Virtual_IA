
import pandas as pd
import json
import requests
import streamlit as st
import os

print("Sucesso! Todas as bibliotecas foram carregadas.")

# CARREGAMENTO DOS ARQUIVOS 

produtos = json.load(open("produtos_financeiros.json"))

clientes = json.load(open("perfil_investidor.json"))

dados_transacoes = pd.read_csv("transacoes.csv")

atendimentos = pd.read_csv("historico_atendimento.csv")
    
print("Sucesso total no carregamento de dados!")


# CONTEXTO DE DADOS DO CLIENTE

contexto = f""" 

[PRODUTOS DISPONÍVEIS]: 
{json.dumps(produtos, indent=2, ensure_ascii=False)}

[CLIENTE]: {clientes["nome"]}, {clientes["idade"]} anos, perfil {clientes["perfil_investidor"]}

[OBJETIVO]: {clientes["objetivo_principal"]}

[PATRIMÔNIO]: R$ {clientes["patrimonio_total"]} | [RESERVA]: R$ {clientes["reserva_emergencia_atual"]}

[TRANSAÇÕES RECENTES]:
{dados_transacoes.to_string(index=False)}

[ATENDIMENTOS ANTERIORES]: 
{atendimentos.to_string(index=False)}

"""

# SYSTEM PROMPT

SYSTEM_PROMPT = """ Você é a Nila, uma consultora financeira inteligente, amigável e focada em finanças pessoais.

OBJETIVO: Seu objetivo é guiar o usuário com leveza, transmitindo máxima confiança e segurança, ajudando-o a tomar decisões inteligentes com relação à seu planejamento financeiro, utilizando os dados do cliente como base para exemplos práticos. 

Siga estritamente estas diretrizes operacionais em todas as respostas:

1. ESCOPO E BLINDAGEM DE CONTEXTO:
- Atue exclusivamente com foco em finanças pessoais.
- JAMAIS responda a perguntas fora do contexto financeiro. Se for questionada sobre outros assuntos, recuse educadamente reforçando o seu papel estrito como consultora financeira.
- Se o usuário perguntar algo específico que você não saiba ou cujos dados fornecidos não cubram, admita abertamente que não possui essa informação.

2. CONDUTA DE INVESTIMENTOS (REGULATÓRIO):
- NUNCA induza ou recomende que o cliente invista em um ativo específico.
- Apenas explique de forma neutra e educativa como funciona cada tipo de investimento e suas particularidades.

3. PERSONALIZAÇÃO E USO DE DADOS:
- Utilize apenas os dados financeiros fornecidos no histórico para gerar soluções e análises personalizadas para a realidade do cliente.

4. FORMATO E LEVEZA DA RESPOSTA:
- Responda sempre de forma direta, pragmática e centrada no objetivo do usuário.
- Seja concisa: organize o texto em parágrafos breves (máximo de 2 a 3 linhas por parágrafo) e use listas se necessário.
- Mantenha a conversa leve e fluida, sem parecer um robô rígido.

5. REGRA OBRIGATÓRIA: Ao final de cada resposta, você deve, obrigatoriamente, sugerir uma nova pergunta relacionada ao assunto ou o próximo passo lógico para o usuário continuar a conversa, baseando-se no que foi respondido."

6. ENCERRAMENTO OBRIGATÓRIO:
- Sempre termine a sua resposta perguntando ativamente ao cliente se a informação transmitida foi clara, se ele compreendeu tudo ou se tem dúvidas sobre algum ponto específico.
"""


# CHAMAR A EXECUÇÃO DA OLLAMA:

OLLAMA_URL = "http://localhost:11434/api/generate"

Modelo = "llama3.2"

def perguntar(msg):
    
    prompt = f"""{SYSTEM_PROMPT}
    Contexto do cliente: {contexto}
    Pergunta: {msg}"""
    
    # Dados para enviar à Ollama
    dados_requisicao = {
        "model": Modelo,
        "prompt": prompt,
        "stream": False
    }
    
    try:
        # Chamada HTTP para o servidor local do Ollama
        r = requests.post(OLLAMA_URL, json=dados_requisicao)
        
        # Extrai a resposta textual em formato JSON e a retorna
        return r.json()["response"]
        
    except Exception as e:
        return f"Erro de conexão com o Ollama via API: {e}"
    

# Implementação do Streamlit

st.markdown(
    "<h1 style='color:#7A28FF ;'>Nila - Sua Consultora Virtual 🤖</h1>", 
    unsafe_allow_html=True
)

# Título e subtítulo  (com cor e tamanho personalizados + linha de separação)
st.markdown(
    "<h3 style='color: #0066CC; font-weight: normal; margin-top: 5px;'> Especialista em finanças pessoais</h3>", 
    unsafe_allow_html=True
)

st.markdown("---")

# Caixa de diálogo da interface "Nila"
if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    
    # Exibe de mensagem do cliente
    
    st.chat_message("user").write(pergunta)
    
    
    with st.spinner("Nila está pensando..."):
        
        resposta_nila = perguntar(pergunta)
        
        # Resposta final da "Nila"
        st.chat_message("assistant").write(resposta_nila)


