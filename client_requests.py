import requests

def GET(route, verbose=True):
    if verbose:
        print(f"GET: {route}")
    return requests.get(route)

def POST(endpoint, payload, verbose=True):
    if verbose:
        print(f"POST: {endpoint}")
    requests.post(endpoint, data=payload)

if __name__ == "__main__":
    sandbox_route = "http://127.0.0.1:8000/sandbox"
    test_payload = {
        "author": "macbook_PUT_", 
        "id": "test_payload_2", 
        "payload": "testing, testing?"
    }
    sandbox = GET(sandbox_route)
    POST(sandbox_route, test_payload)
    sandbox_updated = GET(sandbox_route)
    print(f"\nPayload: {sandbox.text}\n,\
        {sandbox_updated.text}" )
