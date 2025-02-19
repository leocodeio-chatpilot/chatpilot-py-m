FROM python:3.10-slim

WORKDIR /app

# copy pyproject.toml
COPY requirements.txt /app

# install dependencies
RUN pip3 install -r requirements.txt

# copy the rest of the code
COPY . /app

# run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
