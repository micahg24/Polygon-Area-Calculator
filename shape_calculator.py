class Rectangle:
  #Initializes varibales
  def __init__(self,w,h):
    self.width = w
    self.height = h

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

  #Sets the width
  def set_width(self,w):
    self.width = w

  #Sets the height
  def set_height(self,h):
    self.height = h

  #Generates the area
  def get_area(self):
    return self.width * self.height

  #Generates the perimeter
  def get_perimeter(self):
    return (2 * self.width) + (2 * self.height)
  
  #Generates diagonal line
  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** 0.5
  
  #Generates picture of shape      
  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."

    else:
      lines =  "*" * self.width + "\n" 
      lines = lines * self.height
      return lines

  #Generates amount of times the shape could fit in the shape
  def get_amount_inside(self, shape):
    return self.get_area() // shape.get_area()


class Square(Rectangle):
  #Initializes side varible and initialzes variable as a string
  #Super() allows functions in the rectangle class to be used
  def __init__(self, side):
    super().__init__(side, side)

  def __str__(self):
    return f"Square(side={self.width})"
  
  #Generates width and height of the square
  def set_side(self, side):
    self.width = side
    self.height = side
    
    
