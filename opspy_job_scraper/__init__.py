import os
import asyncio

from cfkv import KVStore

from opspy_job_scraper.database import insert_jobs
from opspy_job_scraper.scrape import run_scrape_jobs
from opspy_job_scraper.state import State
from opspy_job_scraper.state.state_storage import StateStorage

if __name__ == "__main__":
    store = StateStorage(store=KVStore(
        namespace_id=os.getenv("NAMESPACE_ID"),
        account_id=os.getenv("ACCOUNT_ID"),
        api_key=os.getenv("API_KEY")
    ))

    state = store.get_current_state()

    print("Successfully loaded state: " + str(state))

    (location, country, fallback_currency) = state.get_location()
    keyword = state.get_keyword()

    jobs = run_scrape_jobs(
        location,
        country,
        fallback_currency,
        keyword=state.get_keyword(),
        results_wanted=int(str(os.getenv("RESULTS_WANTED", 25)))
    )

    print("Successfully scraped", str(len(jobs)), "jobs")

    asyncio.run(insert_jobs(jobs))

    print("Successfully inserted jobs")

    # Increment state and save to store
    state.increment()
    store.set_current_state(state)

    print("Successfully updated state to: " + str(state))
