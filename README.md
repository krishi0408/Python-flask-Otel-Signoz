# Python Sample Application – Flask + MongoDB (for Automatic and Manual Instrumentation with OpenTelemetry & SigNoz Demonstration)

This Python sample application is a starter for developers who want to try out automatic and manual instrumentation with OpenTelemetry and send telemetry data to **SigNoz** for full-stack observability.

This Python sample application is a starter for demonstrating automatic and manual instrumentation with OpenTelemetry and sending telemetry data to SigNoz for full-stack visibility.

It simulates a basic order management service with two main endpoints:

* `/createOrder` – Creates a new order (90% success, 10% failure simulation)

/checkInventory – Simulates checking inventory with a random delay (200–800ms).
* `/checkInventory` – Simulates variable delay for inventory checks

## File Structure
```
python-flask-otel-signoz
│_ templates/
│    └─ index.html                # Simple HTML UI to interact with the Flask endpoints
│_ app.py                         # Flask app 
│_ config.py                      # Loads environment variables and configures Flask app (e.g., MongoDB URI)
│_ db.py                          # Initializes PyMongo instance for database connection
│_ logger.py                      # Configures application-wide logging
│_ requirements.txt               # Python dependencies list
|_ .env                           # Environment variables (MongoDB URI)
```
## Prerequisites

- Python `3.8+` installed
- Pip installed
- MongoDB Atlas account or a local MongoDB instance
- SigNoz Cloud or self-hosted SigNoz instance
- Git (optional, for cloning the repo)

## Setup Instructions

1. Clone the repository
```
git clone https://github.com/krishi0408/Python-flask-Otel-Signoz.git
cd Python-flask-Otel-Signoz
```
2. Create & activate a virtual environment
```
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```
3. Install dependencies
```
pip install -r requirements.txt
```
4. Configure MongoDB
* Create a MongoDB Cluster using [MongoDB Atlas](http://mongodb.com/atlas) or use a local MongoDB instance
* Create a database named `orders`.
* Update your MongoDB connection string in `.env`:
```
MONGO_URI = "mongodb+srv://<username>:<password>@<cluster-url>/<db-name>?retryWrites=true&w=majority"
```

## Running the Application
Run the app using :
```
python app.py
```

## OpenTelemetry & SigNoz Setup Guide
This repository focuses on the Python application setup.
For full details on how to instrument this application with OpenTelemetry and visualize the data in SigNoz, refer to the companion blog post:- https://www.notion.so/From-Black-Box-to-Full-Observability-Instrumenting-Python-Services-with-OpenTelemetry-and-SigNoz-24c8c44242538035bf48cdf41bc5437d?source=copy_link


