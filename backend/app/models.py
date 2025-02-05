from .database import Base
from sqlalchemy import Column, String, Float, DateTime, Integer


class EnergyData(Base):
    __tablename__ = "energy_data"

    timestamp_utc = Column(DateTime, primary_key=True)
    sipx_eur_kwh = Column(Float, nullable=False)
    customer = Column(String, nullable=False)
    consumption_kwh = Column(Float)
    production_kwh = Column(Float)
