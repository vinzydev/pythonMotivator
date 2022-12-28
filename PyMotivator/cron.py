from apscheduler.schedulers.background import BackgroundScheduler
from motivator import send_whatsapp_text,client,quote

scheduler = BackgroundScheduler(timezone="Asia/Kolkata")
scheduler.start()

job = scheduler.add_job(send_whatsapp_text,'cron',[client,quote],hour="11",minute="31")
print(job)

while True:
    time.sleep(5)
    