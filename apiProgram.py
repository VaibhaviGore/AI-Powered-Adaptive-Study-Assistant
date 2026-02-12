import os
from dotenv import load_dotenv

# This function looks for the file named ".env" and loads the variables
load_dotenv()

# Now you pull the specific variable by its name
my_key = os.getenv("GEMINI_API_KEY")
data_path = os.getenv("STUDY_DATA_FILE")

print(f"I am using the key: {my_key[:5]}...")  