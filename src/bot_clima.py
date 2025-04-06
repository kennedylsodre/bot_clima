#%%
from twilio.rest import Client
from dotenv import load_dotenv 
import os
from pathlib import Path
# %%

env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=env_path,override=True)

#%%
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_=os.getenv('FROM_NUMBER'),
  body = "Testando mensagem",
  to=os.getenv('TO_NUMBER_1')
)

print("Status:", message.status)
print("SID:", message.sid)

# %%
