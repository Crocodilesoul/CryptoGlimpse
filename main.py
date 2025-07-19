# main.py
import requests
import time
from datetime import datetime

API_URL = "https://api.blockchair.com/bitcoin/transactions?q=value_usd(>,1000000)"
CHECK_INTERVAL = 300  # Проверка каждые 5 минут
LOG_FILE = "log.txt"

def get_large_transactions():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        return data.get("data", [])
    except Exception as e:
        log(f"[ERROR] Failed to fetch transactions: {e}")
        return []

def log(message):
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")
    print(f"[{timestamp}] {message}")

def summarize_transactions(txns):
    summary = []
    for tx in txns:
        tx_hash = tx.get("hash")
        value_usd = tx.get("value_usd")
        if tx_hash and value_usd:
            summary.append(f"TX {tx_hash[:10]}... — ${value_usd:,.0f}")
    return summary

if __name__ == "__main__":
    log("🚀 CryptoGlimpse started.")
    while True:
        txns = get_large_transactions()
        if txns:
            summary = summarize_transactions(txns)
            for line in summary:
                log(f"[ALERT] {line}")
        else:
            log("No large transactions found.")
        time.sleep(CHECK_INTERVAL)
