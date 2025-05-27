from fastapi import FastAPI, BackgroundTasks
from . import crud, scheduler, models

app = FastAPI(title="Inventario & PO Service")

#Endpoint manual para forzar generación de POs
@app.post("/orders/generate")
async def generate_orders(bg: BackgroundTasks):
    bg.add_task(crud.generate_purchase_orders)
    return {"status": "Ordenes encoladas"}

#Endpoint para consultar estado actual
@app.get("/inventory/status", response_model=list[models.InventoryStatus])
async def get_inventory_status():
    return crud.list_inventory_status()

#Endpoint para listar alertas
@app.get("/alerts", response_model=list[models.Alert])
async def get_alerts():
    return crud.list_alerts()

#Arranco el scheduler al iniciar
@app.on_event("startup")
def start_scheduler():
    scheduler.start_periodic_checks()
