from .models import Inventory, PurchaseOrder, Alert
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

def generate_purchase_orders():
    db: Session = get_db()
    statuses = db.query(Inventory).all()
    for inv in statuses:
        if inv.diff < 0:
            qty = abs(inv.diff)
            po = PurchaseOrder(
                producto=inv.producto,
                cantidad=qty,
                fecha_generada=datetime.utcnow()
            )
            db.add(po)
    db.commit()

def trigger_alerts():
    db: Session = get_db()
    low_stock = db.query(Inventory).filter(Inventory.diff < -threshold).all()
    for inv in low_stock:
        alert = Alert(
            producto=inv.producto,
            mensaje=f"Stock crítico: faltan {abs(inv.diff)} unidades",
            fecha=datetime.utcnow()
        )
        db.add(alert)
        #enviar correo
        send_email_or_slack(alert.mensaje)
    db.commit()
