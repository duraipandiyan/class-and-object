class myclass:
    def myfun1(self,Name,Class,Age,DOB,contact,Mailid):
        self.Name = Name
        self.Class = Class
        self.Age = Age
        self.DOB = DOB
        self.contact = contact
        self.Mailid=Mailid
    def myfun2(self):
        print("Name:",self.Name)
        print("class:", self.Class)
        print("age:", self.Age)
        print("Dob:", self.DOB)
        print("contact:", self.contact)
        print("Mailid:",self.Mailid)
obj=myclass()
obj.myfun1("durai","python",21,2001,900758855,"duraidurai7@gmail.com")
obj.myfun2()
