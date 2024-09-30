import requests
import json
import time

time_start = time.time()
print("[+] Time started")

def send_request_post(message):

    time_start_request = time.time()
    # Define the URL of the Flask app's /greet endpoint
    url = 'http://localhost:5000/greet'

    # Define the payload to send in the POST request
    payload = {
        "input": message
    }

    # Convert the payload to a JSON string
    json_payload = json.dumps(payload)

    # Define the headers for the request
    headers = {
        'Content-Type': 'application/json'
    }

    # Send the POST request
    response = requests.post(url, headers=headers, data=json_payload)

    # Print the response from the server
    if response.status_code == 200:
        # print("Success:", response.json())
        time_request = time.time() - time_start_request
        print("[!] Request Successfull. Time >", time_request, "seconds")
    else:
        print("Error:", response.status_code, response.text)

    
queries_text = ["hello", "You're a waiter robot, please welcome the new guest", "Thank you"]

def test_query_time(num_queries=3):
    time_total = 0
    for i in range(num_queries):
        print(f"\n\n[!] Query num: {i}")
        time_start = time.time()
        for j in queries_text:
            send_request_post(j)
        time_total += time.time() - time_start
    print(f"[++] AVG Total time for queries: {time_total/num_queries}")

if __name__ == "__main__":
    test_query_time(3)
    print("\n\n")
    print("[+] Time taken", time.time() - time_start, "seconds")