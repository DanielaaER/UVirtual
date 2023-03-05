from fastapi import FastAPI
from routes.login import user
app= FastAPI()

app.include_router(user)