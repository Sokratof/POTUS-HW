#FOR START
#docker run -p 8000:8000 -it app

FROM python:3.9-buster


SHELL ["/bin/bash", "-c"]


#set enviroments variable
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFEFED 1


WORKDIR /app


RUN pip install --upgrade pip
RUN apt-get update \
    && apt-get install -y apt-utils \
    && apt-get -y install nano \
    && apt-get clean


COPY requirements.txt ./
RUN pip install --no-warn-script-location --no-cache-dir -r requirements.txt

COPY main.py ./

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

