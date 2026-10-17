import requests  # Importar la biblioteca para realizar solicitudes HTTP
import json
import requests

def emotion_detector(text_to_analyse):
    # URL del servicio de análisis de emociones
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    # Crear el cuerpo JSON de la solicitud
    myobj = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    # Establecer los encabezados requeridos por la API
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Enviar la solicitud POST
    response = requests.post(url, json=myobj, headers=headers)
    formatted_response = response.json()
    #formatted_response = json.loads(response.text)

    # Devolver la respuesta de la API
    #return response.text
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    dominant_emotion = max(emotions, key=emotions.get)

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,mv ./sentiment_analysis.py ./SentimentAnalysis
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }