import sqlite3

class DBManager(object):
    def __init__(self, path):
        self.dbPath = path
    