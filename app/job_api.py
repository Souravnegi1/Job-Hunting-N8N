import os
import requests
import json
from dotenv import load_dotenv
load_dotenv()
def fetch_jobs(role = "Software engineer",
               location = "India",
               page = "1" ):
    app_id = os.getenv("ADZUNA_APP_ID")
    app_key = os.getenv("ADZUNA_APP_KEY")
    url = f"https://api.adzuna.com/v1/api/jobs/in/search/{page}"
    params= {
        "app_id":  app_id,
        "app_key": app_key ,
        "results_per_page": 20 ,
        "what": role ,
        "where" :  location ,
        # "content-type":"application/json"
    }
    headers = {
        "Accept" : "application/json"
    }
    print("APP ID loaded:", bool(app_id))
    print("APP KEY loaded:", bool(app_key))
    print("URL:", url)
    print("PARAMS:", params)
    try:
        response = requests.get(
            url , 
            params=params ,
            timeout=10 ,
            headers=headers
        )
        print("STATUS:", response.status_code)
        print("RESPONSE:", response.text)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Adzuna API Request Failed: {e}")
        return None
def normalize_job(job):
    return{
        "title" : job.get("title", ""),
        "company" : job.get("company" , {}).get("display_name", "") ,
        "location": job.get("location", {}).get("display_name","") ,
        "description": job.get("description" , "") ,
        "url": job.get("redirect_url", "") ,
        "created":job.get("created", ""),
        "category": job.get("category",{}).get("label","") ,
    }

def fetch_all_jobs(role=  "Software Engineer", 
                   location = "India",
                   max_pages  ="2" ,
                   experience = "" ):
     all_jobs = []
     seen_urls = set()
     max_pages = int(max_pages)

     for current_page in range(1 , max_pages +1):
          jobs_data =fetch_jobs(role=role ,
                                location=location ,
                                page=current_page)
          if not jobs_data:
               print(f"Could not fetch page {current_page} ")
               continue
          raw_jobs =jobs_data.get("results" , [])

          print(f"Jobs found on page {current_page}:" , len(raw_jobs))

          for job in raw_jobs:
                normalized_job = normalize_job(job)
                job_url = normalized_job["url"]
                if not job_url:
                     continue
                if job_url in seen_urls:
                    continue
                seen_urls.add(job_url)
                all_jobs.append(normalized_job) 
     if experience:
          experience_jobs =[]
          for job in all_jobs:
               text =(
                    job["title"] +" " + job["description"]).lower()
               if experience.lower() in text:
                    experience_jobs.append(job)
                    all_jobs = experience_jobs
     return all_jobs
          

def display_jobs(jobs):
     for job in jobs[:5]:
                 print("title :" , job["title"])
                 print("Company:" , job["company"])
                 print("Location:" , job["location"])
                 print("Url:" , job["url"])
                 print("-" * 50)

def filter_jobs(jobs, keyword):
     filtered_jobs =[]
     keyword =keyword.lower()

     for job in jobs:
          title = job["title"].lower()
          description = job["description"].lower()
          if keyword in title or keyword in description:
               filtered_jobs.append(job)
     return filtered_jobs


def save_jobs_to_json(jobs , filename="jobs.json"):
    indexed_jobs = []
    # job = display_jobs
    for i, job in enumerate(jobs, start=1):
     indexed_jobs.append({
        "index": i,
        "job": job})
     with open(filename , "w" , encoding="utf-8") as file:
          json.dump(indexed_jobs , file , indent=4 ,ensure_ascii=False)
     print(f"Jobs saved successfully to {filename}")
    

if  __name__ == "__main__":
    jobs = fetch_all_jobs(role="Software engineer" ,location= "India" , max_pages=3 , experience="")
    print("Totle jobs:" , len(jobs))
    filtered_jobs = filter_jobs(jobs , "Python")
    print("Python jobs:", len(filtered_jobs))
    display_jobs(jobs)
    save_jobs_to_json(filtered_jobs, "python_jobs.json")

         




       

     
     


