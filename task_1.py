from pulp import LpMaximize, LpProblem, LpVariable

# Створення моделі
model = LpProblem(name="production-optimization", sense=LpMaximize)

# Змінні рішення (скільки одиниць кожного напою виробляти)
lemonade = LpVariable(name="Lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable(name="Fruit_Juice", lowBound=0, cat="Integer")

# Функція цілі (максимізація загальної кількості вироблених напоїв)
model += lemonade + fruit_juice, "Total Products"

# Обмеження ресурсів
model += (2 * lemonade + fruit_juice <= 100, "Water Constraint")
model += (1 * lemonade <= 50, "Sugar Constraint")
model += (1 * lemonade <= 30, "Lemon Juice Constraint")
model += (2 * fruit_juice <= 40, "Fruit Puree Constraint")

# Розв'язання задачі
model.solve()

# Вивід результатів
print(f"Максимальна кількість Лимонаду: {lemonade.varValue}")
print(f"Максимальна кількість Фруктового соку: {fruit_juice.varValue}")
print(f"Загальна кількість вироблених напоїв: {model.objective.value()}")
