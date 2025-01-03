import pulp

# Define the problem
prob = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Define decision variables
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Continuous')

# Define the objective function
prob += lemonade + fruit_juice, "Total_Production"

# Define the constraints
prob += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint"
prob += 1 * lemonade <= 50, "Sugar_Constraint"
prob += 1 * lemonade <= 30, "Lemon_Juice_Constraint"
prob += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"

# Solve the problem
prob.solve()

# Print the results
print(f"Lemonade: {pulp.value(lemonade)}")
print(f"Fruit Juice: {pulp.value(fruit_juice)}")
