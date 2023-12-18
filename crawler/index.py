from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import uvicorn
import threading
import crawler


scheduler = BackgroundScheduler()
app = FastAPI()


@app.post("/crawl")
def crawl_func(phone_page: int = 0, laptop_page: int = 0, tablet_page: int = 0):
    return crawler.crawl(phone_page, laptop_page, tablet_page)


if __name__ == "__main__":
    # Thêm công việc vào scheduler
    scheduler.add_job(crawler.crawl, trigger=CronTrigger(
        minute='*'), args=[1, 1, 1])

    # Khởi động config cào hàng phút
    scheduler_thread = threading.Thread(target=scheduler.start)
    scheduler_thread.start()

    # Chạy FastAPI
    uvicorn.run(app, host="0.0.0.0", port=8000)
