from datetime import datetime
from urllib.parse import urlparse, parse_qs


from prisma import Prisma
from jobspy import JobPost

from opspy_job_scraper.prisma.enums import JobType, JobStatus


def generate_company_id(company_name: str) -> str:
    return str(company_name).lower().replace(" ", "-")


async def create_companies(jobs: list[JobPost]) -> None:
    db = Prisma()
    await db.connect()

    # write your queries here
    for row in jobs:
        company_id = str(row.company_name).lower().replace(" ", "-")
        print("Creating company: ", row.company_name, "with id", company_id)

        await db.company.upsert(
            where={
                "id": company_id,
            },
            data={
                "create": {
                    "id": company_id,
                    "name": row.company_name,
                    "website": str(row.company_url),
                    "updatedAt": datetime.now(),
                },
                "update": {
                    "name": row.company_name,
                    "website": str(row.company_url),
                },
            },
        )

    await db.disconnect()


def pay_interval_map(interval: str) -> str:
    interval = interval.upper()

    if interval == "YEARLY":
        return "YEARLY"
    elif interval == "MONTHLY":
        return "MONTHLY"
    elif interval == "WEEKLY":
        return "WEEKLY"
    elif interval == "DAILY":
        return "DAILY"
    elif interval == "HOURLY":
        return "HOURLY"

    return "YEARLY"


def job_type_map(job_type: list[JobType] | None) -> str:
    if job_type is None or len(job_type) == 0:
        return str(JobType.FULL_TIME)

    job_type = job_type[0].name

    if job_type == "FULLTIME":
        return str(JobType.FULL_TIME)
    elif job_type == "PARTTIME":
        return str(JobType.PART_TIME)
    elif job_type == "INTERNSHIP":
        return str(JobType.INTERNSHIP)
    elif job_type == "CONTRACT":
        return str(JobType.CONTRACT)

    return str(JobType.FULL_TIME)


def get_indeed_job_id(url: str):
    """
    This function takes a Series of Indeed job URLs in the format:
    https://uk.indeed.com/viewjob?jk=0226eb0fa655a07f
    It extracts and returns the job ID (value of 'jk' query parameter).
    """

    parsed_url = urlparse(url)
    qs = parse_qs(parsed_url.query)
    # Extracting the first item of the list for 'jk' key
    return qs.get("jk", [None])[0]


async def insert_jobs(jobs: list[JobPost]) -> None:
    db = Prisma()
    await db.connect()

    await create_companies(jobs)

    # Prepare the data for bulk insertion
    jobs_to_insert = []
    for row in jobs:
        job_data = {
            "id": get_indeed_job_id(row.job_url),
            "minSalary": float(row.compensation.min_amount),
            "maxSalary": float(row.compensation.max_amount),
            "currency": row.compensation.currency,
            "interval": pay_interval_map(row.compensation.interval.name),
            "title": row.title,
            "type": job_type_map(row.job_type),
            "createdAt": datetime.combine(datetime.strptime(row.date_posted, "%Y-%m-%d"), datetime.min.time()),
            "updatedAt": datetime.now(),
            "companyId": generate_company_id(row.company_name),
            "location": row.location.display_location(),
            "description": row.description,
            "externalLink": row.job_url,
            "isQuickApply": False,
            "status": JobStatus.ACTIVE,
        }

        jobs_to_insert.append(job_data)

    # Bulk insert jobs using createMany with skipDuplicates
    added = await db.jobpost.create_many(
        data=jobs_to_insert,
        skip_duplicates=True
    )

    print("Added jobs: " + str(added))

    await db.disconnect()
