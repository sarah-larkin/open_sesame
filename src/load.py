from config import DB_PATH
import sqlite3


def load_table(df, table_name):
    conn = sqlite3.connect(DB_PATH)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()

