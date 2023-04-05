FROM nginx:1.21

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
COPY nginx_prod.conf /etc/nginx/conf.d

ARG DEV=false

RUN if [ $DEV = "true" ]; \
    then rm -rf /etc/nginx/conf.d/nginx_prod.conf ; \
    else rm -rf /etc/nginx/conf.d/nginx.conf ; \
    fi
