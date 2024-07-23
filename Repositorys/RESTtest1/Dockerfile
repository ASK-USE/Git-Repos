FROM python:3.9-slim

# Copy libcrypt.so.1 into the Docker image
# COPY /var/lib/flatpak/runtime/org.freedesktop.Platform/x86_64/22.08/f3a591e25e87b8267afc80f350b1ead04d5627492dc7f4b19e9b8a4903c5673a/files/lib/x86_64-linux-gnu/libcrypt.so.1 /lib/libcrypt.so.1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]
