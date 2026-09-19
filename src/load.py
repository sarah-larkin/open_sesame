from config import DB_PATH
import sqlite3

def load_to_db(data):
    conn = sqlite3.connect(DB_PATH)