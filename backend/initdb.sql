 
CREATE TABLE energy_data (
    id SERIAL PRIMARY KEY,   
    timestamp_utc TIMESTAMPTZ NOT NULL,
    sipx_eur_kwh NUMERIC(10, 5),
    customer VARCHAR(55),  
    consumption_kwh NUMERIC(10, 3),
    production_kwh NUMERIC(10, 3)
);


-- Load Data from CSV  
COPY energy_data(timestamp_utc, sipx_eur_kwh, customer, consumption_kwh, production_kwh)
FROM '/docker-entrypoint-initdb.d/data.csv'
WITH (FORMAT csv, HEADER, DELIMITER ',');
