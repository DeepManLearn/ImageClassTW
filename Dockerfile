FROM python:3.7.1-slim-stretch

RUN apt update && \
    apt install -y python3-dev gcc

WORKDIR app 
# Install pytorch and fastai
RUN pip install Flask==1.0.2
RUN pip install twilio==6.33.0
RUN pip install torch==1.2.0+cpu torchvision==0.4.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
RUN pip install fastai

ADD app.py .
ADD export.pkl .

#ADD requirements.txt .

#RUN pip install -r requirements.txt
#pip install --no-cache-dir -r
#ADD models models
#ADD src src

# Run it once to trigger resnet download
#RUN python app.py prepare

#EXPOSE 5000

# Start the server
CMD ["python", "app.py"]