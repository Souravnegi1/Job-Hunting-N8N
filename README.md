\# Job Hunting Automation



An automated job-search system built with Python, FastAPI, Adzuna API, n8n, and Telegram.



The system allows a user to send job-search requirements through Telegram, such as:



/job Python Developer | Maharashtra | 2 years



The request is processed by an n8n workflow, sent to a FastAPI backend, and matching jobs are returned to Telegram.



\---



\## Project Architecture



```text

Telegram

&#x20;   |

&#x20;   v

n8n Schedule Trigger

&#x20;   |

&#x20;   v

Telegram getUpdates

&#x20;   |

&#x20;   v

Extract Message

&#x20;   |

&#x20;   v

Parse Role / Location / Experience

&#x20;   |

&#x20;   v

FastAPI /fetch-jobs

&#x20;   |

&#x20;   v

Adzuna Jobs API

&#x20;   |

&#x20;   v

Job Normalization \& Filtering

&#x20;   |

&#x20;   v

n8n Job Formatting

&#x20;   |

&#x20;   v

Telegram





Features

Search jobs using job role

Search jobs by location

Filter jobs using experience

Fetch jobs from Adzuna API

Normalize job data

Remove duplicate jobs

Filter jobs using keywords

FastAPI REST API

n8n workflow automation

Telegram-based job search

Automated job results delivered to Telegram

Technologies Used

Python

FastAPI

Pydantic

Requests

Adzuna Jobs API

n8n

Telegram Bot API

Docker

Git \& GitHub

Telegram Input Format



The bot accepts job-search requests in the following format:



/job <role> | <location> | <experience>



Example:



/job Python Developer | Maharashtra | 2 years



Another example:



/job Software Engineer | Bangalore | 3 years

FastAPI API

GET /



Checks whether the API is running.



Example response:



{

&#x20; "message": "Job hunting API is running"

}

GET /jobs



Returns saved jobs.



POST /fetch-jobs



Fetches jobs based on:



Role

Location

Experience



Example request:



{

&#x20; "role": "Python Developer",

&#x20; "location": "Maharashtra",

&#x20; "experience": "2 years"

}

Python Job Pipeline



The Python backend performs the following operations:



Fetch jobs from Adzuna API

Normalize job information

Remove duplicate jobs

Apply experience filtering

Apply keyword filtering

Save job results as JSON

Return the results through FastAPI

n8n Automation



The n8n workflow handles the automation layer.



Main workflow:



Schedule Trigger

&#x20;       |

&#x20;       v

Telegram getUpdates

&#x20;       |

&#x20;       v

Extract Telegram Message

&#x20;       |

&#x20;       v

Parse Job Search Parameters

&#x20;       |

&#x20;       v

POST /fetch-jobs

&#x20;       |

&#x20;       v

Check Job Results

&#x20;       |

&#x20;       v

Format Jobs

&#x20;       |

&#x20;       v

Send Results to Telegram

Screenshots

n8n Workflow



FastAPI Job Search Request



Telegram Job Results



Environment Variables



Create a .env file:



ADZUNA\_APP\_ID=your\_app\_id

ADZUNA\_APP\_KEY=your\_app\_key



Do not commit .env to GitHub.



Installation



Clone the repository:



git clone <your-github-repository-url>



Go to the project directory:



cd job-hunting-automation



Create a virtual environment:



python -m venv venv



Activate it on Windows:



venv\\Scripts\\activate



Install dependencies:



pip install -r requirements.txt

Run FastAPI



Start the FastAPI server:



uvicorn app.main:app --reload --host 0.0.0.0 --port 8000



The API will be available locally at:



http://localhost:8000

Project Structure

job-hunting-automation/

│

├── app/

│   ├── job\_api.py

│   └── main.py

│

├──  ## Screenshots



\### n8n Workflow



!\[n8n Workflow](./screenshots/01-workflow-overview.png)



\### FastAPI Fetch Jobs



!\[FastAPI Fetch Jobs](./screenshots/02-fetch-jobs-api.png)



\### Telegram Job Results



!\[Telegram Job Results](./screenshots/03-telegram-output.png)

│   

├── .gitignore

├── README.md

└── requirements.txt

Future Improvements

AI-based job matching

Resume-based job recommendations

Salary filtering

Remote/hybrid filtering

Multiple job portals

Scheduled daily job alerts

LLM-based job relevance scoring

Resume-to-job similarity analysis

Persistent Telegram update tracking

Database integration

Author



Sourav



Built as a job-hunting automation project using Python, FastAPI, n8n and Telegram.

