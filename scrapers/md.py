import pandas
import requests
from bs4 import BeautifulSoup

from utils.characters import normalize_whitespace, get_numeric

headers = {"accept-language": "en-US,en;q=0.9"}

response = requests.get(
    "https://encrypt.emdhealthchoice.org/searchable/main.action",
    headers=headers,
)

soup = BeautifulSoup(response.content, "html.parser")
mco_dropdown = soup.find("select", id="main_criteria_mcoNum")

mco_values = [mco["value"] for mco in mco_dropdown.find_all("option")[1:]]
mco_names = [mco.text.strip() for mco in mco_dropdown.find_all("option")[1:]]

all_doulas = []
for mco, mco_name in zip(mco_values, mco_names):
    data = {
        "criteria.mcoNum": mco,
        "criteria.providerType": "DL",
        "criteria.lastName": "",
        "criteria.provNpi": "",
        "criteria.county": "",
        "criteria.state": "MD",
        "criteria.zipCode": "",
        "criteria.distance": "0",
        "__checkbox_criteria.pcpOnly": "y",
        "action:search": "Search",
    }

    response = requests.post(
        "https://encrypt.emdhealthchoice.org/searchable/search.action",
        headers=headers,
        data=data,
    )

    if "There were no providers that matched your search criteria!" in response.text:
        continue

    soup = BeautifulSoup(response.content, "html.parser")
    doulas = soup.find_all("table", width="82%")

    for doula in doulas:
        doula_info = normalize_whitespace(doula.text.strip()).split("\n")

        all_doulas.append(
            {
                "name": doula_info[0].strip(),
                "address": doula_info[3].strip() + ", " + doula_info[9].strip(),
                "phone": get_numeric(doula_info[12]),
                "provider_number": get_numeric(doula_info[22]),
                "npi": get_numeric(doula_info[25]),
                "providerType": "Doula",
                "handicap_accessible": doula_info[42].strip()[-1],
                "tty": doula_info[46].strip()[-1],
                "managed_care_organization": mco_name,
            }
        )

pandas.DataFrame(all_doulas).to_csv("scrapers/data/md.csv", index=False)
