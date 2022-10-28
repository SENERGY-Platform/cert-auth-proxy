# CERT-AUTH-PROXY
This NGINX web server acts as a reverse proxy to authenticate requests with client certificates. Requests are then forwarded to the kong proxy to exchange a JWT user token.

# Build
```
docker build -t cert-auth-proxy .
```

# Deployment
This service needs a connection to the kong proxy which is set by `KONG_PROXY_HOST` and `KONG_PROXY_PORT`.
The server certificate, the corresponding private key and the root CA certificate are expected to be under `/etc/certs/`.
```
docker run -p 443:443 \
            -e KONG_PROXY_HOST=kong_proxy \
            -e KONG_PROXY_PORT=5000 \
            -v /etc/certs/server.crt \
            -v /etc/certs/private.key \
            -v /etc/ca/ca.crt \
            cert-auth-proxy 
```