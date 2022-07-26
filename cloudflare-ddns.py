import requests
import json
import os
from dotenv import load_dotenv

def main():
    load_dotenv()

    try:
        api_key = get_env('CLOUDFLARE_API_KEY')
        zone_id = get_env('CLOUDFLARE_ZONE_ID')
        record_id = get_env('CLOUDFLARE_RECORD_ID')
        my_ip = get_ip()
    except Exception as e:
        print(e)
    else:
        success = update_record(
            api_key=api_key,
            zone_id=zone_id,
            record_id=record_id,
            ip=my_ip
        )
        print (my_ip + (" Success" if success else " Failed"))

def get_env(key):
    var = os.environ.get(key)
    if var is None:
        raise Exception("No " + key + " found in .env file.")
    
    return var

def get_ip():
    endpoint = 'https://ipinfo.io/json'
    response = requests.get(endpoint, verify = True, timeout=5)

    if response.status_code != 200:
        raise Exception("HTTP error reaching " + endpoint)
    
    data = response.json()

    if "ip" not in data:
        raise Exception("No IP address returned")

    return data['ip']

def update_record(api_key,zone_id,record_id, ip):

    url = "https://api.cloudflare.com/client/v4/zones/"+zone_id+"/dns_records/"+record_id

    payload = json.dumps({
        "content": ip
    })
    
    headers = {
        'Authorization': 'Bearer '+api_key,
        'Content-Type': 'application/json'
    }

    response = requests.request("PATCH", url, headers=headers, data=payload)
    return response.json().get("success") == True

if __name__ == '__main__':
    main()
