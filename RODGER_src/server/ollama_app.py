from flask import Flask, request, jsonify
import ollama
import time
import os, sys
from datetime import datetime

app = Flask(__name__)
model_name = 'llama3'
messages_take_order = []
messages_sit_customer = []

participant_id = sys.argv[1] if len(sys.argv) > 1 else 'default_participant'

def read_initial_prompt(file_path):
    with open(file_path, 'r') as file:
        initial_prompt = file.read().strip()
    return initial_prompt

def build_incremental_prompt(initial_prompt, messages):
    context = []
    context.append({"role": "system", "content": initial_prompt})
    for message in messages:
        role, content = message
        context.append({'role': role, 'content': content})
    return context

def setup_logging(participant_id):
    log_dir = f"logs/"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    return os.path.join(log_dir, f"participant_{participant_id}.log")

def log_message(participant_id, type_call ,message):
    log_file_path = setup_logging(participant_id)
    with open(log_file_path, 'a') as log_file:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_file.write(f"{timestamp} | {type_call} - {message}\n")

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the API!"

@app.route('/get_data', methods=['GET'])
def get_data():
    data = {"message": "This is a GET request"}
    return jsonify(data)

@app.route("/sit_customer", methods=['POST'])
def sit_customer():
    start_time = time.time()
    
    # messag received
    data = request.get_json()
    messages_sit_customer.append(("user", data['input']))

    file_path = "PATH_TO_CONTEXT/sit_customer_context.txt"
    initial_prompt = read_initial_prompt(file_path=file_path)
    context = build_incremental_prompt(initial_prompt, messages_sit_customer)

    print("********************************")
    print("          CONTEXT")
    print("********************************")
    print(context)
    print("********************************")
    print("\n\n\n")

    response = ollama.chat(model=model_name, messages=context)
    print("Assistant > ", response['message']['content'])

    messages_sit_customer.append(("assistant", response['message']['content']))
    elapsed_time = time.time() - start_time

    log_message(participant_id,f'POST/sit_customer', f"Time taken: {elapsed_time} seconds")

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    call_type =  f"{timestamp} | POST/sit_customer"

    return jsonify({"response": response['message']['content'], "call_type": call_type, "elapsed_time": elapsed_time})


@app.route('/take_order_drink', methods=['POST'])
def handle_order_drink():
    start_time = time.time()

    #message received 
    data = request.get_json()
    messages_take_order.append(("user", data['input']))

    file_path = 'PATH_TO_CONTEXT/take_order_drink_context.txt'
    initial_prompt = read_initial_prompt(file_path=file_path)
    context = build_incremental_prompt(initial_prompt, messages_take_order)

    print("********************************")
    print("          CONTEXT")
    print("********************************")
    print(context)
    print("********************************")
    print("\n\n\n")
    response = ollama.chat(model=model_name, messages=context)
    print("Assistant > ", response['message']['content'])

    messages_take_order.append(("assistant", response['message']['content']))
    elapsed_time = time.time() - start_time


    log_message(participant_id, f'POST /take_order', f"Time taken: {elapsed_time} seconds")

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    call_type =  f"{timestamp} | POST/take_order"

    return jsonify({"response": response['message']['content'], "call_type": call_type, "elapsed_time": elapsed_time})

@app.route('/take_order_dessert', methods=['POST'])
def handle_order_dessert():
    start_time = time.time()

    #message received 
    data = request.get_json()
    messages_take_order.append(("user", data['input']))

    file_path = 'PATH_TO_CONTEXT/take_order_dessert_context.txt'
    initial_prompt = read_initial_prompt(file_path=file_path)
    context = build_incremental_prompt(initial_prompt, messages_take_order)

    print("********************************")
    print("          CONTEXT")
    print("********************************")
    print(context)
    print("********************************")
    print("\n\n\n")
    response = ollama.chat(model=model_name, messages=context)
    print("Assistant > ", response['message']['content'])

    messages_take_order.append(("assistant", response['message']['content']))
    elapsed_time = time.time() - start_time


    log_message(participant_id, f'POST /take_order', f"Time taken: {elapsed_time} seconds")

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    call_type =  f"{timestamp} | POST/take_order"

    return jsonify({"response": response['message']['content'], "call_type": call_type, "elapsed_time": elapsed_time})

@app.route('/take_order_food', methods=['POST'])
def handle_order_food():
    start_time = time.time()

    #message received 
    data = request.get_json()
    messages_take_order.append(("user", data['input']))

    file_path = 'PATH_TO_CONTEXT/take_order_food_context.txt'
    initial_prompt = read_initial_prompt(file_path=file_path)
    context = build_incremental_prompt(initial_prompt, messages_take_order)

    print("********************************")
    print("          CONTEXT")
    print("********************************")
    print(context)
    print("********************************")
    print("\n\n\n")
    response = ollama.chat(model=model_name, messages=context)
    print("Assistant > ", response['message']['content'])

    messages_take_order.append(("assistant", response['message']['content']))
    elapsed_time = time.time() - start_time


    log_message(participant_id, f'POST /take_order', f"Time taken: {elapsed_time} seconds")

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    call_type =  f"{timestamp} | POST/take_order"

    return jsonify({"response": response['message']['content'], "call_type": call_type, "elapsed_time": elapsed_time})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
