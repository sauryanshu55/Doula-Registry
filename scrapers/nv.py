import pandas
import requests

results = []
total_results_to_fetch = 1  # at least 1
page = 1
while len(results) < total_results_to_fetch:
    response = requests.get(
        (
            "https://ncb.certemy.com/api/organization/public_registry/"
            "982a89ca-1934-40a6-a5f4-26698cb87e38?&filters="
            "{%22last_name%22:[],%22certificationIds%22:[]"
            ",%22organizationId%22:null}"
            f"&page={page}&page_size=20"
            "&order_id=last_name&order_type=asc"
        ),
    )

    print(response.url)

    assert response.status_code == 200
    results.extend(response.json()["result"])

    if total_results_to_fetch == 1:
        total_results_to_fetch = response.json()["count"]

    page += 1


pandas.DateFrame(results).to_csv("data/nv.csv", index=False)
