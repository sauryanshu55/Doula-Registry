import csv
import json
import requests

headers = {
    "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    "Referer": "https://mdhhs-pres-prod.michigan.gov/DoulaMap/",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
    + "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "sec-ch-ua-platform": '"macOS"',
}

params = {
    "version": "211007",
}

response = requests.get(
    "https://mdhhs-pres-prod.michigan.gov/DoulaMap/data/Doulas.js",
    params=params,
    headers=headers,
)

assert response.status_code == 200


def f(d):
    formatted = d.strip()
    if formatted[-1] == ";":
        formatted = formatted[:-1]

    return json.loads(formatted)


# file is served as a js file, need to parse into JSON
doula_data_raw = response.text
doulas = list(
    map(
        f,
        doula_data_raw.split("doulas[doulas.length] = ")[1:],
    )
)

assert len(doulas) > 0

with open("scrapers/data/mi.csv", "w", newline="") as file:

    writer = csv.DictWriter(file, fieldnames=doulas[0].keys())
    writer.writeheader()

    writer.writerows(doulas)

print("Michigan scraper ran successfully.")
