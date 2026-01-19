from fastapi import FastAPI
from app.routes import (
    jobs, applications, resumes,
    candidates, employers, admin
)
from app.core.db import init_db
app = FastAPI(title="Job Board API")

@app.on_event("startup")
def on_startup():
    init_db()


app.include_router(jobs.router, prefix="/jobs", tags=["Jobs"])
app.include_router(applications.router, prefix="/applications", tags=["Applications"])
app.include_router(resumes.router, prefix="/resumes", tags=["Resumes"])
app.include_router(candidates.router, prefix="/candidates", tags=["Candidates"])
app.include_router(employers.router, prefix="/employers", tags=["Employers"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])