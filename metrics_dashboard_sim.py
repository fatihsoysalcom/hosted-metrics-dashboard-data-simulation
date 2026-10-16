import json
import random
import time
from datetime import datetime, timedelta

# This script simulates data for a hosted metrics dashboard, focusing on
# custom business imports and demonstrating how different metrics can be tracked.

def generate_metric_data(num_points=100):
    """Generates simulated time-series data for key business metrics."""
    metrics = {
        "users_registered": [],
        "orders_placed": [],
        "revenue_usd": [],
        "customer_satisfaction": []
    }
    end_time = datetime.now()
    start_time = end_time - timedelta(days=1)

    for i in range(num_points):
        # Simulate time progression
        current_time = start_time + (end_time - start_time) * (i / num_points)
        timestamp = current_time.isoformat()

        # Simulate custom business metric: users registered
        users_registered_value = random.randint(5, 50)
        metrics["users_registered"].append({"timestamp": timestamp, "value": users_registered_value})

        # Simulate custom business metric: orders placed
        orders_placed_value = random.randint(10, 100)
        metrics["orders_placed"].append({"timestamp": timestamp, "value": orders_placed_value})

        # Simulate custom business metric: revenue in USD
        # Revenue is often correlated with orders, but with variance
        revenue_value = orders_placed_value * random.uniform(5.0, 50.0)
        metrics["revenue_usd"].append({"timestamp": timestamp, "value": round(revenue_value, 2)})

        # Simulate a qualitative metric: customer satisfaction (e.g., on a scale of 1-5)
        satisfaction_value = round(random.uniform(3.5, 5.0), 1)
        metrics["customer_satisfaction"].append({"timestamp": timestamp, "value": satisfaction_value})

    return metrics

def display_dashboard_preview(data):
    """Prints a simplified preview of the metrics data, mimicking a dashboard view."""
    print("\n--- Metrics Dashboard Preview ---")
    latest_data = {key: val[-1] for key, val in data.items()}

    print(f"Last Updated: {datetime.now().isoformat()}")
    print("\nKey Metrics:")

    # Displaying the latest value for each metric
    for metric_name, metric_info in latest_data.items():
        print(f"- {metric_name.replace('_', ' ').title()}: {metric_info['value']}")

    print("\n(This is a simulation. In a real scenario, this data would be fetched from a hosted dashboard service.)")

if __name__ == "__main__":
    print("Generating simulated metrics data...")
    simulated_data = generate_metric_data(num_points=50) # Generate data for 50 time points

    # In a real application, this `simulated_data` would be sent to or fetched from
    # a hosted metrics dashboard service (e.g., Datadog, Grafana Cloud, etc.).
    # The choice of service depends on factors like custom data integration needs,
    # scalability, and cost, as discussed in the article.

    display_dashboard_preview(simulated_data)

    # To simulate a real-time dashboard, you could loop this:
    # while True:
    #     time.sleep(60) # Update every minute
    #     simulated_data = generate_metric_data(num_points=1)
    #     display_dashboard_preview(simulated_data)
