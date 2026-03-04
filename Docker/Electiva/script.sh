#!/bin/bash
set -e 

echo "📌 Creando base de datos 'factory' en los workers..."
docker exec -it worker1 psql -U admin -d postgres -c "CREATE DATABASE factory;"
docker exec -it worker2 psql -U admin -d postgres -c "CREATE DATABASE factory;"

echo "📌 Habilitando extensión CITUS en ambos workers..."
docker exec -it worker1 psql -U admin -d factory -c "CREATE EXTENSION IF NOT EXISTS citus;"
docker exec -it worker2 psql -U admin -d factory -c "CREATE EXTENSION IF NOT EXISTS citus;"

echo "📌 Agregando nodos al coordinador..."
docker exec -it coordinator psql -U admin -d factory -c "SELECT * FROM master_add_node('worker1', 5432);"
docker exec -it coordinator psql -U admin -d factory -c "SELECT * FROM master_add_node('worker2', 5432);"

echo "📌 Consultando nodos activos..."
docker exec -it coordinator psql -U admin -d factory -c "SELECT * FROM citus_get_active_worker_nodes();"

echo "📌 Creando tabla distribuible factory_sensors en el coordinador..."
docker exec -it coordinator psql -U admin -d factory -c "
CREATE TABLE IF NOT EXISTS factory_sensors (
    Machine_ID TEXT,
    Machine_Type TEXT,
    Installation_Year INT,
    Production_Capacity_T FLOAT,
    Temperature_C FLOAT,
    Vibration_mms FLOAT,
    Sound_dB FLOAT,
    Oil_Level_pct FLOAT,
    Counter_Cycles FLOAT,
    Power_Consumption_kW FLOAT,
    Last_Maintenance_Days_Ago INT,
    Maintenance_History_Count INT,
    Failure_History_Count INT,
    AI_Supervision BOOLEAN,
    Error_Codes_Last_30_Days INT,
    Unplanned_Stops_Last_Month FLOAT,
    Failure_Within_7_Days BOOLEAN,
    Laser_Intensity FLOAT,
    Hydraulic_Pressure_bar FLOAT,
    Coolant_Flow_L_min FLOAT,
    Heat_Index FLOAT,
    AI_Override_Events INT
);
"

echo "📌 Marcando la tabla como distribuida..."
docker exec -it coordinator psql -U admin -d factory -c "
SELECT create_distributed_table('factory_sensors', 'machine_id');
"

echo "📌 Copiando CSV al coordinator..."
docker cp factory_sensor_simulator_2040.csv coordinator:/tmp/factory_sensor_simulator_2040.csv

echo "📌 Cargando datos desde CSV a la tabla distribuida..."
docker exec -it coordinator psql -U admin -d factory -c "\copy factory_sensors FROM '/tmp/factory_sensor_simulator_2040.csv' CSV HEADER;"

echo "✅ Todo listo. Citus configurado, tabla creada y datos cargados correctamente."

