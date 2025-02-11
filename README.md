# Python SQLite Helper

SQL Helper is a small class that simplifies working with SQLite databases in Python.

## Installation

```bash
pip install pysqlite3
```

## Usage

### Create SQLite instance

```python
sqlite = SQLite('data.db')
```

### SELECT

The ```select()``` method of the SQLite instance is used to retrieve data from the database.

```python
def select(table_name, fields=None, where=None, orderby=None, groupby=None)
```

Here:

- ```table_name```: Name of the table.
- ```fields```: A list of fields to select. Use ```None``` to select all fields.
- ```where```: A dictionary for the WHERE clause, where the key is the field name and the value is the field value.
- ```orderby```: The field name used to sort results.
- ```groupby```: The field name used to group results.

**Example**

```python
with sqlite as db:
	results = db.select('users', fields=['id', 'login', 'password'], where={'username': 'john_smith'})
```

### INSERT

The ```insert()``` method of the SQLite instance is used to add a record to the database.

```python
def insert(table_name, values)
```

Here:
- ```table_name```: Name of the table.
- ```values```: A dictionary containing the values to add.

**Example**

```python
with sqlite as db:
	db.insert('users', {'login': 'john_smith', 'password': 'john_pass', 'first_name': 'John', 'last_name': 'Smith'})
```

### UPDATE

The ```update()``` method of the SQLite-instance is used to change a record in a table.

```python
update(table_name, values, where=None)
```

Here:
- ```table_name```: Name of the table.
- ```values```: A dictionary with fields and values to update.
- ```where```: A dictionary for the WHERE clause, where the key is the field name and the value is the field value.

**Example**

```python
with sqlite as db:
	db.update('users', values={'login': 'Johanes'}, where={'login': 'John'})
```

### DELETE

The ```delete()``` method of the SQLite instance is used to remove a record from a table.

```python
def delete(table_name, where=None)
```

Here:
- ```table_name```: Name of the table
- ```where```: A dictionary for the WHERE clause, where the key is the field name and the value is the field value.

**Example**

```python
with sqlite as db:
	db.delete('users', where={'login': 'John'})
```
