from database.database import Database
from datetime import date


Database()

from database.handlers import lost_items_handler, found_items_handler

handler=lost_items_handler.LostItemsHandler()

handler.createItem(1,"lost item 1","wallet",date.today().isoformat(),b"no photo","aaaaa")
handler.getItem(1)
handler.updateItem(1)
handler.deleteItem(1)
try:
    handler.getItem(1)
except:
    print("item not found")


#Adding the Found items handler
handler2=found_items_handler.FoundItemshandler()
#Test Create, get, delete and update Item with dummy inputs
handler2.createItem(3, "2025-04-26", "Library", "Found a wallet witn $20","https://res.cloudinary.com/demo/image/upload/sample.jpg", "Ann", "ann@upr.edu")
handler.getItem(3)
handler.updateItem(3)
handler.deleteItem(3)
try:
    handler.getItem(3)
except:
    print("item not found")