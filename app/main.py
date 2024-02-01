from fastapi import FastAPI
import uvicorn
from app.public.weather import weather_router


app = FastAPI()
app.include_router(weather_router)
@app.get("/")
def index():
    return {"title": "Hello!"}

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)