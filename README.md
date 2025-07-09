# Image Caption Generator

A web application that generates descriptive captions for uploaded images using the BLIP (Bootstrapped Language Image Pretraining) model from Hugging Face Transformers. The app is built with FastAPI and features a modern, user-friendly interface.

## Features

- **Image Upload:** Upload any image and receive an AI-generated caption.
- **State-of-the-art Model:** Uses Salesforce's BLIP image captioning model for high-quality results.
- **Web Interface:** Clean, responsive UI built with HTML and CSS.
- **FastAPI Backend:** Efficient, asynchronous server for quick responses.

## Demo

![App Screenshot](static/Screenshot%202025-07-08%20173119.png)

## How It Works

1. **User uploads an image** via the web interface.
2. The backend loads the image and processes it using the BLIP model.
3. The model generates a caption describing the image.
4. The caption and the uploaded image are displayed on the page.

## Project Structure

```
Image_Caption_Generator/
│
├── app.py                  # Main FastAPI application
├── requirementes.txt       # Python dependencies
├── README.md               # Project documentation
├── static/                 # Static files (uploaded images, logo)
│   ├── Screenshot 2025-07-08 173119.png
│   └── uploaded_image.jpg
└── templates/
    └── index.html          # HTML template for the web UI
```

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Image_Caption_Generator.git
   cd Image_Caption_Generator
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirementes.txt
   ```

3. **Download the BLIP model:**
   The model will be automatically downloaded the first time you run the app.

## Usage

1. **Start the server:**
   ```bash
   uvicorn app:app --reload
   ```

2. **Open your browser and go to:**
   ```
   http://127.0.0.1:8000/
   ```

3. **Upload an image** and get a caption!

## Code Overview

- **app.py:**  
  - Loads the BLIP processor and model from Hugging Face.
  - Defines a FastAPI app with two routes:
    - `GET /`: Renders the upload form.
    - `POST /`: Handles image upload, generates a caption, and displays the result.
  - Saves the uploaded image to `static/uploaded_image.jpg` for display.

- **templates/index.html:**  
  - Provides a modern, dark-themed UI for uploading images and displaying results.
  - Shows a spinner while the caption is being generated.

- **requirementes.txt:**  
  - Lists all required Python packages, including FastAPI, Transformers, Torch, Pillow, and Uvicorn.

## Dependencies

- `fastapi`
- `uvicorn`
- `transformers`
- `torch`
- `Pillow`
- `starlette`
- `aiofiles`
- `python-multipart`
- `sentencepiece`

Install them all with:
```bash
pip install -r requirementes.txt
```

## Notes

- The BLIP model is large and may require a good internet connection and sufficient RAM for the first download.
- For production, consider serving with a production ASGI server and securing file uploads.

## License

This project is for educational purposes. 
