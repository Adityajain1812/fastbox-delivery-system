import json
import math
import csv


# ---------------------------------------------------
# Function to load JSON data
# ---------------------------------------------------
def load_data(filename):
    with open(filename, "r") as file:
        return json.load(file)


# ---------------------------------------------------
# Function to calculate Euclidean distance
# ---------------------------------------------------
def calculate_distance(point1, point2):
    return math.sqrt(
        (point2[0] - point1[0]) ** 2 +
        (point2[1] - point1[1]) ** 2
    )


# ---------------------------------------------------
# Function to find nearest agent
# ---------------------------------------------------
def find_nearest_agent(warehouse_location, agents):

    nearest_agent = None
    minimum_distance = float("inf")

    for agent_id, agent_location in agents.items():

        distance = calculate_distance(
            agent_location,
            warehouse_location
        )

        if distance < minimum_distance:
            minimum_distance = distance
            nearest_agent = agent_id

    return nearest_agent, minimum_distance


# ---------------------------------------------------
# Function to simulate deliveries
# ---------------------------------------------------
def simulate_deliveries(data):

    warehouses = data["warehouses"]
    agents = data["agents"]
    packages = data["packages"]

    # Initialize report dictionary
    report = {}

    for agent_id in agents:
        report[agent_id] = {
            "packages_delivered": 0,
            "total_distance": 0
        }

    print("\n========== DELIVERY SIMULATION ==========")

    # Process all packages
    for package in packages:

        package_id = package["id"]
        warehouse_id = package["warehouse"]
        destination = package["destination"]

        warehouse_location = warehouses[warehouse_id]

        # Find nearest available agent
        assigned_agent, distance_to_warehouse = find_nearest_agent(
            warehouse_location,
            agents
        )

        # Distance from warehouse to destination
        delivery_distance = calculate_distance(
            warehouse_location,
            destination
        )

        # Total trip distance
        total_trip_distance = (
            distance_to_warehouse +
            delivery_distance
        )

        # Update report
        report[assigned_agent]["packages_delivered"] += 1
        report[assigned_agent]["total_distance"] += total_trip_distance

        # Update agent current location after delivery
        agents[assigned_agent] = destination

        # Print simulation details
        print(f"\nPackage ID: {package_id}")
        print(f"Assigned Agent: {assigned_agent}")
        print(f"Warehouse: {warehouse_id}")
        print(f"Destination: {destination}")
        print(f"Distance to Warehouse: {distance_to_warehouse:.2f}")
        print(f"Delivery Distance: {delivery_distance:.2f}")
        print(f"Total Trip Distance: {total_trip_distance:.2f}")

    # Calculate efficiency
    for agent_id in report:

        delivered = report[agent_id]["packages_delivered"]
        total_distance = report[agent_id]["total_distance"]

        if delivered > 0:
            efficiency = total_distance / delivered
        else:
            efficiency = 0

        report[agent_id]["total_distance"] = round(
            total_distance,
            2
        )

        report[agent_id]["efficiency"] = round(
            efficiency,
            2
        )

    # Determine best agent
    best_agent = min(
        report,
        key=lambda agent: (
            report[agent]["efficiency"]
            if report[agent]["packages_delivered"] > 0
            else float("inf")
        )
    )

    report["best_agent"] = best_agent

    return report


# ---------------------------------------------------
# Function to save report JSON
# ---------------------------------------------------
def save_report(report, filename):

    with open(filename, "w") as file:
        json.dump(report, file, indent=4)

    print(f"\nReport saved successfully to {filename}")


# ---------------------------------------------------
# BONUS: Export best agent to CSV
# ---------------------------------------------------
def export_best_agent_csv(report, filename):

    best_agent = report["best_agent"]

    with open(filename, "w", newline="") as csvfile:

        writer = csv.writer(csvfile)

        writer.writerow([
            "Agent ID",
            "Packages Delivered",
            "Total Distance",
            "Efficiency"
        ])

        writer.writerow([
            best_agent,
            report[best_agent]["packages_delivered"],
            report[best_agent]["total_distance"],
            report[best_agent]["efficiency"]
        ])

    print(f"Best agent exported successfully to {filename}")


# ---------------------------------------------------
# Main Function
# ---------------------------------------------------
def main():

    try:
        # Load JSON file
        data = load_data("data.json")

    except FileNotFoundError:
        print("Error: data.json file not found.")
        return

    # Simulate deliveries
    report = simulate_deliveries(data)

    # Display final report
    print("\n========== FINAL REPORT ==========")

    for agent_id, details in report.items():
        print(f"{agent_id}: {details}")

    # Save report JSON
    save_report(report, "report.json")

    # Export best agent CSV
    export_best_agent_csv(
        report,
        "best_agent.csv"
    )


# ---------------------------------------------------
# Program Entry Point
# ---------------------------------------------------
if __name__ == "__main__":
    main()