from careerjet_api import CareerjetAPIClient
import socket
import requests
import json

cj  =  CareerjetAPIClient("en_GB")

headers = requests.utils.default_headers()
userIp = socket.gethostbyname(socket.gethostname())
userAgent = headers['User-Agent']

print(userIp, userAgent)

result_json = cj.search({
  'location'    : 'United States',
  'keywords'    : 'CS',
  'affid'       : '213e213hd12344552',
  'user_ip'     : userIp,
  'user_agent'  : userAgent
})

print(json.dumps(result_json, indent=4))