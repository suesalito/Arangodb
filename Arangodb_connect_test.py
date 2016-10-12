# from pyArango.connection import *
# conn = Connection(username="root", password="2222")
#
# db = conn.createDatabase(name="my_pydb")

from arango import ArangoClient

# Initialize the client for ArangoDB
client = ArangoClient(
    protocol='http',
    host='localhost',
    port=8529,
    username='root',
    password='2222',
    enable_logging=True
)

# Create a new database named "my_database"
# db = client.create_database('my_py_database')
db = client.database('my_py_database')

# Create a new collection named "students"  >>> Meaning that create a new table
# students = db.create_collection('students2')

# Create the object and link the object to the collection table name 'Students'
students = db.collection('students2')

# Add a hash index to the collection >> Create the field name on the table
# students.add_hash_index(fields=['name'], unique=True)

# Insert new documents into the collection >> Add the records in the table selection from the students object
# This time the students object linked to the students collection.
students.insert({'name': 'romeo2', 'age': 19})
students.insert({'name': 'josh22', 'age': 18})
students.insert({'name': 'jake22', 'age': 21})

# Execute an AQL query
result = db.aql.execute('FOR s IN students2 RETURN s')
print([student['name'] for student in result])