import requests  # Importar la biblioteca para realizar solicitudes HTTP


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

    # Devolver la respuesta de la API
    return response.text