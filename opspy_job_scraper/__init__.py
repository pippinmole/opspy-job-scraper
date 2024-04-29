import os
import asyncio
from datetime import datetime

from cfkv import KVStore

from opspy_job_scraper.common.base_logger import logger
from opspy_job_scraper.database import insert_jobs
from opspy_job_scraper.scrape import run_scrape_jobs
from opspy_job_scraper.state import State
from opspy_job_scraper.state.state_storage import StateStorage

if __name__ == "__main__":
    # Log a header with the current datetime and a unique identifier
    run_id = datetime.now().strftime('%Y%m%d%H%M%S')
    logger.info("=== Starting new run: ID %s ===", run_id)

    store = StateStorage(store=KVStore(
        namespace_id=os.getenv("NAMESPACE_ID"),
        account_id=os.getenv("ACCOUNT_ID"),
        api_key=os.getenv("API_KEY")
    ))

    state = store.get_current_state()

    logger.info("Successfully loaded state: " + str(state))

    (location, country, fallback_currency) = state.get_location()
    keyword = state.get_keyword()

    jobs = run_scrape_jobs(
        location,
        country,
        fallback_currency,
        keyword=state.get_keyword(),
        results_wanted=int(str(os.getenv("RESULTS_WANTED", 25)))
    )

    logger.info("Successfully scraped %s jobs", str(len(jobs)))

    asyncio.run(insert_jobs(jobs))

    logger.info("Successfully inserted jobs")

    # Increment state and save to store
    state.increment()
    store.set_current_state(state)

    logger.info("Successfully updated state to: %s", str(state))
