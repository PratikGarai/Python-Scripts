from neo4j import GraphDatabase

class PathwayDatabase:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def get_respons


if __name__ == "__main__":
    db = PathwayDatabase("bolt://localhost:7687", "", "")
    db.close()
