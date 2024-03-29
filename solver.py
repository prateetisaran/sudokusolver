
def split_into_rows(numbers):
  global rows
  
  rows = {1:{'nums':numbers[0:9],'mnums':[]},
  2:{'nums':numbers[9:18],'mnums':[]}, 
  3:{'nums':numbers[18:27],'mnums':[]}, 
  4:{'nums':numbers[27:36],'mnums':[]}, 
  5:{'nums':numbers[36:45],'mnums':[]}, 
  6:{'nums':numbers[45:54],'mnums':[]}, 
  7:{'nums':numbers[54:63],'mnums':[]}, 
  8:{'nums':numbers[63:72],'mnums':[]}, 
  9:{'nums':numbers[72:],'mnums':[]}}
  
def columns_and_boxes(rows):
  global columns, boxes
  
  columns = {1:{'nums':[], 'mnums':[]},2:{'nums':[], 'mnums':[]},3:{'nums':[], 'mnums':[]},4:{'nums':[], 'mnums':[]},5:{'nums':[], 'mnums':[]},6:{'nums':[], 'mnums':[]},7:{'nums':[], 'mnums':[]},8:{'nums':[], 'mnums':[]},9:{'nums':[], 'mnums':[]}}
  for x,y in rows.items():
    for z in range (9):
      (columns[z+1])['nums'].append((y['nums'])[z])
  boxes = {1:{'nums':[], 'mnums':[]},2:{'nums':[], 'mnums':[]},3:{'nums':[], 'mnums':[]},4:{'nums':[], 'mnums':[]},5:{'nums':[], 'mnums':[]},6:{'nums':[], 'mnums':[]},7:{'nums':[], 'mnums':[]},8:{'nums':[], 'mnums':[]},9:{'nums':[], 'mnums':[]}}
  for number, items in boxes.items():
    p = ((number-1)%3)*3
    if number<4:
      k = 1 
    elif number>3 and number<7:
      k = 4
      
    elif number>6:
      k = 7 
    r1 = (rows[k])['nums']
    r2 = (rows[k+1])['nums']
    r3 = (rows[k+2])['nums']
    (items)['nums'] = ([r1[p], r1[p+1], r1[p+2], r2[p], r2[p+1], r2[p+2],r3[p], r3[p+1], r3[p+2]]) 


def identifymissingnumbers(dictionary):
  for number, parts in dictionary.items():
    numberlist = parts['nums']
    for x in posnums:
      if x not in numberlist:
        parts['mnums'].append(x)
    
  return (dictionary)

def solving_strategy_1(row,box,column):
  global rows, boxes, columns
  rows = row
  boxes = box 
  columns = column

  for x,y in rows.items():
    for l in (y['nums']):
      if type(l) == list:
        w = (y['nums']).index(l)
        
        (y['nums']).remove(l)
        (y['nums']).insert(w,0)
        
    numbers = y['nums']
    missings = y['mnums']
    
    for t in range (numbers.count(0)):
      p = numbers.index(0)
      missingcolumn = (columns[p+1])['mnums']
      boxno = ((((x-1)//3)*3)+(p//3))+1
      missingboxes = (boxes[boxno])['mnums']
      possiblevalues = []
      for value in missings: 
        if value in missingcolumn and value in missingboxes:
          possiblevalues.append(value)
          
      if len(possiblevalues)== 1:
        value = possiblevalues[0]
        (y['nums'])[p] = value
        (y['mnums']).remove(value)
        ((columns[p+1])['mnums']).remove(value)
        ((columns[p+1])['nums'])[x-1] = value
        ((boxes[((((x-1)//3)*3)+(p//3)+1)])['mnums']).remove(value)
        for d in (y['nums']):
          if type(d) == list:
            if value in d:
              d.remove(value)
      else:
        (y['nums'])[p] = possiblevalues 



numbers = input("""Enter all the numbers in your sudoku puzzle in a single row
Replace all missing numbers with zeroes:\n""")
numbers = [int(x) for x in numbers]

split_into_rows(numbers)

columns_and_boxes(rows)

posnums = [1,2,3,4,5,6,7,8,9]

boxes = identifymissingnumbers(boxes)
columns = identifymissingnumbers(columns)
rows = identifymissingnumbers(rows)


for x in range (9):
  trial1 = solving_strategy_1(rows, boxes, columns)
  
for x,y in rows.items():
  print(y['nums'])
  
