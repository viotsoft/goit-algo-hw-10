import pulp

# Define the problem
prob = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Define decision variables as Integer
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')  # Змінено на Integer
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')  # Змінено на Integer

# Define the objective function
prob += lemonade + fruit_juice, "Total_Production"

# Define the constraints
prob += 2 * lemonade + fruit_juice <= 100, "Water_Constraint"
prob += lemonade <= 50, "Sugar_Constraint"
prob += lemonade <= 30, "Lemon_Juice_Constraint"
prob += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"

# Solve the problem
prob.solve()

# Print the results
print(f"Lemonade: {int(lemonade.varValue)}")  # Конвертація в ціле число для наочності
print(f"Fruit Juice: {int(fruit_juice.varValue)}")
print(f"Total Production: {int(pulp.value(prob.objective))}")