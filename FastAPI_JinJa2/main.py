import uvicorn
from fastapi import FastAPI, UploadFile,Request,Form ,Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from schemas import *

app = FastAPI()

templates = Jinja2Templates(directory='templates')
app.mount("/static",StaticFiles(directory='static'),name = 'static')

@app.get('/basic',response_class=HTMLResponse)
async def get_basic_form(request:Request):
    return templates.TemplateResponse('basic-form.html',{'request':request})

@app.post('/basic',response_class=HTMLResponse)
async def get_basic_form(request:Request,username:str = Form(...),password: str = Form(...)):
    print(f'username:{username}')
    print(f'password:{password}')
    return templates.TemplateResponse('basic-form.html',{'request':request,'password':password})

@app.get('/awesome', response_class=HTMLResponse)
def get_form(request: Request):
    return templates.TemplateResponse("awesome.html", {"request": request})

@app.post('/awesome', response_class=HTMLResponse)
def post_form(request: Request, form_data: AwesomeForm = Depends(AwesomeForm.as_form)):
    print(form_data)
    return templates.TemplateResponse("awesome.html", {"request": request,'data':form_data.username})