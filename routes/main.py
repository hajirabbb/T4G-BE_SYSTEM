from fastapi import FastAPI
#calling an instance of the class
app = FastAPI()
#to use the instance, use the decorator @
#specify the root. if anyone requires a service they specify a route
@app.get('/')
def home():
    return "message :"  "Welcome to FastAPI"
