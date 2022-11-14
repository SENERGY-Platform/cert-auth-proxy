<a href="https://github.com/SENERGY-Platform/cert-auth-proxy/actions/workflows/test.yml" rel="nofollow">
    <img src="https://github.com/SENERGY-Platform/cert-auth-proxy/actions/workflows/test.yml/badge.svg" alt="Tests" />
</a>

<a href="https://github.com/SENERGY-Platform/cert-auth-proxy/actions/workflows/dev.yml" rel="nofollow">
    <img src="https://github.com/SENERGY-Platform/cert-auth-proxy/actions/workflows/dev.yml/badge.svg" alt="Deployment Dev" />
</a>

<a href="https://github.com/SENERGY-Platform/cert-auth-proxy/actions/workflows/prod.yml" rel="nofollow">
    <img src="https://github.com/SENERGY-Platform/cert-auth-proxy/actions/workflows/prod.yml/badge.svg" alt="Deployment Prod" />
</a>

# CERT-AUTH-PROXY
This NGINX web server acts as a reverse proxy to authenticate requests with client certificates. Requests are then forwarded to the kong proxy to exchange a JWT user token.

## Certificates
All valid clients must have a client certificate signed by the private CA.

# Build
```
docker build -t cert-auth-proxy .
```

# Tests
You can run test by using the docker-compose.yml file in the tests directory.
```
docker compose -f tests/docker-compose.yml build
docker compose -f tests/docker-compose.yml up -d cert_auth gateway
docker compose -f tests/docker-compose.yml run test
``` 
Client and server certificates provided in the tests directory. Keep in mind that the Organization Name of CA certificate and client certificate must be different and that the Common Name or Subject Alternativ Name field of the server certificate must match the hostname, e.g. `localhost` or the container name.

# Deployment
This service needs a connection to the kong proxy which is set by `KONG_PROXY_HOST` and `KONG_PROXY_PORT`.
The server certificate, the corresponding private key and the root CA certificate are expected to be under:
- Server certificate: `/etc/certs/server.crt`
- Server private key: `/etc/certs/private.key`
- Root CA certificate: `/etc/certs/ca.crt`
