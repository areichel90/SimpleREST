import requests


'''def POST(endpoint, payload, verbose=True):
    if verbose:
        print(f"POST: {endpoint}")
    requests.post(endpoint, data=payload)'''
    

def post_payload(endpoint, payload, verbose=True):
    print("this is a RESTful test!")
    print(payload)

    payloadTime = list(payload)[0]
    results = payload[payloadTime]
    downloadSpeed = results['down']
    uploadSpeed = results['up']
    deviceSSID = results['device_ssid']

    payload_to_post = {'device':deviceSSID,
                        'datetime':payloadTime,
                        'download_speed':downloadSpeed,
                        'upload_speed':uploadSpeed}
    
    if verbose:
        print(f"POST: {endpoint}")
        print(f"to_post: {payload_to_post}\n")
    
    requests.post(endpoint, data=payload_to_post)
