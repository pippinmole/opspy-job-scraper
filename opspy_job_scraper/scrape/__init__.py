from jobspy import scrape_jobs, JobPost, DescriptionFormat
from dotenv import load_dotenv

load_dotenv()

sites = "indeed"


def run_scrape_jobs(location: str, country: str, fallback_currency: str, keyword: str,
                    results_wanted: int) -> list[JobPost]:
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

    print(f"Searching for {results_wanted} {keyword} jobs in {location}")

    jobs = scrape_jobs(
        site_name="indeed",
        search_term=keyword,
        country_indeed=country,
        location=location,
        description_format=DescriptionFormat.MARKDOWN,
        results_wanted=results_wanted,
    )

    # Filter bad rows
    jobs = list(filter(is_valid, jobs))

    for job in jobs:
        job.compensation.currency = job.compensation.currency if job.compensation.currency else fallback_currency

    print(f"Found {len(jobs)} jobs")

    return jobs
