from fastapi import APIRouter
import base64
from io import BytesIO
from apps.calculator.utils import analyze_image
from schema import ImageData
from PIL import Image

router = APIRouter()

@router.post("")
async def run(data: ImageData):
    try:
        image_data = base64.b64decode(data.image.split(",")[1]) 
        image_bytes = BytesIO(image_data)
        image = Image.open(image_bytes)
        responses = analyze_image(image, dict_of_vars=data.dict_of_vars)
    
        data_list = []
        last_response = None 
        
        for response in responses:
            data_list.append(response)
            last_response = response 
        
        print("Response in route: ", last_response if last_response else "No response received")

        return {"message": "Image processed", "data": data_list, "status": "success"}

    except Exception as e:
        print("Error:", e)
        return {"message": "Error processing image", "error": str(e), "status": "failure"}
