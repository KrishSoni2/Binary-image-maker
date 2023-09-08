import turtle



t = turtle
# Speed of the turtle
t.speed(100)
 #makes turtle a square
t.shape('square') 


# Add a turtle Screen
wn = turtle.Screen()
#sets background screen to light gray
wn.bgcolor('light gray') 

# Part A 

# Wrting a list that contains binary code to draw the original gradient

orig_gradient = [['11111111', '11111111', '11111111'], ['11101011', '11111010', '11101011'], ['11010110', '11110101', '11010110'], ['11000010', '11110000', '11000010'], ['10101101', '11101011', '10101101'], ['10011001', '11100110', '10011001'], ['10000101', '11100000', '10000101'], ['01110000', '11011011', '01110000'], ['01011100', '11010110', '01011100'], ['01000111', '11010001', '01000111'], ['00110011', '11001100', '00110011'], ['00101110', '10111000', '00101110'], ['00101001', '10100011', '00101001'], ['00100100', '10001111', '00100100'], ['00011111', '01111010', '00011111'], ['00011001', '01100110', '00011001'], ['00010100', '01010010', '00010100'], ['00001111', '00111101', '00001111'], ['00001010', '00101001', '00001010'], ['00000101', '00010100', '00000101'], ['00000000', '00000000', '00000000']]


#Part B gradient
mypic_gradient =   gradient = [['00000000','11111111','00000000'],['00000000','11111111','00000000'],['00000000','11111111','00000000'],['00000000','11111111','00000000'],['00000000','11111111','00000000'],['11111111','11111111','11111111'],['11111111','11111111','11111111'],['11111111','11111111','11111111'],['11111111','11111111','11111111'],['11111111','11111111','11111111'],['11111111','00000000','00000000'],['11111111','00000000','00000000'],['11111111','00000000','00000000'],['11111111','00000000','00000000'],['11111111','00000000','00000000']]#store the pixel's art binary number in 'gradient' list.

temp = [] #temporary list that modifies gradient

# Procedure to Draw the any gradient
def tetris_piece_draw(gradient):
  t.penup()
  count = 0
  while count < 12:  #makes 12 rows
    for k in gradient:
      rgb = [int(i, 2) for i in k]
      t.color(rgb[0], rgb[1], rgb[2])  #makes a color based on each byte in gradient
      t.begin_fill()
      square()
      t.pencolor(rgb[0], rgb[1], rgb[2])
      t.end_fill()
      t.fd(20)
    row(gradient)
    count = count + 1

# Procedure to  Draw a square:
def square():    
  t.pendown()
  for x in range(4):  #repeats the steps below 4 times
    t.fd(20)
    t.right(90)

#Procedure to add a new row once the turtle finishes a row    
def row(rgb_list):  
  t.penup()
  t.left(180)
  t.fd(len(rgb_list) * 20)
  t.left(90)
  t.fd(20)
  t.left(90)    

# Procedure to Remove one bit from each byte in the RGB
def remove_one_bit(gradient,temp):
  for i in gradient:
  #removes last character from each bit    
    temp.append([i[0][:-1], i[1][:-1], i[2][:-1]]) 
  return temp

# Procude to Add 01 to each byte in the RGB
def add_01(temp):
  temp = [['11111111', '01111111', '11011111'], ['11110111', '10101101', '11111010'], ['01111010', '11011101', '01100111'], ['11010101', '11010110', '00111000'], ['01001111', '10000011', '10000100'], ['11010110', '10111101', '01101101'], ['01101011', '00110010', '11110011'], ['00110011', '00101100', '00101011'], ['11000000', '11000010', '10101110'], ['00001110', '11011010', '11100000'], ['10101110', '00111010', '11001010'], ['11100010', '10001110', '11101000'], ['10101000', '11101001', '10011011'], ['10011000', '10011001', '10100101'], ['11001101', '11000010', '01011100'], ['10010100', '10110100', '01101001'], ['01001010', '01001000', '11000111'], ['10100100', '10001000', '11111010'], ['11110100', '10001111', '10100011'], ['00101011', '00110010', '00110010'], ['10001010', '00101010', '01001000'], ['10100010', '00011110', '10011110'], ['10100001', '11101000', '01010010'], ['01010010', '10000101', '00100000'], ['10101000', '10100010', '00001010'], ['10000000', '00100000', '00001000']]
  return temp
  
# Procedure to Converting to RG Dichrome Palette
def rg_dichrome(gradient):
  t.penup()
  count = 0
  while count < 12:  #makes 12 rows for the gradient
    for k in gradient:
      rgb = [int(i, 2) for i in k]
#takes the colors from red and green and leaves 0 for blue colors      
      t.color(rgb[0], rgb[1], 0)  
      t.begin_fill()
      square()
      t.pencolor(rgb[0], rgb[1], 0)
      t.end_fill()
      t.fd(20)
    row(gradient)
    count = count + 1
  return gradient

# Procedure to Converting the GB Dichrome Palette  
def gb_dichrome(gradient):
  t.penup()
  count = 0
  while count < 12:
    for k in gradient:
      rgb = [int(i, 2) for i in k]
 #takes colors from green and blue and leaves 0 for red colors      
      t.color(0, rgb[1], rgb[2]) 
      t.begin_fill()
      square()
      t.pencolor(0, rgb[1], rgb[2])
      t.end_fill()
      t.fd(20)
    row(gradient)
    count = count + 1
  return gradient

#Procedure Converts to RB Dichrome Palette  
def rb_dichrome(gradient):
  t.penup()
  count = 0
  while count < 12:
    for k in gradient:
      rgb = [int(i, 2) for i in k]
  #takes colors from red and blue and leaves 0 for green colors      
      t.color(rgb[0], rgb[0], rgb[2])
      t.begin_fill()
      square()
      t.pencolor(rgb[0], 0, rgb[2])
      t.end_fill()
      t.fd(20)
    row(gradient)
    count = count + 1
  return gradient

print('Enter a to access part one.')
print()
print('Enter b to access part two. (fire flower)')
print()
part_choice = input().lower() #taking user input

if part_choice =='a':
  print('Enter 1 to draw the original gradient.')
  print('Enter 2 to Remove one bit from each byte in the RGB.')
  print('Enter 3 add 01 in each byte in the RGB.')  
  print('Enter 4 to convert to GB Dichrome Palette')  
  print('Enter 5 to convert to GB Dichrome Palette')
  print('Enter 6 to convert to RB Dichrome Palette.')
  print()
  choice= int(input())
  if choice == 1:
    wn.colormode(255)
    t.penup()
    t.goto(-210, 120)
    square()
    tetris_piece_draw(orig_gradient)
    print()
    print(orig_gradient)
    print(len(orig_gradient))
  elif choice == 2:  #make a gradient with 1 less bit for each bye from gradient
    wn.colormode(255)
    t.penup()
    t.goto(-210, 120)
    square()
    remove_one_bit(orig_gradient, temp)
    tetris_piece_draw(orig_gradient)
    print()
    print(temp) #draw gradient with 1 less bit in each byte after drawing gradient
  #--------------------
  #Choice 3
  elif choice == 3:  
    wn.colormode(255)
    t.penup()
    t.goto(-260, 120)
    square()
    print(tetris_piece_draw(add_01(temp)))
    print(add_01(temp))
  #--------------------
  #Choice 4
  elif choice == 4:  #draws the red and green dichrome
    wn.colormode(255)
    t.penup()
    t.goto(-210, 120)
    square()
    rg_dichrome(orig_gradient)
  #--------------------
  #Choice 5
  elif choice == 5:  #draws the green and blue dichrome
    wn.colormode(255)
    t.penup()
    t.goto(-210, 120)
    gb_dichrome(orig_gradient)
  #--------------------
  #Choice 6
  elif choice == 6:  #draws the red and blue dichrome
    wn.colormode(255)
    t.penup()
    t.goto(-210, 120)
    rb_dichrome(orig_gradient)
  
  else:  #prints an error message if the user types in anything besides the numbers from 1 to 6
    print('You have made a typing error. Please rerun the program.')
  
elif part_choice == 'b':
#All the choices for part B
  print('Enter 1 to draw the My Picture.')
  print('Enter 2 to convert to RG Dichrome Palette.')
  print('Enter 3 to convert to GB Dichrome Palette')
  print('Enter 4 to convert to RB Dichrome Palette.')
  print()
  choice= int(input())

  if choice == 1:
    wn.colormode(255)
    t.penup()
    t.goto(-210, 120)
    square()
    tetris_piece_draw(mypic_gradient)
    print()
    print(mypic_gradient)
    print(len(mypic_gradient))
  #Choice 2
  elif choice == 2:  #draws the red and green dichrome
    wn.colormode(255)
    t.penup()
    t.goto(-210, 120)
    square()
    rg_dichrome(mypic_gradient)
  #--------------------
  #Choice 3
  elif choice == 3:  #draws the green and blue dichrome
    wn.colormode(255)
    t.penup()
    t.goto(-210, 120)
    gb_dichrome(mypic_gradient)
  #--------------------
  #Choice 4
  elif choice == 4:  #draws the red and blue dichrome
    wn.colormode(255)
    t.penup()
    t.goto(-210, 120)
    rb_dichrome(mypic_gradient)
  
  else:  #prints an error message if the user types in anything besides the numbers from 1 to 4
    print('You have made a typing error. Please rerun the program.')