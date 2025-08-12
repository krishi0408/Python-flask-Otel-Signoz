from flask import Flask, request, jsonify, render_template, redirect, url_for
from bson.objectid import ObjectId
from config import configure_app
from db import mongo
from logger import logger
from opentelemetry import trace
from opentelemetry.trace import StatusCode, Status
import random
import time
import os
from datetime import datetime


tracer = trace.get_tracer(__name__)

app = Flask(__name__)
configure_app(app)

@app.route("/")
def index():
    orders = mongo.db.orders.find()
    return render_template("index.html", orders=orders)

@app.route("/createOrder", methods=["POST"])
def create_order():
    with tracer.start_as_current_span("db_process_order") as span:
        try:
            item_name = request.form.get("item_name")
            quantity = request.form.get("quantity")
            span.set_attribute("item_name", item_name)
            span.set_attribute("quantity", quantity)
            span.add_event("Order Processing started")
            order = {
                'item': item_name,
                'quantity': quantity,
                'created_at': datetime.now()
            }
            result = mongo.db.orders.insert_one(order)
            logger.info(f"Order created: {item_name} - {quantity}")
            span.add_event("Order successfully created in database", {
                "order.id": str(result.inserted_id),
                "order.status": "success"
            })
            span.set_status(Status(StatusCode.OK, "Order created successfully"))
            return redirect('/')
        except Exception as e:
             span.add_event("Order creation failed", {
                "error.message": str(e),
                "order.status": "failed"
            })
             span.set_status(Status(StatusCode.ERROR, f"Order creation failed: {str(e)}"))
             logger.error(f"Order creation failed: {str(e)}")
             return "Order creation failed", StatusCode.ERROR


@app.route("/checkInventory", methods=["GET"])
def check_inventory():
    delay = random.uniform(0.2, 0.8)
    time.sleep(delay)
    logger.info(f"Inventory checked with delay: {delay:.3f}s")
    return jsonify({"status": "Inventory checked", "delay": f"{delay:.3f}s"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
