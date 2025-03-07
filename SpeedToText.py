from flask import Flask,request,jsonify
from vosk import Model,KaldiRecognizer
import wave
import json
import os
import re
app=Flask(__name__)
model_path="vosk-model-small-cn-0.22"
if not os.path.exists(model_path):
    print(f"f模型路径{model_path}不存在")
    exit(1)
model=Model(model_path)
def speech_to_text(audio_file):
    wf=wave.open(audio_file,"rb")
    recognizer=KaldiRecognizer(model,wf.getframerate())
    result=""
    while True:
        data=wf.readframes(4000)
        if len(data)==0:
            break
        if recognizer.AcceptWaveform(data):
            result=json.loads(recognizer.Result())["text"]
    return result
@app.route("/process_audio",methods=["POST"])
def process_audio():
    audio_file="received_audio.wav"
    with open(audio_file,'wb') as f:
        f.write(request.data)
    result=speech_to_text(audio_file)
    result=re.sub(r"\s+","",result)
    print("识别结果：",result)
    return jsonify({"result":result})
if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)