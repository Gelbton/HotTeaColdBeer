# Fill in this file with the code from parsing JSON exercise
import json
import yaml

with open ('myfile.json', 'r') as json_file:
    ourjson = json.load(json_file)
    print(ourjson) 

print(f"The access token is: {ourjson['access_token']}")
print(f"The token expires in: {ourjson['expires_in']}seconds")
print("\n\n ---")
print(yaml.dump(ourjson))