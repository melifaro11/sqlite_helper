# Python SQLite helper

SQL Helper is a small class that makes it easier to work with SQLite databases in python.

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

The ```select()``` method of the SQLite-instance is used to retrieve data from the database.

```python
def select(table_name, fields=None, where=None, orderby=None, groupby=None)
```

Here:

- ```table_name```: Name of the table
- ```fields```: A list of fields to select (```None``` for all)
- ```where```: Dictionary for the WHERE-clause, where key is the field name, and value is the field value
- ```orderby```: The field name to sorting results
- ```groupby```: The field name to grouping results

**Example**

```python
with sqlite as db:
	results = db.select('users', fields=['id', 'login', 'password'], where={'username': 'john_smith'})
```

### INSERT

The ```insert()``` method of the SQLite-instance is used to add a record to the database.

```python
def insert(table_name, values)
```

Here:
- ```table_name```: Name of the table
- ```values```: Dictionary with values to add

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
- ```table_name```: Name of the table
- ```values```: Dictionary with fields and values to update
- ```where```: Dictionary for the WHERE-clause, where key is the field name, and value is the field value

**Example**

```python
with sqlite as db:
	db.update('users', values={'login': 'Johanes'}, where={'login': 'John'})
```

### DELETE

The ```delete()``` method of the SQLite-instance is used to delete a record from a table.

```python
def delete(table_name, where=None)
```

Here:
- ```table_name```: Name of the table
- ```where```: Dictionary for the WHERE-clause, where key is the field name, and value is the field value

**Example**

```python
with sqlite as db:
	db.delete('users', where={'login': 'John'})
```
