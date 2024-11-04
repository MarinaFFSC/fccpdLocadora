# db/Dockerfile

FROM mysql:latest
ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=locadora
ENV MYSQL_USER=user
ENV MYSQL_PASSWORD=pass
COPY init.sql /docker-entrypoint-initdb.d/
