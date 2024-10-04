import os
import subprocess


if __name__ == "__main__":
    scraper_dir = "scrapers"
    state_scrapers = [
        f"{scraper_dir}/{f}" 
        for f in os.listdir(scraper_dir)
        if f.endswith(".py")
    ]

    for state_scraper in state_scrapers:
        # each scraper should save data to a file in data directory 
        # with file name "{state}.csv" eg. "mn.csv" for minnesota
        result = subprocess.run(f"python3 {state_scraper}", shell=True)

    print("All files executed.")
