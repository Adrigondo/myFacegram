FROM python:3.12.4
WORKDIR /app
COPY . .

# Define build arguments
ARG SECRET_KEY

# Use build arguments as environment variables
ENV SECRET_KEY=${SECRET_KEY}

RUN python -m pip install --user pipx
RUN python -m pipx ensurepath
RUN python -m pipx install poetry
RUN python -m pipx run poetry install

EXPOSE 8000
# CMD sh
RUN python -m pipx run poetry run python manage.py collectstatic --noinput &&
    python -m pipx run poetry run python manage.py makemigrations --noinput &&
    python -m pipx run poetry run python manage.py migrate --noinput
CMD python -m pipx run poetry run daphne myFacegram.asgi:application -b 0.0.0.0 -p 8000
