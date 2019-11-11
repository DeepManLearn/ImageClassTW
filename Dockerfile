FROM python:3.7.5-slim-stretch

RUN apt update && \
    apt install -y python3-dev gcc

WORKDIR app 
# Install pytorch and fastai
#RUN pip install torch_nightly -f https://download.pytorch.org/whl/nightly/cpu/torch_nightly.html

ADD requirements.txt .
ADD app.py .
ADD export.pkl .
RUN pip install -r requirements.txt
#pip install --no-cache-dir -r
#ADD models models
#ADD src src

# Run it once to trigger resnet download
RUN python app.py prepare

#EXPOSE 5000

# Start the server
CMD ["python", "app.py", "serve"]