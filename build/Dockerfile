FROM nginx AS prod
COPY default.conf.template /etc/nginx/templates/default.conf.template
EXPOSE 443

FROM nginx AS test 
COPY default.conf.template /etc/nginx/templates/default.conf.template
COPY tests/server_certs/server.crt  /etc/certs/server.crt
COPY tests/server_certs/private.key /etc/certs/private.key
COPY tests/ca_certs/ca.crt /etc/ca/ca.crt
EXPOSE 443