N = int(input("Enter the number of rows:"))
M = int(input("Enter the number of columns:"))

matrix =[[0 for j in range(M)] for i in range(N)]
        #   Columns(M)               Rows(N)

for i in range(0,N):
    for j in range(0,M):
        matrix[i][j] = int(input(f"Enter the value at Matrix[{i}][{j}] : "))
print("Original Matrix")
print(matrix)

# Transposing a matrix using In place approach
for i in range(N):
        for j in range(i+1,N):
                matrix[i][j] ,matrix[j][i] = matrix[j][i] ,matrix[i][j]
                
print("Transposed Matrix using In place approach")
print(matrix)

transpose = [[0 for _ in range(N)] for _ in range(M)]

for i in range(N):
        for j in range(M):
                transpose[j][i] = matrix[i][j]

print("Tranposed matrix again using another matrix")
print(transpose)