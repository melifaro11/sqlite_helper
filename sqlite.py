import sqlite3


class SQLiteException(Exception):
	pass


class SQLite():
    ''' Class to working with SQLite databases '''
    def __init__(self, dbfile):
        ''' Initialize SQLite()

            Keyword arguments:
                dbfile -- Name of the SQLite database file
        '''
        self.__dbfile = dbfile

    def __enter__(self):
        ''' Open database connection '''
        try:
            self.__conn = sqlite3.connect(self.__dbfile)
            self.__cursor = self.__conn.cursor()
        except Exception as e:
			raise SQLiteException(f'Error by opening SQLite database: {e}')

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        ''' Close database connection '''
        self.__conn.close()

    def __create_select_statement(self, table_name, fields):
        ''' Create "SELECT field1, field2, field3 FROM table"-Statement from
        fields list '''
        query = 'SELECT '
        for idx, field in enumerate(fields):
            if idx == 0:
                query += f'"{field}"'
            else:
                query += f', "{field}"'

        query += f' FROM "{table_name}" '

        return query

    def __create_where_statement(self, where):
        ''' Create "WHERE"-Statement from "where"-dictionary '''
        query = 'WHERE ';
        for idx, param in enumerate(where.keys()):
            value = where[param]

            if idx == 0:
                query += f'"{param}" = "{value}"'
            else:
                query += f' AND "{param}" = "{value}"'

        return query

    def select(self, table_name, fields=None, where=None, orderby=None, groupby=None):
        ''' Select records from table

            Keyword arguments:
                table_name -- Name of the table to select
                fields -- List of fields to select
                where -- dictionary with fields and values to filter request
        '''
        try:
            if fields is None:
                self.__cursor.execute(f'PRAGMA table_info("{table_name}")')
                fields = [entry[1] for entry in self.__cursor.fetchall()]

            query = self.__create_select_statement(table_name, fields)

            if where is not None:
                query += self.__create_where_statement(where)

            if orderby is not None:
                query += f' ORDER BY {orderby}'

            if groupby is not None:
                query += f' GROUP BY {groupby}'

            self.__cursor.execute(query)

            db_result = self.__cursor.fetchall();

            result = []
            for db_entry in db_result:
                entry = {}
                for idx, field in enumerate(fields):
                    entry[field] = db_entry[idx]
                result.append(entry)

            return result
        except Exception as e:
            raise SQLiteException(f'Database exception: {e}')

    def insert(self, table_name, values):
        try:
            query = f'INSERT INTO {table_name}('
            insert_values = '';
            for idx, param in enumerate(values.keys()):
                value = values[param]
                if idx == 0:
                    query += f'"{param}"'
                    insert_values += f'"{value}"'
                else:
                    query += f', "{param}"'
                    insert_values += f', "{value}"'

            query += f') VALUES ({insert_values})'

            self.__cursor.execute(query)
            self.__conn.commit()

            return self.__cursor.lastrowid
        except Exception as e:
            raise SQLiteException(f'Database exception: {e}')

    def update(self, table_name, values, where=None):
        ''' Update table from a dictonary values '''
        try:
            query = f'UPDATE "{table_name}" SET '

            for idx, param in enumerate(values.keys()):
                value = values[param]
                if idx == 0:
                    query += f'"{param}" = "{value}"'
                else:
                    query += f', "{param}" = "{value}"'

            if where is not None:
                query += ' ' + self.__create_where_statement(where)

            self.__cursor.executescript(query)
        except Exception as e:
            raise SQLiteException(f'Database exception: {e}')

    def delete(self, table_name, where=None):
        ''' Delete record(s) from table '''
        try:
            query = f'DELETE FROM "{table_name}" ';

            if where is not None:
                query += self.__create_where_statement(where)

            self.__cursor.executescript(query)
        except Exception as e:
            raise SQLiteException(f'Database exception: {e}')

    def custom_select(self, query, commit=False):
        ''' Perforum custom SELECT-request '''
        try:
            self.__cursor.executescript(query)
            if commit:
                self.__conn.commit()
        except Exception as e:
            raise SQLiteException(f'Database exception: {e}')

    def start_transaction(self):
        self.__cursor.execute('BEGIN TRANSACTION')

    def commit_transaction(self):
        self.__cursor.execute('COMMIT')

    def rollback_transaction(self):
        self.__cursor.execute('ROLLBACK')
