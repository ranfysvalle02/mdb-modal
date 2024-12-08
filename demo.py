import modal  
import pymongo  

app = modal.App("example-hello-mongodb")  
image = modal.Image.debian_slim().pip_install("fastapi", "pymongo")    
  
@app.function(image=image)    
@modal.web_endpoint(method="POST", docs=True)  
def goodbye(data: dict) -> str:  
    mdb_uri = data.get("mdb_uri", "")  
    #database_name = data.get("database_name", "default_db")  
    #collection_name = data.get("collection_name", "transcripts")  
  
    if not mdb_uri:  
        return "Error: 'mdb_uri' is required."  
  
    # Connect to MongoDB  
    client = pymongo.MongoClient(mdb_uri)  
    try:  
        # The 'ping' command is a basic way to check if a MongoDB connection is alive  
        client.admin.command("ping")  
    except Exception as e:  
        return f"NOT OK: Unable to connect to MongoDB - {str(e)}"  
  
    return "OK"
