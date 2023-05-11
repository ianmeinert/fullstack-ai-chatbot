import uuid
from datetime import datetime
from pydantic import BaseModel


class Message(BaseModel):
    id = str(uuid.uuid4())
    msg: str
    timestamp = str(datetime.now())
