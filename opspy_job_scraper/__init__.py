import os

import asyncio
import logging

from opspy_job_scraper.database import insert_jobs
from opspy_job_scraper.scrape import get_current_state, run_scrape_jobs, set_current_state

logging.info("Getting state")
state = get_current_state()
logging.info("Current state: " + str(state))

logging.info("Scraping jobs...")

(location, country, fallback_currency) = state.get_location()
keyword = state.get_keyword()

results_wanted = int(str(os.getenv("RESULTS_WANTED", 25)))
jobs = run_scrape_jobs(location, country, fallback_currency, keyword, results_wanted)
logging.info("Scraped jobs: " + str(len(jobs)))

logging.info("Inserting jobs...")
# save_jobs_to_file(jobs)
asyncio.run(insert_jobs(jobs))

# Increment state
state.increment()

logging.info("New state: " + str(state))

# Save state
set_current_state(state)