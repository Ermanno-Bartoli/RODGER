import ollama
import time
import sys
import os
# Correcting the path to include the project root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, project_root+"/light_chatbot")
from logger.logger import RunLogger


class ChatBot:
    def __init__(self) -> None:
        self.histories = []
        self.messages_sit_customer = []


        # Read the ChatGPT context from a file
        self.context_location = "PATH_TO_CONTEXT"
        if self.context_location is None:
            raise RuntimeError("You have to provide a context location")

        with open(self.context_location, 'r') as f:
            self.gpt_context = f.read()

    def read_initial_prompt(self):
        with open(self.context_location, 'r') as file:
            initial_prompt = file.read().strip()
        return initial_prompt

    def build_incremental_prompt(self,initial_prompt, messages):
        context = []
        context.append({"role": "system", "content": initial_prompt})
        for message in messages:
            role, content = message
            context.append({'role': role, 'content': content})
        return context

    def prompt(self, state, text):
        time_start_query = time.time()

        # Update history with user message
        self.messages_sit_customer.append(("user",  f"<{state}>" + text))

        initial_prompt = self.read_initial_prompt()
        context = self.build_incremental_prompt(initial_prompt, self.messages_sit_customer)
        try:
            # Create completion with Ollama
            response = ollama.chat(model='llama3', messages=context)
            # Assume 'response' has a valid 'message' key
            response = response['message']['content']
            
            
            # Handling response content
            if "|" in response:
                tag,content = response.split("|")
                if "finished" in tag.replace(" ", ""):
                    time_query = time.time() - time_start_query
                    print("Finished")
                    return content, time_query
                else:
                    time_query = time.time() - time_start_query
                    return content, time_query
            elif "finished>" in response:
                time_query = time.time() - time_start_query
                print("Finished")
                return content, time_query
            else:
                content = response
                time_query = time.time() - time_start_query
                return content, time_query

        except Exception as e:
            print(f"Exception occurred: {e}")
            return "[Error] Exception in processing response", 0

def test_query_time(num_queries=3):
    logger = RunLogger("desktop")
    time_total = 0
    queries_text = ["start | ", "reply | Which is the most fresh dish?", "reply | What do you suggest me", "reply | I will take a salad then"]

    for i in range(num_queries):
        chatbot = ChatBot()
        time_start = time.time()
        for j in queries_text:
            state, text = j.split("|")
            chat_completion, time_query = chatbot.prompt(state, text)
            print(f"Response> {chat_completion}")
            print(f"Time for query {j}: {time_query}\n")

            logger.log_query(state, text, time_query, chat_completion)
        
        time_total += time.time() - time_start

    print(f"[++] AVG Total time for queries: {time_total/(num_queries*len(queries_text))}")

if __name__ == "__main__":
    test_query_time(21)
