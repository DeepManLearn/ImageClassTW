import mimetypes
import os
from io import BytesIO
from typing import List, Dict, Union, ByteString, Any
from urllib.parse import urlparse

from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

from fastai.vision import *

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))

model = load_learner('.')

def load_image(raw_bytes: ByteString) -> Image:
    img = open_image(BytesIO(raw_bytes))
    return img

@app.route("/")
def hello():
    return "Welcome to Bird Image Classifier!\nPlease, send POST request to /whatsapp."


@app.route("/whatsapp", methods=["GET", "POST"])
def reply_whatsapp():
    response = MessagingResponse()

    num_media = request.values.get("NumMedia")

    if (not num_media) or (num_media == '0'):
        msg = response.message("Please, send us a Bird image!")
    else:
        for idx in range(int(num_media)):
           media_url = request.values.get(f'MediaUrl{idx}')
           mime_type = request.values.get(f'MediaContentType{idx}')
#          print("mime_type :"+mime_type)
           req = requests.get(media_url)

           img = load_image(req.content)
           pred_class, pred_idx, outputs = model.predict(img)

           msg = response.message("Thanks for the "+ str(pred_class)+" image!")

#   print("num_media:" +str(num_media))

    return str(response)

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0',port=port)