class Expense:
 def __init__ (self, name , category ,amount) -> None:
      self.name= name
      self.amount= amount
      self. category= category
      
 def __repr__(self):
         return f"<Expense:{self.name},{self.category},¢{self.amount:.2f} >"

