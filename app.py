from fastapi import FastAPI, Form, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import io

# ✅ Load BLIP model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

app = FastAPI()

# Static and templates setup
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# 🚀 Function to generate caption
def generate_caption(image: Image.Image) -> str:
    inputs = processor(image, return_tensors="pt")
    out = model.generate(**inputs, max_length=20, num_beams=4)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "caption": None,
        "image_url": None,
    })


@app.post("/", response_class=HTMLResponse)
async def generate(request: Request, file: UploadFile):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")
    caption = generate_caption(image)

    # Save uploaded image for display
    image_path = "static/uploaded_image.jpg"
    image.save(image_path)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "caption": caption,
        "image_url": "/" + image_path,
    })
