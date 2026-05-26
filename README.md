# FastBox Mystery Delivery System

## Overview

This project simulates a one-day logistics delivery operation for a fictional company called **FastBox**.

The system:
- Reads warehouse, agent, and package data from a JSON file
- Assigns packages to the nearest available delivery agent
- Simulates package deliveries
- Calculates travel distances
- Generates delivery performance reports
- Identifies the most efficient delivery agent
- Exports the top-performing agent details to CSV

---

# Features

- Dynamic JSON input handling
- Euclidean distance calculation
- Nearest-agent package assignment
- Delivery simulation
- Agent movement tracking
- Performance report generation
- CSV export for best agent
- Clean and modular Python code

---

# Technologies Used

- Python 3
- JSON
- CSV
- Math Library

---

# Project Structure

```text
fastbox-delivery-system/
│
├── main.py
├── README.md
├── requirements.txt
├── sample_data.json
├── report.json
├── best_agent.csv
└── .gitignore
```

---

# Assumptions

1. Each package is assigned to only one nearest agent.

2. Distance is calculated using Euclidean distance.

3. Package delivery order is processed sequentially
   as listed in the JSON file.

4. If two agents are at the same distance from a warehouse,
   the first encountered agent is selected.

5. Efficiency is defined as:

   efficiency = total_distance / packages_delivered

6. Lower efficiency value indicates better performance.

7. The simulation assumes successful delivery
   for all packages.

8. Input JSON structure is assumed to be valid.

9. After completing a delivery, the agent’s
   current location becomes the package destination.

---

# Euclidean Distance Formula

The distance between two coordinates is calculated using:

```math
d = √((x2 - x1)^2 + (y2 - y1)^2)
```

---

# Input Format

Example JSON structure:

```json
{
    "warehouses": {
        "W1": [0, 0]
    },

    "agents": {
        "A1": [5, 5]
    },

    "packages": [
        {
            "id": "P1",
            "warehouse": "W1",
            "destination": [10, 20]
        }
    ]
}
```

---

# Output

The program generates:

## 1. report.json

Contains:
- packages delivered
- total distance traveled
- efficiency score
- best agent

Example:

```json
{
    "A1": {
        "packages_delivered": 2,
        "total_distance": 50.25,
        "efficiency": 25.12
    },

    "best_agent": "A1"
}
```

---

## 2. best_agent.csv

Exports top-performing agent details.

---

# Generated Files

After execution:

- report.json
- best_agent.csv

will be created automatically.

---

# Future Improvements

Possible enhancements:
- Random delivery delays
- Route optimization
- Multi-package batching
- Live map visualization
- Priority deliveries
- Real-time tracking dashboard
