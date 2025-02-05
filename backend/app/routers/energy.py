import logging
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies import get_db
from .. import crud, schema

router = APIRouter(prefix="/energy", tags=["Energy Data"])

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


@router.get("/user/{customer}", response_model=schema.EnergyDataResponse)
def get_energy_data_by_customer(
    customer: str, start_time: str, end_time: str, db: Session = Depends(get_db)
):
    """
    Fetch energy data for a given customer in a time range.
    """
    try:
        result = crud.get_energy_data_by_customer(db, customer, start_time, end_time)

        if result.status_code == 404:
            raise HTTPException(status_code=404, detail=result.message)

        return result
    except Exception as e:
        logger.error(f"Error fetching energy data for {customer}: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get(
    "/user/{customer}/calculate", response_model=schema.EnergyCalculationResponse
)
def calculate_costs_revenues(
    customer: str, start_time: str, end_time: str, db: Session = Depends(get_db)
):
    """
    Compute total cost and revenue for a given customer in a given time range.
    """
    try:
        result = crud.calculate_costs_revenues(db, customer, start_time, end_time)

        if result.status_code == 404:
            raise HTTPException(status_code=404, detail=result.message)

        return result

    except Exception as e:
        logger.error(f"Error calculating costs for {customer}: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
