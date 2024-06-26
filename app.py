from typing import Annotated
import json
import random

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel

# Description for the docs
DESCRIPTION = """
This API provides a collection of hilarious programming memes to lighten up your coding sessions.

## Api
You can tailor the humor to fit your preferences by filtering memes based on dimensions.
You can select the:
* **max_width**: between 193 to 2560.
* **min_width**: between 193 to 2560.
* **max_height**: between 101 to 2560.
* **min_height**: between 101 to 2560.
"""

#Summary for the docs
SUMMARY = """
Whether you're integrating memes into your application or just browsing for a chuckle, this API provides an entertaining solution for programmers of all levels.
"""

app = FastAPI(
    title="Programming Meme API",
    description=DESCRIPTION,
    summary=SUMMARY,
    version="0.0.1",
    contact={
        "name": "Lakhindar Pal",
        "url": "https://lakhindar.is-a-good.dev"
    },
    license_info={
        "name": "MIT",
        "url": "https://github.com/LakhindarPal/programming-meme-api/blob/main/LICENSE",
        "identifier": "MIT"
    }
)

# Response model
class Meme(BaseModel):
    id: str
    url: str
    width: int
    height: int

# Base URL for memes
CDN_BASE = "https://raw.githubusercontent.com/deep5050/programming-memes/main"

# Load memes from a local JSON file
try:
    with open("data.json", "r", encoding="utf-8") as file:
        memes = json.load(file)
except FileNotFoundError as exc:
    raise Exception("Memes file not found. Please make sure 'memes.json' exists in the specified directory.") from exc
except json.JSONDecodeError as exc:
    raise Exception("Error parsing JSON. Please check if 'memes.json' contains valid JSON data.") from exc

# Test route 
@app.get("/")
async def root():
    return {"message": "Hello World"}

#  route
@app.get("/api")
async def random_meme(
    max_width: Annotated[int | None, Query(ge=193, le=2560)] = None,
    min_width: Annotated[int | None, Query(ge=193, le=2560)] = None,
    max_height: Annotated[int | None, Query(ge=101, le=2560)] = None,
    min_height: Annotated[int | None, Query(ge=101, le=2560)] = None
) -> Meme:
    filtered_memes = [meme for meme in memes
                      if (max_width is None or meme["width"] <= max_width)
                      and (min_width is None or meme["width"] >= min_width)
                      and (max_height is None or meme["height"] <= max_height)
                      and (min_height is None or meme["height"] >= min_height)]

    if not filtered_memes:
        raise HTTPException(status_code=404, detail="No meme is found matching the criteria.")

    random_meme = random.choice(filtered_memes)
    return Meme(
        id=random_meme["id"],
        url=f"{CDN_BASE}/{random_meme['path']}",
        width=random_meme["width"],
        height=random_meme["height"]
    )
