FROM python:3.8

COPY bad_client_certs /etc/certs/bad_client_certs
COPY good_client_certs /etc/certs/good_client_certs
COPY ca_certs /etc/certs/ca_certs
COPY server_certs /etc/certs/server_certs

RUN pip install requests 

COPY test.py .

ENTRYPOINT [ "python", "-m", "unittest", "discover" ]