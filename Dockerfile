FROM python:3.12-slim-bullseye AS base

# Instalar dependencias del sistema
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libgl1 \
        libgl1-mesa-dri \
        libglib2.0-0 \
        gcc \
        python3-dev \
        libzbar0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
        
# Actualizar pip
RUN pip3 install --upgrade pip

# Crear directorio de la aplicación
RUN mkdir /app

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar y instalar dependencias de Python
COPY requirements.txt /app
RUN pip3 install --no-cache-dir -r requirements.txt

# Copiar archivos del proyecto
COPY . /app/

# Copiar y dar permisos de ejecución al script de entrada
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Establecer el script de entrada
ENTRYPOINT ["/app/entrypoint.sh"]
