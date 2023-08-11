import json
class Employee:
     Empcount=0
     def __init__(self, Name, DOB, Height,City,State):
        self.Name=Name
        self.DOB=DOB
        self.Height=Height
        self.City=City
        self.State=State
        Employee.Empcount=Employee.Empcount+1
     def displayCount(self):
      print("The number of Employees are:",self.Empcount)
      return""
     pass     
     def displayDetails(self):
      return(f"Name of Employee is:", {self.Name},"The Date of Birth of Employee is:", self.DOB,"The height of the Employee is:",self.Height,"The City of the Employee is:",self.City,"The State of the Employee is:",self.State)
Employee_Details=({

      "Employee1":{
      "Name":"Akash",
      "DOB":'15/2/1978',
      "Height":167.64,
      "City":"Kodaku",
      "State":"Karnataka"},
 
"Employee2":{
"Name":"Vishal",
"DOB":'20/5/1986',
"Height":155.54,
"City":"Panaji",
"State":"Goa"},


"Employee3":{
"Name":"Varun",
"DOB":'26/8/1982',
"Height":160,
"City":"Madikeri",
"State":"Karnataka"},


"Employee4":{
"Name": "Arun",
"DOB":'5/5/1990',
"Height":159.12,
"City":"Vijayapura",
"State":"Karnataka"},


"Employee5":{
"Name":"Karthik",
"DOB":'20/11/1988',
"Height":162,
"City":"Kushalnagar",
"State":"Karnataka"
}})
print(Employee_Details)
Employee_List=[]
with open('Employ.json', 'w') as f:
  EmDetails=json.dump(Employee_Details,f,indent=1)
print(EmDetails)
with open("Employ.json","r") as f:
     Emp1= json.load(f)
     Empee=[Emp1]
     for i in range(len(Empee[0])):
          Employee_List.append(Empee[0][f'Employee{i+1}'])
     print(Employee_List)    
Empp1=Employee("Name","DOB","Height","City","State")
Empp2=Employee("Name","DOB","Height","City","State")
Empp3=Employee("Name","DOB","Height","City","State")
Empp4=Employee("Name","DOB","Height","City","State")
Empp5=Employee("Name","DOB","Height","City","State")
Empp1.displayCount()
Empp1.displayDetails()
Empp2.displayDetails()
Empp3.displayDetails()
Empp4.displayDetails()
Empp5.displayDetails()
