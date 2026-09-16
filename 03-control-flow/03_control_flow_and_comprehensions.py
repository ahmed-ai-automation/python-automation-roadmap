"""
Module: 03_control_flow_and_comprehensions.py
Description: Control flow operations, filtering loops, and comprehensions for workflow decisions.
Unit: 03 - Control Flow & Comprehensions
"""

# --- 1. Raw Data Simulation (Incoming Customer Inquiries/Orders) ---
raw_orders = [
    {"id": "ORD-101", "amount": 250.0, "status": "completed", "vip": True},
    {"id": "ORD-102", "amount": 0.0, "status": "cancelled", "vip": False},
    {"id": "ORD-103", "amount": 1200.0, "status": "completed", "vip": True},
    {"id": "ORD-104", "amount": 450.0, "status": "pending", "vip": False},
    {"id": "ORD-105", "amount": 80.0, "status": "completed", "vip": False},
]

# --- 2. Conditions & Guard Clauses (Ternary & Truthiness) ---
# Evaluation function using conditional expressions
def categorize_order(amount: float, status: str) -> str:
    # Guard clause: Fail fast if status is not actionable
    if status != "completed":
        return "IGNORED"
    
    # Conditional expression (Ternary operator)
    return "HIGH_VALUE" if amount >= 500.0 else "STANDARD"

# --- 3. Loops, break, continue & loop else ---
valid_orders_count = 0

print("=" * 50)
print("PROCESSING ORDERS QUEUE (Loop & Branching)")
print("=" * 50)

for order in raw_orders:
    # Skip invalid or non-completed orders
    if order["status"] == "cancelled" or order["amount"] <= 0:
        print(f"Skipping Invalid Order: {order['id']}")
        continue

    category = categorize_order(order["amount"], order["status"])
    print(f"Processing {order['id']}: Amount = ${order['amount']} | Category = {category}")
    valid_orders_count += 1
else:
    # Executes only if loop finishes without hitting a 'break'
    print(f"\nQueue execution completed successfully. Total valid: {valid_orders_count}")

# --- 4. Comprehensions (List, Dict & Set) ---
# List Comprehension: Extract high-value order IDs directly
high_value_order_ids = [
    order["id"] 
    for order in raw_orders 
    if order["status"] == "completed" and order["amount"] >= 500.0
]

# Dictionary Comprehension: Map order_id to amount for active orders
active_orders_map = {
    order["id"]: order["amount"] 
    for order in raw_orders 
    if order["status"] != "cancelled"
}

# Set Comprehension: Extract unique status categories
unique_statuses = {order["status"] for order in raw_orders}

# --- 5. Output Summary ---
print("\n" + "=" * 50)
print("COMPREHENSIONS SUMMARY")
print("=" * 50)
print(f"High Value Order IDs (List Comp) : {high_value_order_ids}")
print(f"Active Orders Map (Dict Comp)    : {active_orders_map}")
print(f"Unique Statuses (Set Comp)       : {unique_statuses}")
print("=" * 50)