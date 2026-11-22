from fastapi import FastAPI,Request
from app.routers.student_router import router

app = FastAPI()

app.include_router(router)

@app.middleware("http")
async def add_middleware(request:Request,call_next):
    print("start")

    res=await call_next(request)
    print(res)

    print("close")
    return res

