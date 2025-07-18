# ---------------- main.py ----------------

import time
from utils import get_large_transactions, summarize_transactions
from alert import send_telegram_alert

CHECK_INTERVAL = 60  # seconds

if __name__ == "__main__":
    print("[main.ry] Monitoring large blockchain transactions...")
    while True:
        large_txns = get_large_transactions(min_value_usd=1_000_000)
        if large_txns:
            summary = summarize_transactions(large_txns)
            send_telegram_alert(summary)
        time.sleep(CHECK_INTERVAL)
# test commit from Fri Jul 18 17:12:33 UTC 2025
