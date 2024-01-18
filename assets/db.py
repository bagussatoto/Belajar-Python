import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="belajar-python",
    user="postgres",
    password="postgres",
)


# id serial
# todo varchar
# is_done boolean
