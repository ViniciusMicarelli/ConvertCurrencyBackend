
from . import cotacao_router
from fastapi import status, HTTPException
from ..schemas import QuoteMap
import requests

BASE_API_URL = "https://economia.awesomeapi.com.br/json/last/"

@cotacao_router.get("/to-bra", status_code=status.HTTP_200_OK, response_model=QuoteMap)
def get_cotacao():
    
    try:
        resp = requests.get(f"{BASE_API_URL}THB-BRL", timeout=(3, 10))
        resp.raise_for_status()
        return resp.json()

    except requests.exceptions.Timeout:
        raise HTTPException(status_code=504, detail="Timeout consultando API de cotação")
    
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=502, detail=f"Erro ao consultar API de cotação: {e}")


@cotacao_router.get("/to-thai", status_code=status.HTTP_200_OK, response_model=QuoteMap)
def get_cotacao():
    
    try:
        resp = requests.get(f"{BASE_API_URL}BRL-THB", timeout=(3, 10))
        resp.raise_for_status()
        return resp.json()

    except requests.exceptions.Timeout:
        raise HTTPException(status_code=504, detail="Timeout consultando API de cotação")
    
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=502, detail=f"Erro ao consultar API de cotação: {e}")
