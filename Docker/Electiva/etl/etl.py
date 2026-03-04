import psycopg2
import time
import csv

conn = psycopg2.connect(
    host="coordinator",
    dbname="factory",
    user="admin",
    password="admin",
    port=5432
)

cur = conn.cursor()

while True:
    cur.execute("""
        SELECT EXISTS (
            SELECT 1 
            FROM information_schema.tables 
            WHERE table_name = 'factory_sensors'
        );
    """)
    exists = cur.fetchone()[0]

    if exists:
        print("La tabla factory_sensors ya existe. Iniciando ETL...")
        break

    print("Esperando a que exista la tabla factory_sensors...")
    time.sleep(2)

cycle = 0

while True:
    cycle += 1

    cur.execute("SELECT * FROM factory_sensors;")
    rows = cur.fetchall()
    col_names = [desc[0] for desc in cur.description]

    cleaned_rows = []

    machine_id_index = col_names.index("machine_id")
    installation_year_index = col_names.index("installation_year")

    for row in rows:
        machine_id = row[machine_id_index]
        installation_year = row[installation_year_index]

        if machine_id is None or str(machine_id).strip() == "":
            continue

        if installation_year is not None and installation_year > 2025:
            continue

        cleaned_rows.append(row)

    if cycle == 10:
        print("Generando reporte ETL para Power BI...")

        with open("/app/powerbi_data.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(col_names)
            writer.writerows(cleaned_rows)

        print("Reporte actualizado: powerbi_data.csv")
        cycle = 0

    time.sleep(2)

