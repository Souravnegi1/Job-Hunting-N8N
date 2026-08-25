from fastapi import FastAPI
import json
from pydantic import BaseModel
app = FastAPI()
from app.job_api import(
    fetch_all_jobs ,
    filter_jobs  ,
    save_jobs_to_json

)

@app.get("/")
def home():
    return {"message": "Job hunting API is running"}

class jobSearchRequest(BaseModel):
    role : str
    location : str
    experience : str
@app.get("/jobs")
def get_jobs():
    with open(
        "python_jobs.json" ,
        "r",
        encoding= "utf-8"
    ) as file:
        jobs =json.load(file)
    return {
        "total jobs": len(jobs) ,
        "jobs" : jobs
    }
@app.post("/fetch-jobs")
def fetch_jobs_api(request:jobSearchRequest):
    jobs = fetch_all_jobs(
        role =request.role, 
        location= request.location,
        experience= request.experience,
    
    )
    filtered_jobs =filter_jobs(jobs,"Python")
    save_jobs_to_json(filtered_jobs ,
                      "python_jobs.json")
    return {
       "jobs":filtered_jobs ,
        "total_jobs": len(filtered_jobs)
    }