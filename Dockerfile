FROM python:3.10.4-slim-buster
ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1
WORKDIR /usr/src
COPY Pipfile Pipfile.lock ./
RUN set -ex; \
    pip install pipenv; \
    pipenv install --system;
COPY ./src ./
EXPOSE 5000
ENTRYPOINT [ "flask" ]
CMD [ "run" ]
