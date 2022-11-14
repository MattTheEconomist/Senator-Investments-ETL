import psycopg2

hostname='localhost'
database='senator'
username='postgres'
pwd='admin'
port_id=5432

conn=None
cur=None 

try: 
    conn = psycopg2.connect(
        host=hostname,
        dbname=database, 
        user=username, 
        password = pwd,
        port = port_id
    )

    cur = conn.cursor()


    create_script = '''
    CREATE TABLE IF NOT EXISTS transactions(
        id                  int PRIMARY KEY,
        transaction_date    VARCHAR(50),
        owner               VARCHAR(50),
        asset_description   VARCHAR(250),
        asset_type          VARCHAR(50),
        type                VARCHAR(50),
        amount              VARCHAR(50),
        comment             VARCHAR(250),
        senator             VARCHAR(50),
        ptr_link            VARCHAR(150),
        disclosure_date     VARCHAR(50)
    )
    '''

    cur.execute(create_script)
    
    conn.commit()
    


except Exception as err:
    print(err)
finally: 
    if cur is not None: 
        cur.close()
    if conn is not None: 
        conn.close()






