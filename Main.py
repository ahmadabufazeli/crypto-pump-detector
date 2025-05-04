import schedule
import time
from pump_detector import check_market_and_send_alerts

def run():
    print("Pump detector started.")
    schedule.every(10).minutes.do(check_market_and_send_alerts)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    run()
