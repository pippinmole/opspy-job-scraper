import json

from jobspy import scrape_jobs, JobPost, DescriptionFormat
import os
from dotenv import load_dotenv
from state import State

load_dotenv()

sites="indeed"

# sites = [
#     "indeed",  # Only one that gives description
#     # "linkedin",
#     # "zip_recruiter",
#     # "glassdoor",
# ]

state_container_name = "scrape-state"
state_blob_name = "state.json"


def ensure_state_exists() -> None:
    # Ensure file state.json exists in file system
    if not os.path.exists(state_blob_name):
        with open(state_blob_name, "w") as f:
            f.write(json.dumps(State(0, 0).__dict__))


def get_current_state() -> State:
    ensure_state_exists()

    # Read all text from file
    with open(state_blob_name, "r") as f:
        return State(**json.loads(f.read()))


def set_current_state(state: State):
    # Write all text to file
    with open(state_blob_name, "w") as f:
        f.write(json.dumps(state.__dict__))


def filter_data(j: list[JobPost]) -> list[JobPost]:
    def is_valid(job: JobPost) -> bool:
        if job.compensation is None:
            return False

        if job.compensation.min_amount is None:
            return False

        if job.compensation.max_amount is None:
            return False

        if job.compensation.currency is None:
            return False

        return True

    return list(filter(is_valid, j))


def run_scrape_jobs(location: str, country: str, fallback_currency: str, keyword: str,
                    results_wanted: int) -> list[JobPost]:
    print(f"Searching for {results_wanted} {keyword} jobs in {location}")

    jobs = scrape_jobs(
        site_name="indeed", search_term="software engineer", country_indeed="usa",
        description_format=DescriptionFormat.MARKDOWN
    )

    # Filter bad rows
    jobs = filter_data(jobs)

    for job in jobs:

        print("Compensation:", job.compensation.__dict__)
        print("Job:", job.job_type)
        job.compensation.currency = job.compensation.currency if job.compensation.currency else fallback_currency

    print(f"Found {len(jobs)} jobs")
    print(jobs[0].dict())

    return jobs
