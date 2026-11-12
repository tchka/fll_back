# FROM — базовый образ: Linux + Python 3.10 (как на PythonAnywhere).
FROM python:3.10-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=fll_drf.settings_docker

# COPY — копируем список пакетов в образ.
COPY requirements.txt /tmp/requirements.txt

# RUN — выполняется на сборке образа. setuptools<81 — та же дыра pkg_resources.
# backports.zoneinfo на 3.10 не нужен.
RUN pip install --no-cache-dir "setuptools<81" \
    && grep -v "backports.zoneinfo" /tmp/requirements.txt > /tmp/requirements_docker.txt \
    && pip install --no-cache-dir -r /tmp/requirements_docker.txt

# COPY — код проекта в образ.
COPY . /app
RUN mkdir -p static media

EXPOSE 8000

# CMD — что запустить, когда контейнер стартует.
CMD ["sh", "-c", "python manage.py migrate --noinput && python manage.py runserver 0.0.0.0:8000"]
