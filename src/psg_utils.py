import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect(
    host='127.0.0.1',
    port=5432,
    dbname='uscis',
    user='uscis',
    password='1234'
)


def update_case_status(cols, data, primary_keys=('case_no', 'update_date')):
    cusor = conn.cursor()

    insert_sql = """
    INSERT INTO 
    case_status ({}) VALUES ({})
    ON CONFLICT ({}) DO UPDATE 
        SET {}
    """.format(
        ', '.join(cols),
        ', '.join(['%s' for i in range(len(cols))]),
        ', '.join(primary_keys),
        ', '.join(["{} = %s".format(col) 
                   for col in cols if col not in primary_keys])
    )
    
    cusor.execute(
        insert_sql, 
        [data.get(col) for col in cols] + \
            [data.get(col) for col in cols if col not in primary_keys]
    )
    conn.commit()
