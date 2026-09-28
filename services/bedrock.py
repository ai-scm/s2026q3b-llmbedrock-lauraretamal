import boto3
from dotenv import load_dotenv
from services.prompt import SYSTEM_PROMPT

load_dotenv()

MODEL_ID = "amazon.nova-pro-v1:0"

bedrock = boto3.client(
    "bedrock-runtime",
    region_name = "us-east-1"
)
