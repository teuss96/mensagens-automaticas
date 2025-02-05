import pywhatkit as kit
import time

def enviar_mensagem(numero, mensagem):
    try:
        kit.sendwhatmsg(numero, mensagem, 15, 0)  # Hora: 15, minuto: 0 (exemplo)
        print(f"Mensagem enviada para {numero}!")
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")

def mensagem_pizzaria():
    mensagem = """
    🍕 Bem-vindo à Pizzaria Delícia! 🍕
    
    Nosso cardápio:
    
    1. Pizza Margherita - R$ 35,00
    2. Pizza Calabresa - R$ 40,00
    3. Pizza Quatro Queijos - R$ 45,00
    4. Pizza Frango com Catupiry - R$ 42,00
    
    Promoções do dia:
    - 2 pizzas grandes por R$ 70,00
    - Pizza + refrigerante por R$ 50,00

    Faça seu pedido pelo WhatsApp ou pelo nosso site!
    """
    return mensagem

# Exemplo de uso
numero_cliente = "+55XX999999999"  # Substitua com o número de telefone do cliente (formato internacional)
mensagem = mensagem_pizzaria()  # Mensagem com o cardápio
enviar_mensagem(numero_cliente, mensagem)
