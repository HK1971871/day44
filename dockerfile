FROM python:3.11-slim

# Giảm size & cài nền tảng tối thiểu
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Cài dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source
COPY . .

# Expose cổng 5000
EXPOSE 5000

# Chạy Gunicorn cho production
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "app:app"]