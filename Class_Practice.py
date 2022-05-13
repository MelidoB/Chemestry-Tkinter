from tkinter import *
from Instance import Instance
from Quemestry_Result import chemestry_result

class Interface:
    def __init__(self):
        self.top = None
        self.all_instances = []
        
        self.a_buttom = None
        self.a_result = None

    def insert_instance(self, instance):
        self.all_instances.append(instance)

    def create_result(self):
        self.a_result = Label(self.top, text="None")

    def create_buttom(self):
        #chemestry_result(self.all_instances))
        self.a_buttom = Button(self.top, text="Press for result", command=self.set_result)

    def create_interface(self):
        for i in range(len(self.all_instances)):
            self.all_instances[i].make_instance(self.top)
        
        self.a_buttom.grid(row=len(self.all_instances),column=0)
        self.a_result.grid(row=len(self.all_instances),column=1)

    def set_result(self):
        self.a_result["text"] = chemestry_result(self.all_instances)
    
    def keep_loop(self):
        self.top.mainloop()





def main():
    an_interface = Interface()
    an_interface.top = Tk()

    f_row_pos = 0
    
    an_instance1 = Instance("Instancia 1",f_row_pos)
    an_instance2 = Instance("Instancia 2",f_row_pos+1)
    an_instance3 = Instance("Instancia 3",f_row_pos+2)
    an_instance4 = Instance("Instancia 4",f_row_pos+3)

    an_interface.insert_instance(an_instance1)
    an_interface.insert_instance(an_instance2)
    an_interface.insert_instance(an_instance3)
    an_interface.insert_instance(an_instance4)

    an_interface.create_result()
    an_interface.create_buttom()

    an_interface.create_interface()
    an_interface.keep_loop()

    
    


    
if __name__=='__main__':
    main()
