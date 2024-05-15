import pypyodbc as adbc

driver_name = 'SQL SERVER'
server_name = 'DESKTOP-B2IG1G0\\SQLEXPRESS'
database_name = 'DB'

conn_str = f"""
     DRIVER={{{driver_name}}};
     SERVER={server_name};
     DATABASE={database_name};
     Trusted_Connection=yes;
"""

connection = adbc.connect(conn_str)

loginExist = """
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('logevent'))
    SELECT 0 AS TableExists
ELSE
    SELECT 1 AS TableExists
"""

cursor = connection.cursor()
cursor.execute(loginExist)
login = cursor.fetchone()[0]

if not login:
    LoginTable = """
    CREATE TABLE logevent (
        id INT IDENTITY PRIMARY KEY,
        nom VARCHAR(50),
        mpass VARCHAR(16),
        photo VARCHAR(500)
    )
    """
    cursor.execute(LoginTable)

EventExist = """
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('event'))
    SELECT 0 AS TableExists
ELSE
    SELECT 1 AS TableExists
"""

cursor = connection.cursor()
cursor.execute(EventExist)
event = cursor.fetchone()[0]

if not event:
    EventTable = """
    CREATE TABLE event (
        id INT IDENTITY PRIMARY KEY,
        titre VARCHAR(50),
        description VARCHAR(600),
        jour VARCHAR(50),
        heur VARCHAR(50),
        date DATE,
        annonce VARCHAR(100),
        capaciter INT, 
        prix FLOAT
)
    """
    cursor.execute(EventTable)

ParticipentExist = """
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('participent'))
    SELECT 0 AS TableExists
ELSE
    SELECT 1 AS TableExists
"""

cursor = connection.cursor()
cursor.execute(ParticipentExist)
Participent = cursor.fetchone()[0]

if not Participent:
    ParticipentTable = """
    CREATE TABLE participent (
        id INT IDENTITY PRIMARY KEY,
        photo VARCHAR(200),
        cin VARCHAR(50) UNIQUE,
        nom VARCHAR(50),
        email VARCHAR(600),
        fonction VARCHAR(100),
        heurArrive VARCHAR(100),
        heurDepart VARCHAR(100),
        durre VARCHAR(100)
    )
    """
    cursor.execute(ParticipentTable)

visiteurExist = """
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('visiteur'))
    SELECT 0 AS TableExists
ELSE
    SELECT 1 AS TableExists
"""

cursor = connection.cursor()
cursor.execute(visiteurExist)
visiteur = cursor.fetchone()[0]

if not visiteur:
    visiteurTable = """
    CREATE TABLE visiteur (
        id INT IDENTITY PRIMARY KEY,
        photo VARCHAR(200),
        cin VARCHAR(50) UNIQUE,
        nom VARCHAR(50),
        email VARCHAR(600),
        event_id INT,
        CONSTRAINT FK_id FOREIGN KEY (event_id) REFERENCES event(id)
    )
    """
    cursor.execute(visiteurTable)

connection.commit()
