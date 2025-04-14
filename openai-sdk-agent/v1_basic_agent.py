from agents import Agent, Runner
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set the OPENAI_API_KEY from local environment variables
from agents import set_default_openai_key
set_default_openai_key(os.getenv('OPENAI_API_KEY'))

# Define agent
agent = Agent(
    name="Assistant", 
    instructions="You are a helpful assistant",
    model="gpt-4o-mini"
)

def main():
    result = Runner.run_sync(agent, "Write a haiku about recursion in programming.")
    print(result.final_output)

if __name__ == "__main__":
    main()


    