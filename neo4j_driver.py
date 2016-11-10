

from neo4j.v1 import GraphDatabase, basic_auth

# Code from: http://neo4j.com/docs/developer-manual/current/drivers/
driver = GraphDatabase.driver("bolt://192.168.99.100:32771", auth=basic_auth("neo4j", "neo4jneo4j"))
session = driver.session()


#########
# CREATE #
#########


# Create nodes
session.run("CREATE(var:Person {firstName:'Stefan',lastName:'Bieliauskas'})")
session.run("CREATE(var:Person {firstName:'Andreas',lastName:'Schreiber'})")
session.run("CREATE(var:Person {firstName:'Bob',lastName:'Müller'})")
session.run("CREATE(var:Person {firstName:'Alice',lastName:'Meier'})")

# Create relation with duplicates

#session.run("CREATE (from:Person {firstName:'Stefan',lastName:'Bieliauskas'})-[rel:KNOWS]-> (to:Person {firstName:'Andreas',lastName:'Schreiber'})")


# Create relation with existing nodes
# session.run("MATCH (u:Person {firstName:'Stefan'}), (r:Person {firstName:'Andreas'})  CREATE (u)-[:KNOWS]->(r)")



#########
# MERGE #
#########

# session.run("""
# MERGE (from:Person {firstName:'Stefan',lastName:'Bieliauskas'})
# MERGE (to:Person {firstName:'Andreas',lastName:'Schreiber'})
# MERGE (from)-[rel:KNOWS]->(to)"""


#########
# Query #
#########

result = session.run ("MATCH (person:Person) RETURN person")

for row in result:
    print(row["person"])


#########
# DELETE #
#########

# session.run("MATCH (X) DETACH DELETE (X)")