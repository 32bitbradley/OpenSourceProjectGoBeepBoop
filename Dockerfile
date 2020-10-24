FROM python:3.8.5-alpine3.12
LABEL maintainer="32bitbradley@gmail.com"
LABEL version="1.1"

EXPOSE 5000/tcp

# Add content 
ADD . /var/OpenSourceProjectGoBeepBoop

# Install required packages, pip requirements and then cleanup
RUN apk add --no-cache gcc musl-dev libxslt-dev python3-dev=3.8.5-r0 --virtual .build-deps \
&& pip install --no-cache-dir --upgrade pip \
&& pip install --no-cache-dir -r /var/OpenSourceProjectGoBeepBoop/requirements.txt \
&& apk del .build-deps

WORKDIR /var/OpenSourceProjectGoBeepBoop/

# Run application
CMD ["python", "/var/OpenSourceProjectGoBeepBoop/ospgbb.py"]
