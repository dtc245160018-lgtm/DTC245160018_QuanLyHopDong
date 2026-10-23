FROM python:3.10-slim

# Tạo user không có quyền root (Hardening)
RUN adduser --disabled-password --gecos '' appuser

WORKDIR /app

# Cài đặt các thư viện phụ thuộc
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ mã nguồn ứng dụng vào container
COPY . /app
RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 5000
CMD ["python", "app.py"]
