from fastapi import FastAPI


from dotenv import load_dotenv
load_dotenv(r"assets/.env")

from routes import base



app=FastAPI()

app.include_router(base.route )