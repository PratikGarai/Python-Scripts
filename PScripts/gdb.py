from neo4j import GraphDatabase

GRAPH_URI = "bolt://host.docker.internal:7687"
GRAPH_USER = "" 
GRAPH_PASSWORD = ""


class PathwayDatabase:
    def __init__(self, uri, user, password):
        try : 
            self.driver = GraphDatabase.driver(uri, auth=(user, password))
            print("Connected to graph db")
        except Exception as e :
            print("Error connecting to graph db: {}".format(e))

    def close(self):
        self.driver.close()

    def get_path(self, disease):
        with self.driver.session() as session:
            res = session.run('''
            MATCH p = (a)<-[*1..20]-(b) WHERE 
            a.n4sch__label="disease" AND b.n4sch__label=~$disease 
            RETURN nodes(p)
            ORDER BY length(p) DESC;
            ''', disease=disease)
            
            path = []
            r = res.single()
            if not r : 
                return None
            r = r[0]
            for i in r :
                path.append(i.get('n4sch__label'))
            return path
    
    def get_all_tags(self) : 
        with self.driver.session() as session : 
            res = session.run('''
            MATCH (n:n4sch__Class) 
            RETURN n
            ''')
            r = []
            for i in res.values() :
                r.append(i[0].get('n4sch__label'))
            return r

if __name__=="__main__":
    gdb = PathwayDatabase(GRAPH_URI, GRAPH_USER, GRAPH_PASSWORD)
