FROM python:3.8

COPY tests/bad_client_certs /etc/certs/bad_client_certs
COPY tests/good_client_certs /etc/certs/good_client_certs
COPY tests/ca_certs /etc/certs/ca_certs
COPY tests/server_certs /etc/certs/server_certs

RUN pip install requests 

COPY tests/test.py .

ENTRYPOINT [ "python", "-m", "unittest", "discover" ]