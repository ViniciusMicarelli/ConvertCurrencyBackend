from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pathlib import Path
import pkgutil
import importlib
from fastapi.openapi.utils import get_openapi
import os


app = FastAPI(title="Portal Qualiconsig")

routers = []

APPS_DIR = os.path.join(os.path.dirname(__file__), 'app')

EXCLUDED_MODULES = ['clients', '__pycache__', 'databases', 'beneficio', 'clientes', 'cidades']

modules = []

for name in os.listdir(APPS_DIR):
    mod_path = os.path.join(APPS_DIR, name)

    if (os.path.isdir(mod_path) and name not in EXCLUDED_MODULES):
        modules.append(name)



for mod_name in modules:
    try:
        module_path = f"app.{mod_name}"
        module = importlib.import_module(module_path)

        if hasattr(module, "routers"):
            for router in getattr(module, "routers"):
                app.include_router(router)
            print(f"✔️ Routers importados de {module_path}")
        else:
            print(f"⚠️ Módulo {module_path} não possui 'routers'")
    except Exception as e:
        print(f"❌ Erro ao importar {mod_name}: {e}")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)