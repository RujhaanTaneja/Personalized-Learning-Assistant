FROM python:3.11-slim

# Install Tesseract and other dependencies
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    libleptonica-dev \
    poppler-utils \
    && apt-get clean

# Install Python libraries
RUN pip install --no-cache-dir pytesseract Pillow
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

# Set the working directory inside the container


# Copy the current directory contents into the container


# Run the Python script
CMD ["bash", "-c", "python tess.py && python app.py"]
