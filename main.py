class MyClass:
    def __init__(self,task,time,status):
        self.task=task
        self.time=time
        self.status=False

    def yes(self):
        self.status=True



class Task:
    def __init__(self):
        self.spisok = []


    def add(self,task,time,status):
        a=MyClass(task,time,status)
        self.spisok.append(a)

    def show(self):
        for i in self.spisok:
            print(i.task,i.time,i.status)


    def complete(self,index):
        if 0 <= index < len(self.spisok):
            self.spisok[index].yes()
            print("Задача",self.spisok[index].task,"завершена")
        else:
            print("Неверный индекс")



manager=Task()
while True:
    print("1.Добавить задачу")
    print("2.Показать список задач")
    print("3.Завершить задачу")
    print("4.Выход")
    choice=int(input("Выберите действие:"))
    if choice==1:
        task=input("Введите задачу:")
        time=input("Введите время выполнения задачи:")
        manager.add(task,time,False)
    elif choice==2:
        print("Список задач")
        manager.show()
    elif choice==3:
        try:
            manager.show()
            index=int(input("Введите индекс задачи,которая завершена:"))
            index-=1
            manager.complete(index)
        except:
            print("Неверный индекс")
    elif choice==4:
        break
    else:
        print("Неверный выбор")





