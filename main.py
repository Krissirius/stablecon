from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
myvar = {'message': 'Hello world!'}  # Имя ключа в словаре сделано строчным для соответствия стандартам Python

# Настройка путей для шаблонов и статических файлов
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def read_root(request: Request):
    # Передаем myvar в контексте шаблона
    return templates.TemplateResponse("index.html", {"request": request, "myvar": myvar})

