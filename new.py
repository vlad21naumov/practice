from dotenv import load_dotenv
import os

load_dotenv()

c = os.getenv('CONST')
print(c)