import logging
import numpy as np
import matplotlib.pyplot as plt

# Set up logging
logging.basicConfig(level=logging.INFO)

class ResourceMonitor:
    def __init__(self):
        self.resources = {}  # Dictionary to hold resource information
        self.alerts = []      # List to hold alerts for resource usage

    def update_resources(self, node_id, resource_info):
        """Update the resource information for a given node."""
        self.resources[node_id] = resource_info
        logging.info(f"Updated resources for node {node_id}: {resource_info}")

    def get_resource_status(self, node_id):
        """Get the current status of resources for a given node."""
        status = self.resources.get(node_id, "No resource information available.")
        logging.info(f"Resource status for node {node_id}: {status}")
        return status

    def check_resource_utilization(self, node_id, thresholds):
        """Check resource utilization against thresholds and trigger alerts if necessary."""
        resource_info = self.get_resource_status(node_id)
        if isinstance(resource_info, dict):
            for resource, usage in resource_info.items():
                if resource in thresholds and usage > thresholds[resource]:
                    alert_message = f"Alert: {resource} usage for node {node_id} exceeded threshold! Current usage: {usage}"
                    self.alerts.append(alert_message)
                    logging.warning(alert_message)

    def get_alerts(self):
        """Get the list of alerts."""
        return self.alerts

    def visualize_resource_usage(self):
        """Visualize resource usage for all nodes."""
        if not self.resources:
            logging.warning("No resource data available for visualization.")
            return

        node_ids = list(self.resources.keys())
        resource_types = list(next(iter(self.resources.values())).keys())
        usage_data = np.array([[self.resources[node_id][resource] for resource in resource_types] for node_id in node_ids])

        plt.figure(figsize=(12, 6))
        for i, resource in enumerate(resource_types):
            plt.plot(node_ids, usage_data[:, i], marker='o', label=resource)

        plt.title("Resource Usage by Node")
        plt.xlabel("Node ID")
        plt.ylabel("Resource Usage")
        plt.legend()
        plt.grid()
        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    monitor = ResourceMonitor()
    
    # Update resources for nodes
    monitor.update_resources("Node1", {"CPU": 70, "Memory": 50, "Bandwidth": 30})
    monitor.update_resources("Node2", {"CPU": 85, "Memory": 60, "Bandwidth": 40})
    
    # Check resource utilization against thresholds
    thresholds = {"CPU": 80, "Memory": 70, "Bandwidth": 50}
    monitor.check_resource_utilization("Node1", thresholds)
    monitor.check_resource_utilization("Node2", thresholds)
    
    # Get alerts
    alerts = monitor.get_alerts()
    for alert in alerts:
        print(alert)
    
    # Visualize resource usage
    monitor.visualize_resource_usage()
