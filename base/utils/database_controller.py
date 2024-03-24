import pymysql

from base.utils.settings.settings_keys import SettingsKeys, Settings


def connect():
    return pymysql.connect(host=SettingsKeys.DB_HOST,
                           user=SettingsKeys.DB_USER,
                           password=SettingsKeys.DB_PASSWORD,
                           database=SettingsKeys.DB_DATABASE)


class Database:
    def __init__(self):
        self.settings = Settings()


class DataBaseController(Database):
    def __init__(self):
        Database.__init__(self)

    @staticmethod
    def insert_data(test_name="", test_path="", test_trace="", test_status="", test_duration=""):
        db = connect()
        cursor = db.cursor()
        query = ("INSERT INTO insiderDB.test_results (test_name, test_path, test_trace, test_status, test_duration) "
                 "VALUES (%s, %s, %s, %s, %s)")
        cursor.execute(query, (test_name, test_path, test_trace, test_status, test_duration))
        db.commit()
        db.close()

