import requests
from datetime import datetime
USERNAME="subh"
TOKEN="hkjsdhaiodhfsdf"
pixela_endpoint="https://pixe.la/v1/users"
user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
# response=requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)
graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config={
    "id":"graph1",
    "name":"cycling graph",
    "unit":"Km",
    "type":"float",
    "color":"momiji",
}
headers={
    "X-USER-TOKEN":TOKEN
}
# response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

graph_post_url=f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

day=datetime(year=2022,month=11,day=14)
date=day.strftime("%Y%m%d")

pixel_config={
    "date":date,
    "quantity":"50",
}
# response=requests.post(url=graph_post_url,json=pixel_config,headers=headers)
# print(response.text)

graph_update_url=f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{date}"
pixel_update_config={
    "quantity":"5",
}
# response=requests.put(url=graph_update_url,json=pixel_update_config,headers=headers)
# print(response.text)
response=requests.delete(url=graph_update_url,headers=headers)
print(response.text)
