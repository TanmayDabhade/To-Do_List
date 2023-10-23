def buildTodoList(TodoItem):
    todoList = []
    todoList.append(TodoItem)
    return todoList

def addTodoItem(listitem, Index, TodoItem):
    listitem.append(TodoItem)
    return listitem

def removeTodoItem(listitem, Index):
    Index = int(Index)-1
    listitem.pop(Index)
    return listitem

def printTodoList(listitem):
    print("Todo List")
    print("---------")
    print("Item Number\tTodo Item")
    print("-----------\t---------")
    for i, item in enumerate(listitem):
        print("{:^11}|{:^}".format(str(i+1), item))
    return listitem

def main():
    listitem = []
    todoList = []
    while True:
        print("Build a todo list")
        print("1. Add a todo item")
        print("2. Remove a todo item")
        print("3. Print the todo list")
        print("4. Quit")
        todoList = buildTodoList(listitem)
        choice = input("Enter your choice: ")
        if choice == "1":
            Index = input("Enter the task number: ")
            TodoItem = input("Enter the todo item: ")
            listitem = addTodoItem(listitem, Index, TodoItem)
        elif choice == "2":
            Index = input("Enter the task number: ")
            listitem = removeTodoItem(listitem, Index)
        elif choice == "3":
            printTodoList(listitem)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
    print("Goodbye!")

if __name__ == "__main__":
    main()