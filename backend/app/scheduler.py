from apscheduler.schedulers.asyncio import AsyncIOScheduler
from .crud import generate_purchase_orders, trigger_alerts

sched = AsyncIOScheduler()

def start_periodic_checks():
    #Cada día a las 8am: revisar stock y generar PO
    sched.add_job(generate_purchase_orders, "cron", hour=8)
    #Cada hora: disparar alertas si Diff supera umbrales
    sched.add_job(trigger_alerts, "interval", hours=1)
    sched.start()
