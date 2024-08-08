import uvicorn
from fastapi import FastAPI
from database import SessionLocal,engine,Base
from routers import users as UserRouter

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(UserRouter.router,prefix="/user")


if __name__ == "__main__":
    uvicorn.run(app,host='0.0.0.0',port=8001)