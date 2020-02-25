import PostgresqlManager



if __name__ == '__main__':
    PostgresqlManager.get_connection_by_config(PostgresqlManager, 'database.ini', 'postgresql_conn_data')
    cur = PostgresqlManager._conn.cursor()

    # example of creating table after successful connection
    cur.execute('''CREATE TABLE passenger (
    code        char(5) CONSTRAINT firstkey PRIMARY KEY,
    title       varchar(40) NOT NULL,
    did         integer NOT NULL,
    date_prod   date,
    kind        varchar(10),
    len         interval hour to minute
);''')

    cur.close()
    PostgresqlManager._conn.commit()
