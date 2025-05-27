# QPH – Inventario & Forecast de Ventas

Este repositorio contiene:

- **backend/** – Servicio FastAPI para:
  - Forecast de ventas Q4 con Prophet
  - Análisis de inventario vs. demanda
  - Generación automática de Órdenes de Compra (cron)
  - Trigger de Alertas (stock crítico)
- **frontend/** – Dashboard React + Vite para visualizar:
  - Estado de inventario vs. estimado
  - Órdenes de Compra y Alertas
- **notebooks/** – PoC en Google Colab:
  - `consumer_sales_analysis_inventory_projection.ipynb`
- **data/** – Datos de entrada:
  - `Ventas e inventarios juguetes.xlsx`
- **output/** – Salidas del notebook:
  - `forecast_q4_2024.csv`
  - `inventory_analysis_2024.csv`

---

## Requisitos

- Python 3.9+
- Node.js 16+ / Yarn 1+
- PostgreSQL (u otra BD relacional)

---

## Instalación

1. **Backend**

   ```bash
   cd backend
   python -m venv .venv
   source .venv/bin/activate      # Unix/macOS
   .venv\Scripts\activate         # Windows
   pip install -r ../requirements.txt




# Uso
## Iniciar Backend

cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
Iniciar Frontend

## Iniciar frontend
cd frontend
npm run dev

# Notebook Colab

Abre notebooks/consumer_sales_analysis_inventory_projection.ipynb en Google Colab

Ejecuta las celdas de 1 a 11 para cargar datos, generar forecast, analizar inventario y ver el resumen final

# Endpoints principales (FastAPI)
GET /inventory/status → Estado actual de inventario vs. estimado

GET /alerts  Listado de alertas de stock crítico

POST /orders/generate → Forzar generación de Órdenes de Compra

# Arquitectura

QPH/
├─ backend/     FastAPI + SQLModel + APScheduler
├─ frontend/    React + Vite O NEXT.JS + shadcn/ui
├─ notebooks/   PoC y análisis en Colab
├─ data/        Datos de ventas e inventario
├─ output/      cSVs generados por el notebook
├─ requirements.txt
└─ README.md
# Contribuir
Haz un fork
Crea tu feature branch (git checkout -b feature/x)
Commit y push
Abre un Pull Request

# Licencia
MIT © 2025 Isaac Reyes





# A FUTURO - ESCALABLE
1. Integrar alertas automáticas (ej Slack/email Google- outlook M365) cuando el stock proyectado caiga por debajo de umbrales definidos.
2. DASHBOARD EN REACT.JS NEXT.JS Y desplegar en Vercel