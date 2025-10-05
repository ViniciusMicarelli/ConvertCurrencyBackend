import pkgutil
import importlib
import pathlib

from fastapi import APIRouter


cotacao_router = APIRouter(
    prefix='/cotacao',
    tags=['Cotação']
)


package_dir = pathlib.Path(__file__).parent
for module_info in pkgutil.iter_modules([str(package_dir)]):
    if not module_info.name.startswith("_"):
        importlib.import_module(f"{__name__}.{module_info.name}")
