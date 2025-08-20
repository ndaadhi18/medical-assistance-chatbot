from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from middlewares.exception_handlers import catch_exception_middleware
from routes.upload_pdfs import router as upload_router
from routes.ask_question import router as ask_router

app = FastAPI(title="Medical Assistant API", description="API for AI Medical Assistance")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_credentials=["*"],
    allow_headers=["*"]
)

# middleware exception handleers
app.middleware("http")(catch_exception_middleware)
# routers

# upload pdf docs
app.include_router(upload_router)
# asking query
app.include_router(ask_router)