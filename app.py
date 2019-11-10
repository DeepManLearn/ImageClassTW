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


model = load_learner('.')

def load_image(raw_bytes: ByteString) -> Image:
    img = open_image(BytesIO(raw_bytes))
    return img
	

@app.route("/whatsapp", methods=["GET", "POST"])
def reply_whatsapp():

    num_media = int(request.values.get("NumMedia"))
    media_files = []
    for idx in range(num_media):
        media_url = request.values.get(f'MediaUrl{idx}')
        mime_type = request.values.get(f'MediaContentType{idx}')
        media_files.append((media_url, mime_type))

        req = requests.get(media_url)
        file_extension = mimetypes.guess_extension(mime_type)
        media_sid = os.path.basename(urlparse(media_url).path)

 #       with open(f"app_data/{media_sid}{file_extension}", 'wb') as f:
 #           f.write(req.content)
        img = load_image(req.content)
        pred_class, pred_idx, outputs = model.predict(img)
	
    response = MessagingResponse()

    if not num_media:
        msg = response.message("Please, send us a Bird image!")
    else:
        msg = response.message("Thanks for the "+ str(pred_class)+" image!")

    return str(response)
