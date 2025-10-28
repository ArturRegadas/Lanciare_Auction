from flask import Blueprint, render_template

inventoryPage = Blueprint("inventoryPage", __name__)

@inventoryPage.route("/profile/my_items")
def InventoryPage():
    return render_template("Inventory.html")