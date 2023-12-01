from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import aiohttp

app = FastAPI()

API_CAT_FACT_URL = "https://meowfacts.herokuapp.com"

@app.get("/hello")
def hello():
    return {"Hello":"World"}\
    
@app.get("/catfact")
async def catfact():
    url = API_CAT_FACT_URL
    data = await connect_to_outside_cat_fact_api(url)
    return {"CatFact" : data}

@app.get("/catfact/{count}")
async def catfactsByCount(count:int):

    url = API_CAT_FACT_URL + "/?count=" + str(count)
    data = await connect_to_outside_cat_fact_api(url)

    # # Convert the JSON-formatted string to a Python dictionary
    # data_dict = json.loads(data)
    # # Access the "data" key as a list and append its elements to the facts list
    # facts.extends(data_dict["data"])

    return {"Catfacts": data}

async def connect_to_outside_cat_fact_api(url:str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.text()
            return data
        
origins = [
   "http://127.0.0.1:5500", # Replace with the port your Vue.js app is running on
]

# Cross-Origin Resource Sharing (CORS) enabled
app.add_middleware(
   CORSMiddleware,
   allow_origins=origins,
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"],
)


