import requests
from pymongo import MongoClient

class PriceAlertManager:
    def __init__(self, mongo_uri="mongodb://localhost:27017",
                 db_name="price_alert_bot", collection_name="alerts"):
        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def add_price_alert(self, chat_id: int, coin_name: str, target_price: float):
        self.collection.update_one(
            {"chat_id": chat_id, "coin_name": coin_name.lower()},
            {"$set": {"target_price": target_price}},
            upsert=True
        )

    def get_all_alerts(self):
        return list(self.collection.find())

    def remove_alert(self, alert_id):
        self.collection.delete_one({"_id": alert_id})

    def get_coin_price(self, coin_name: str) -> float | None:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_name.lower()}&vs_currencies=usd"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            return data.get(coin_name.lower(), {}).get("usd")
        except Exception as e:
            print(f"Error fetching price for {coin_name}: {e}")
            return None

    async def check_alerts(self):
        triggered = []
        alerts = self.get_all_alerts()

        for alert in alerts:
            coin_name = alert["coin_name"]
            target_price = alert["target_price"]
            chat_id = alert["chat_id"]
            current_price = self.get_coin_price(coin_name)
            if current_price is None:
                continue

            if current_price <= target_price:
                triggered.append({
                    "chat_id": chat_id,
                    "coin_name": coin_name,
                    "current_price": current_price,
                    "target_price": target_price,
                    "alert_id": alert["_id"]
                })

        return triggered

    def clear_alert(self, alert_id):
        self.remove_alert(alert_id)
