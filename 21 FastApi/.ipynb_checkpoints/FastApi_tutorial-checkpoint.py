from fastapi import FastAPI

app = FastAPI()

food_item = {
    'Indian' : ["Samosa", "Dosa"],
    'Italian' : ["Pizza", "Pasta"],
    'American' : ["American Pie", "Hot Dog"]
}

@app.get("/get_items/{cuisie}")
async def hello(cuisie):
    return food_item.get(cuisie)