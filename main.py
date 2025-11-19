
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_game_info(appid):
    url = f"https://store.steampowered.com/api/appdetails?appids={appid}&cc=pt&l=pt"
    response = requests.get(url)
    data = response.json()

    if not data[str(appid)]["success"]:
        return None

    game_data = data[str(appid)]["data"]
    price = game_data.get("price_overview")

    return {
        "id": appid,
        "name": game_data.get("name"),
        "price": price["final"] / 100 if price else 0,
        "currency": price["currency"] if price else "FREE",
        "date_checked": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

@app.post("/check-prices")
async def check_prices(payload: dict):
    ids = payload.get("ids", [])
    results = []

    for appid in ids:
        info = get_game_info(appid)
        if info:
            results.append(info)

    return {"results": results}
