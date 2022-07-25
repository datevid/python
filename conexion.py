import psycopg2


# def getCredetials(host :str ,port :int ,database :str ,user :str ,password :str):
def getCredetials():
    # Establish a connection to the database by creating a cursor object
    # The PostgreSQL server must be accessed through the PostgreSQL APP or Terminal Shell

    # conn = psycopg2.connect("dbname=suppliers port=5432 user=postgres password=postgres")

    # Or:
    connConfig = {
        'host': "yourHost",
        'port': 5432,
        'database': 'yourDB',
        'user': 'yourUser',
        'password': 'yourPass',
    };
    return connConfig;


def getData(connConfig):
    # Establish a connection to the database by creating a cursor object
    # The PostgreSQL server must be accessed through the PostgreSQL APP or Terminal Shell

    # conn = psycopg2.connect("dbname=suppliers port=5432 user=postgres password=postgres")

    # Or:
    conn = psycopg2.connect(host=connConfig['host'], port=connConfig['port'],
                            database=connConfig['database'],
                            user=connConfig['user'], password=connConfig['password']);

    # Create a cursor object
    cur = conn.cursor()

    # A sample query of all data from the "vendors" table in the "suppliers" database
    cur.execute("""select * from ceadm.persona
    where id = 7112 ;
    """)
    query_results = cur.fetchall()
    print(query_results)
    print(type(query_results))

    # Close the cursor and connection to so the server can allocate
    # bandwidth to other requests
    cur.close()
    conn.close()


credentials = getCredetials();
getData(credentials)
