import unittest
from src.singleton.DatabaseConnection import DatabaseConnection

class TestDatabaseConnectionSingleton(unittest.TestCase):
    def test_singleton_instance(self):
        db1 = DatabaseConnection()
        db2 = DatabaseConnection()

        self.assertIs(db1, db2)
        self.assertEqual(db1.get_connection(), db2.get_connection())

if __name__ == '__main__':
    unittest.main()