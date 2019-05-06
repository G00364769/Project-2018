import pymongo
myclient = None

def connect():
	global myclient
	myclient=pymongo.MongoClient()
	myclient.admin.command('ismaster')
	
def insert():
    mydb=myclient["project"]
    docs=mydb["docs"]
    query={"name":"Mayo"}
    people=docs.find(query)
    for p in people:
        print(p)

	
def main():
    if (not myclient):
        try:
            connect()
            insert()
        except Exception as e:
            print("Error",e)
			
if __name__ == "__main__":
    
    main()