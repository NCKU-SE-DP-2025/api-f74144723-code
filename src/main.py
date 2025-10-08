from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/api/v1/me")
def me():
    return {"name": "張寶嘉", "student_id": "F74144723"}

@app.get("/api/v1/rectangle-area")
def rectangle_area(width : int, height : int):
    return width*height

class WordsRequest(BaseModel):
    words: list[str]

@app.post("/api/v1/word-length-calculator")
def calculate_word_lengths(request: WordsRequest):
    result = [
        {"word": word, "length": len(word)}
        for word in request.words
    ]
    return result
