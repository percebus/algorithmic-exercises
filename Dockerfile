FROM python:3.14.7 AS base

FROM base AS project
WORKDIR /usr/app
COPY . .
RUN ls -la
RUN bash _scripts/bash/clean.ba.sh


FROM project AS dev
RUN bash _scripts/install.ba.sh

FROM dev AS tested
RUN pipx run -- pypyr ci_docker

# TODO use light image. alpine?
FROM project AS release
RUN bash _scripts/pip/install.ba.sh 'release'
CMD [ "python", "src/problems/" ]
