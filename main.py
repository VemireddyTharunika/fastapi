from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# For Swagger UI Testing
class Message(BaseModel):
    text: Optional[str] = ""

class ChatPayload(BaseModel):
    message: Optional[Message] = None

@app.post("/gchat-endpoint")
async def gchat_webhook(payload: ChatPayload):
    message = payload.message.text.lower() if payload.message else ""

    if "hi" in message:
        reply = "How are you?"
    else:
        reply = f"You said: {message}"

    return JSONResponse(content={"text": reply})
