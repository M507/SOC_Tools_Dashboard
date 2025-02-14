FROM python:3.9

WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Generate SSL certificate
RUN apt-get update && apt-get install -y openssl && \
    openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365 \
    -subj "/CN=localhost"

# Copy app files
COPY . .

# Run Flask app
CMD ["python", "soc_web.py"]
