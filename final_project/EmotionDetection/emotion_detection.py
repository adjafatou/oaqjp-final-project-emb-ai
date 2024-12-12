import requests

def emotion_detector(text_to_analyze):
    # Vérification de l'entrée vide
    if not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
            'error': "Texte invalide ! Veuillez réessayer !"
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    input_data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        response = requests.post(url, headers=headers, json=input_data)
        print("Response Status Code:", response.status_code)
        print("Response Content:", response.text)

        if response.status_code == 200:
            response_dict = response.json()

            # Accède aux prédictions d'émotion
            emotion_predictions = response_dict.get('emotionPredictions', [])

            if emotion_predictions:
                emotions = emotion_predictions[0].get('emotion', {})
                
                # Crée un dictionnaire avec les scores des émotions
                emotion_scores = {emotion: emotions.get(emotion, 0) for emotion in ['anger', 'disgust', 'fear', 'joy', 'sadness']}
                
                # Trouve l'émotion dominante
                dominant_emotion = max(emotion_scores, key=emotion_scores.get)

                # Retourne les scores d'émotion avec l'émotion dominante
                return {
                    'anger': emotion_scores['anger'],
                    'disgust': emotion_scores['disgust'],
                    'fear': emotion_scores['fear'],
                    'joy': emotion_scores['joy'],
                    'sadness': emotion_scores['sadness'],
                    'dominant_emotion': dominant_emotion
                }
            else:
                return {"error": "No emotion predictions found"}
        
        elif response.status_code == 400:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None,
                'error': "Texte invalide ! Veuillez réessayer !"
            }
        else:
            return f"Error: {response.status_code}, {response.text}"
    
    except Exception as e:
        return f"An error occurred: {str(e)}"
