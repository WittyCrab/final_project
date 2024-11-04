import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }

    returned_value = requests.post(url,headers=header, json=input_json)

      formatted_response = json.loads(response.text)

    if response.status_code == 200:
        emotion = formatted_response['emotionPredictions'][0]['emotion']
        max_emotion = max(emotion.items(), key=lambda x: x[1])
        return max_emotion[0]
    else:
        return None
