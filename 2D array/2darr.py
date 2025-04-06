# prepare for the interview question
# remember, you failed miserably in paycom interview, but you have 6 months until july to make a great comback. 

ta = [ [ 11 , 3 , 9 , 1 ] , [ 25 , 6 , 10 ] , [ 10 , 8 , 12 , 5 ]]

empty2D = [[]]

fixOutD = [[] for _ in range(5)] # 5 row 1 col


# different and correct way to declare matrix
row, col = 3, 4
m1 = [ [0 for _ in range(col)] for _ in range(row)]
m2 = [[0] * col for _ in range(row)]

# assign values
m1[1][2]=6
m2[1][2]=3

# wrong way to declare matrix
m3 = [[0]*col]*row
m3[1][2]=3 # it assigns 3 every 3rd index of the row. 

#access rows: 

for row1 in m1:
    for i in range(col):
        col1 = [row1[i] for row1 in m1]
        print(col1) 

# odf page 149


