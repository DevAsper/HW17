class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.status = False

    def mark_as_done(self):
        self.status = True

    def __str__(self):
        return f"Задача: {self.description}, Срок: {self.due_date}, Статус: {'Выполнено' if self.status else 'Не выполнено'}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_done(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_as_done()
                return
        print("Задача не найдена.")

    def show_current_tasks(self):
        for task in self.tasks:
            if not task.status:
                print(task)

class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
        else:
            print("Товар не найден.")

    def get_price(self, item_name):
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
        else:
            print("Товар для обновления цены не найден.")

store1 = Store("Магазин А", "Улица 1")
store2 = Store("Магазин Б", "Улица 2")
store3 = Store("Магазин В", "Улица 3")
print("Магазин А:", store1.name, store1.address,
      "Магазин Б:", store2.name, store2.address,
      "Магазин В:", store3.name, store3.address)

store1.add_item("Яблоки", 0.5)
store1.add_item("Бананы", 0.75)
store2.add_item("Дыня", 0.8)
store3.add_item("Мандарины", 0.6)
print("Товары в магазинах:", {"Магазин А": store1.items, "Магазин Б": store2.items, "Магазин В": store3.items})

store1.update_price("Яблоки", 0.55)

print("Цена яблок:", store1.get_price("Яблоки"))

store1.remove_item("Бананы")

print("Цена бананов после удаления:", store1.get_price("Бананы"))
print("Товары в магазинах:", store1.items, store2.items, store3.items)