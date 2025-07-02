class Employe:
  language = "Python"
  salary=1200000
  
shah=Employe()
# hERE Name is instance attribute and salary is class attribute as thi is directly belong to the class
shah.language = "Java"
shah.name = "Shahmir"
print(shah.name, shah.language, shah.salary)