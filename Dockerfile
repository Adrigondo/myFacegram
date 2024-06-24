FROM python:3.12.4

WORKDIR /app

COPY . .

RUN python -m pip install --user pipx
RUN python -m pipx ensurepath
RUN python -m pipx install poetry
RUN python -m pipx run poetry install

EXPOSE 8000
# CMD sh
CMD python -m pipx run poetry run daphne myFacegram.asgi:application -b 0.0.0.0 -p 8000
