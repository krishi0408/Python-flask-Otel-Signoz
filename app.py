from flask import Flask, request, jsonify, render_template, redirect, url_for
from bson.objectid import ObjectId
from config import configure_app
from db import mongo
from logger import logger
import random
import time
import os

app = Flask(__name__)
configure_app(app)

@app.route("/")
def index():
    orders = mongo.db.orders.find()
    return render_template("index.html", orders=orders)

@app.route("/createOrder", methods=["POST"])
def create_order():
    if random.random() < 0.1:
        logger.error("Order creation failed due to random error.")
        return jsonify({"error": "Failed to create order"}), 500

    item_name = request.form.get("item_name")
    quantity = request.form.get("quantity")

    if not item_name or not quantity:
        logger.warning("Invalid input: missing item_name or quantity.")
        return redirect(url_for("index"))

    mongo.db.orders.insert_one({"item_name": item_name, "quantity": int(quantity)})
    logger.info(f"Order created: {item_name} - {quantity}")
    return redirect(url_for("index"))

@app.route("/checkInventory", methods=["GET"])
def check_inventory():
    delay = random.uniform(0.2, 0.8)
    time.sleep(delay)
    logger.info(f"Inventory checked with delay: {delay:.3f}s")
    return jsonify({"status": "Inventory checked", "delay": f"{delay:.3f}s"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
