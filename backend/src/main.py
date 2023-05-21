#!/usr/bin/env python
from flask import Flask, request
import os
import numpy as np
import cv2
import io
import base64
from ocr.ocr import ocr as ocr_tesseract
from chat_gpt.chat_gpt import chatGPT

app = Flask(__name__)


@app.route('/summarize', methods=["POST"])
def summarize():
    post_imgs = request.json["post_imgs"]
    option = request.json["option"]
    txts = ""
    for i, img_base64 in enumerate(post_imgs):
        # Base64データをバイナリに変換
        img_binary = io.BytesIO(base64.b64decode(img_base64))
        # ライブラリを使って画像を読み込み
        npimg = np.frombuffer(img_binary.getvalue(), dtype=np.uint8)
        img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
        
        txt = ocr_tesseract(img)
        txts += txt
    
    txts = chatGPT(txts, option)

    return {"result": txts}

@app.route('/translate', methods=["POST"])
def translate():
    img_base64 = request.json["post_img"]
    option = request.json["option"]

    img_binary = io.BytesIO(base64.b64decode(img_base64))

    npimg = np.frombuffer(img_binary.getvalue(), dtype=np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    txt = ocr_tesseract(img)
    txt = chatGPT(txt, option)

    return {"result": txt}


@app.route('/')
def home():
    return {"root": "home"}

if __name__ == "__main__":
    # app.run(debug=True, host="0.0.0.0", port=5000)
    # print(ocr_tesseract("image/sample.jpg"))
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
