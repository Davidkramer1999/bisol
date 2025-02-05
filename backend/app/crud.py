from sqlalchemy.orm import Session
from . import models, schema


def get_energy_data_by_customer(
    db: Session, customer: str, start_time, end_time
) -> schema.EnergyDataResponse:
    """
    Fetch energy data for a given customer (by name) within a time range.
    """
    query = (
        db.query(models.EnergyData)
        .filter(
            models.EnergyData.customer == customer,
            models.EnergyData.timestamp_utc >= start_time,
            models.EnergyData.timestamp_utc <= end_time,
        )
        .all()
    )

    if not query:
        return schema.EnergyDataResponse(
            status_code=404,
            message=f"No energy data found for {customer} in the given time range.",
            data=None,
        )

    return schema.EnergyDataResponse(
        status_code=200,
        message="Energy data retrieved successfully.",
        data=query,
    )


def calculate_costs_revenues(
    db: Session, customer: str, start_time, end_time
) -> schema.EnergyCalculationResponse:
    """
    Compute total cost and revenue for a given customer in a given time range.
    """
    query = db.query(models.EnergyData).filter(
        models.EnergyData.customer == customer,
        models.EnergyData.timestamp_utc >= start_time,
        models.EnergyData.timestamp_utc <= end_time,
    )

    results = query.all()

    if not results:
        return schema.EnergyCalculationResponse(
            status_code=404,
            message=f"No energy data available for {customer}.",
            data={"customer": customer, "total_cost": 0.0, "total_revenue": 0.0},
        )

    total_cost = sum(row.sipx_eur_kwh * (row.consumption_kwh or 0) for row in results)
    total_revenue = sum(row.sipx_eur_kwh * (row.production_kwh or 0) for row in results)

    return schema.EnergyCalculationResponse(
        status_code=200,
        message="Calculation successful.",
        data={
            "customer": customer,
            "total_cost": total_cost,
            "total_revenue": total_revenue,
        },
    )
