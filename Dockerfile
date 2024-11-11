# Koristimo osnovnu sliku za Python
FROM python:3.9-slim

# Postavljamo radni direktorij
WORKDIR /app

# Kopiramo requirements.txt i instaliramo zavisnosti
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Kopiramo ostatak aplikacije
COPY . .

# Treniramo i spremamo model
RUN python train_model.py

# Pokrećemo aplikaciju
CMD ["python", "app.py"]