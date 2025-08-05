def to_do_list():
    tasks=[]

    while True:
        print("1. Agregar Tarea")
        print("2. Eliminar Tarea")
        print("3.Ver Tareas")
        print("4.Salir")
        choice = input("Ingrese su elección: ")

        if choice == "1":
            task = input ("Ingrese Tarea: ")
            tasks.append(task)
        elif choice == "2":
            task = input("Ingrese la tarea a remover: ")
            if task in tasks:
                tasks.remove(task)
            else:
               print("Revise que no se esté equivocando.")
        elif choice == "3":
            print ("Tasks:")
            for task in tasks:
                print("-" + task)
        elif choice == "4":
            break
        else:
            print("Opción incorrecta.")

to_do_list()        