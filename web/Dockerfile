FROM python:3.9

WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

# Run Flask app
CMD ["python", "soc_web.py"]
