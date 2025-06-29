import requests
import boto3  # Librería para AWS S3
import os

# Configuracion
API_KEY = "00000" #Reemplazala con tu API Key de ElevenLabs
VOICE_ID= "21m00Tcm4TlvDq8ikWAM"   # ID de la voz a utilizar (puedes cambiar la voz)
BUCKET_NAME = "eleven-audio-2025"  # Nombre del bucket de S3 donde se subirán los audios, Debes crear un Bucket S3

# lista de textos a convertir en audio (PUEDES CAMBIAR LOS TEXTS POR CUALQUIER COSA !!)
TEXTS = [
    "Hola, este es el primer audio.",
    "Este es el segundo mensaje de prueba.",
    "Y finalmente, este es el tercer audio."
]

# Configura el cliente de AWS S3
s3 = boto3.client("s3")


def text_to_speech(text, file_name):
    """
    Función que envía una solicitud a la API de ElevenLabs para convertir un texto en audio.
    Guarda el audio generado en un archivo local.
    """
    print(f"🎤 Iniciando solicitudes a ElevenLabs...")

    # URL de la API de ElevenLabs
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "Accept": "audio/mpeg",
         "Content-Type": "application/json",
        "xi-api-key": API_KEY 
    }
    data = {
        "text": text,
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

     # Enviar la solicitud
    print(f"🎤 Generando audios: {file_name}...")
    response = requests.post(url, json=data, headers=headers)
    print(f"🔹 Código de respuesta: {response.status_code}")

     # Si la solicitud fue exitosa, guardar el archivo de audio
    if response.status_code == 200 and response.content:
        with open(file_name, "wb") as f:
            f.write(response.content)
        print("✅ Audio guardado: {file_name}")
        return file_name
    else:
        print("❌ Error en la generación de {file_name}:{response.text}")
        return None
    
# Función que sube un archivo de audio a un bucket de AWS S3 y lo elimina localmente después.
def upload_to_s3(file_name):
    if not os.path.exists(file_name):  # Verificar que el archivo existe antes de subirlo
        print(f"⚠️ Archivo no encontrado: {file_name}, no se subirá a S3.")
        return

    try:
        # Subir el archivo a S3
        s3.upload_file(file_name, BUCKET_NAME, file_name)
        print(f"🚀 Archivo subido a S3: {file_name}")

        # Eliminar el archivo local después de subirlo
        os.remove(file_name) 
        print(f"🗑️ Archivo local eliminado: {file_name}")
    except Exception as e:
        print(f"❌ Error al subir {file_name} a S3:", e)

# 🔹 Generar y subir cada archivo
for i, text in enumerate(TEXTS):
    file_name = f"audio_{i+1}.mp3"
    audio_file = text_to_speech(text, file_name)

    # Subir el archivo generado a S3
    if audio_file:
        upload_to_s3(audio_file)
        
    
