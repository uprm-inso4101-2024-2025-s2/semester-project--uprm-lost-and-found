from database.database import Database


Database()

from database.handlers import lost_items_handler
handler=lost_items_handler.LostItemsHandler()

handler.createItem("1","lost item 1","random date","no photo","aaaaa")
handler.getItem("1")
handler.updateItem("1")
handler.deleteItem("1")
try:
    handler.getItem("1")
except:
    print("item not found")