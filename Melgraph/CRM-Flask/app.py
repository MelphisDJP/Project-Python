from flask import Flask, render_template
from twilio.rest import Client
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)

# Inicializar el cliente de Twilio con tus credenciales
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_WHATSAPP_FROM = 'whatsapp:+14155238886'  # Número de Twilio (sandbox)

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def get_recent_contact():
    # Obtener los 10 ultimos mensajes (Recibido y Enviado)
    all_messages = client.messages.list(limit=10)
    
    # Filtrar por mensajes de WhatsApp
    whatsapp_messages = [msg for msg in all_messages.from_.startswith('whatsapp:')]
    
    # Formatear los mensajes de WhatsApp
    formatted_messages = [{
        'from': msg.from_,
        'body': msg.body[:100],
        'date_send': msg.date_sent
    } for msg in whatsapp_messages]
    
    return formatted_messages

@app.route('/')
def home():
    print("Renderizando la página de inicio")
    try:
        # Obtener los mensajes recientes
        unique_messages = get_recent_contact()

        # Renderizamos la página con los mensajes únicos
        return render_template('home.html', unique_messages=unique_messages)

    except Exception as e:
        print(f"Error al obtener mensajes: {e}")
        return render_template('home.html', unique_messages=[], error="Error al obtener mensajes.")