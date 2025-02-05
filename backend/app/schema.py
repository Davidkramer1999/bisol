from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import datetime


class EnergyQuery(BaseModel):
    customer: str
    start_time: datetime
    end_time: datetime


class EnergyRecord(BaseModel):
    timestamp_utc: datetime
    sipx_eur_kwh: float
    consumption_kwh: Optional[float]
    production_kwh: Optional[float]

    model_config = ConfigDict(from_attributes=True)


class EnergyDataResponse(BaseModel):
    status_code: int
    message: str
    data: Optional[List[EnergyRecord]]


class EnergyCalculationResponse(BaseModel):
    status_code: int
    message: str
    data: Optional[dict]
