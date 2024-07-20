FROM python:3.12.4
WORKDIR /app
COPY . .

# Define build arguments
ARG SECRET_KEY
ARG AWS_ACCOUNT_ID
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG AWS_STORAGE_BUCKET_NAME
ARG AWS_DB_NAME
ARG AWS_DB_USER
ARG AWS_DB_PASSWORD
ARG AWS_DB_HOST
ARG AWS_DB_PORT

# Use build arguments as environment variables
ENV SECRET_KEY=${SECRET_KEY}
ENV AWS_ACCOUNT_ID=${AWS_ACCOUNT_ID}
ENV AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
ENV AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}
ENV AWS_STORAGE_BUCKET_NAME=${AWS_STORAGE_BUCKET_NAME}
ENV AWS_DB_NAME=${AWS_DB_NAME}
ENV AWS_DB_USER=${AWS_DB_USER}
ENV AWS_DB_PASSWORD=${AWS_DB_PASSWORD}
ENV AWS_DB_HOST=${AWS_DB_HOST}
ENV AWS_DB_PORT=${AWS_DB_PORT}

RUN python -m pip install --user pipx
RUN python -m pipx ensurepath
RUN python -m pipx install poetry
RUN python -m pipx run poetry install

EXPOSE 8000
# CMD sh
RUN python -m pipx run poetry run python manage.py collectstatic --noinput
RUN python -m pipx run poetry run python manage.py makemigrations --noinput
RUN python -m pipx run poetry run python manage.py migrate --noinput
CMD python -m pipx run poetry run daphne myFacegram.asgi:application -b 0.0.0.0 -p 8000
