# Text to Speech con ElevenLabs y AWS S3

Este proyecto convierte texto en audio utilizando la API de ElevenLabs y sube los archivos generados a un bucket de AWS S3. 

## 🚀 Características:
- Convierte múltiples textos a formato de audio `.mp3`
- Utiliza **ElevenLabs** para la conversión de texto a voz
- Sube automáticamente los audios a un **bucket de AWS S3**

## 📌 Requisitos
- Python 3.x
- Cuenta en ElevenLabs con una API Key
- AWS CLI configurado con credenciales

## 📥 Instalación
1. Clona este repositorio:
   ```sh
   git clone https://github.com/charleetrion/Text-To-Speech-s3.git

2. Instala las dependencias:
   pip install requests boto3

3. Configura tus credenciales en el script. Configure AWS
4. Uso
   python text_to_speech.py

