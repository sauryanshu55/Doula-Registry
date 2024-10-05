import os
import subprocess


if __name__ == "__main__":
    scraper_dir = "scrapers"
    data_dir = f"{scraper_dir}/data"

    state_scrapers = [
        f 
        for f in os.listdir(scraper_dir)
        if f.endswith(".py")
    ]

    os.makedirs(data_dir, exist_ok=True)
    for state_scraper in state_scrapers:
        # each scraper should save data to a file in data directory 
        # with file name "{state}.csv" eg. "mn.csv" for minnesota
        result = subprocess.run(["python3", f"{scraper_dir}/{state_scraper}"])
        result.check_returncode()

        assert os.path.exists(f"{data_dir}/{state_scraper.replace('.py', '')}.csv")

    print("All files executed.")
