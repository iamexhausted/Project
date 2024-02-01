import tkinter as tk

matrix_entries = []
rref_matrix_entries = []
result_label = None   # A label to separate user's matrix and rref matrix
solution_label = None # A label displaying solutions
info_label = None


# A function to row reduce
def rref(matrix):
    rowCount = len(matrix)
    columnCount = len(matrix[0])
    lead = 0

    for row in range(rowCount):
        if lead >= columnCount:
            return matrix
        i = row
        while matrix[i][lead] == 0:
            i += 1
            if i == rowCount:
                i = row
                lead += 1
                if columnCount == lead:
                    return matrix
        matrix[i], matrix[row] = matrix[row], matrix[i]
        pivot = matrix[row][lead]

        matrix[row] = [element / pivot if element != -0.0 
                        else 0.0 for element in matrix[row]]
        for i in range(rowCount):
            if i != row:
                ratio = matrix[i][lead]
                matrix[i] = [iv - ratio * rv if iv - ratio * rv != -0.0 
                                else 0.0 for rv, iv in zip(matrix[row], matrix[i])]
        lead += 1
    return matrix

# A function to create matrix
def create_matrix():
    # Clear any existing Entry widgets in the matrix
    for entry in matrix_entries:
        entry.destroy()
    matrix_entries.clear()

    for entry in rref_matrix_entries:
        entry.destroy()
    rref_matrix_entries.clear()

    # A command to destroy label when creating a new matrix
    global result_label
    if result_label is not None:
        result_label.destroy()

    # A command to destroy label when creating a new matrix
    global solution_label
    if solution_label is not None:
        solution_label.destroy()

    global info_label
    if info_label is not None:
        info_label.destroy()

    # Get the input from the Entry widgets
    input_rows = entry_rows.get()
    input_cols = entry_cols.get()

    # Check if the input is valid integers
    if input_rows.isdigit() and input_cols.isdigit():
        rows = int(input_rows)
        cols = int(input_cols)

        # Create a matrix of Entry widgets
        entries = [[tk.Entry(root) for _ in range(cols)] for _ in range(rows)]
        
        # Fill the Entry widgets with values from the list
        for i in range(rows):
            for j in range(cols):
                entries[i][j].grid(row=i+3, column=j+1)
                matrix_entries.append(entries[i][j])
    else:
        print("Please enter valid integers.")

def glob(rref_matrix):
    global m
    m = rref_matrix


# A function to create a rref matrix 
def get_matrix():
    matrix = []
    rows = int(entry_rows.get())
    cols = int(entry_cols.get())
    for i in range(rows):
        row = []
        for j in range(cols):
            entry = matrix_entries[i*cols + j].get()
            try:
                row.append(float(entry))
            except ValueError:
                print("Please enter valid numbers.")
                return
        matrix.append(row)
    rref_matrix = rref(matrix)
    
    glob(rref_matrix)  # rref_matrix is global and it's f

    for entry in rref_matrix_entries:
        entry.destroy()
    rref_matrix_entries.clear()

    # A command to destroy label when creating a new matrix
    global result_label
    if result_label is not None:
        result_label.destroy()

    # A command to destroy label when creating a new matrix
    global solution_label
    if solution_label is not None:
        solution_label.destroy()

    global info_label
    if info_label is not None:
        info_label.destroy()
    

    # A matrix of Entry widgets for the rref matrix
    entries = [[tk.Entry(root) for _ in range(cols)] for _ in range(rows)]
    
    # Fill the Entry widgets with values from the rref matrix
    k = 0
    for i in range(rows):
        for j in range(cols):
            entries[i][j].grid(row=i+rows+5, column=j+1)  
            entries[i][j].insert(0, str(rref_matrix[i][j]))
            rref_matrix_entries.append(entries[i][j])
            if k == 0:
                result_label = tk.Label(root, text="Result")
                result_label.grid(row=i+rows+4, column=j+1)
                k = 1

def solve_rref(matrix):
    # Number of equations
    n = len(matrix)

    # Number of variables
    m = len(matrix[0]) - 1

    k = 0  # a variable to check for a unique solution
           # (every time there is a sum == 1 it will increase)
    g = n  # a variable to check for a unique solution
           # (every time there is a row of zeroes it will decrease)

    solution = [row[-1] for row in matrix]
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    for row in matrix:
        # Check for no solutions
        if row[-1] != 0 and (sum([int(v) for v in row[:-1]]) == 0):
            return "There are no solutions."
    
        # Check for a unique solution
        if (sum([v for v in row[:-1]]) == 1):
            k+=1
        elif (sum([v for v in row[:-1]]) == 0):
            g-=1
        
    if k == g:
        result = []
        variables1 = []
        for row in matrix:
            for i in range(m):
                if row[i] == 1:
                    variable1 = letters[i]
                    variables1.append(variable1)
        for var, val in zip(variables1, solution):
            if var != '':
                string = f'{var} = {val}'
                result.append(string)
        return f"There is exactly one solution: {result}"
    
    for row in matrix:
        # Check for infinite solutions
        if (sum([v for v in row[:-1]]) != 1) or (sum([v for v in row[:-1]]) != 0):
            pivots = []    # pivots
            variables = []    # free variables
            result = []        # a final list of all solutions
            for row in matrix:
                k=0     # a variable to control pivot positions
                for j in range(m):
                    if k == 0:
                        string = ''  # a string for pivots
                        after = ''   # a string for free variables
                        if row[j] == 1:
                            k=1
                            string += letters[j]
                    else:
                        if row[j] != 0:
                            if row[j] < 0 and row[-1] == 0:
                                a = str(row[j])
                                a = a[1::]
                                a = float(a)
                                if a == 1:
                                    after += f'{letters[j]}'
                                else:
                                    after += f'{a}*{letters[j]}'
                            elif row[j] > 0 and row[-1] == 0:
                                if row[j] == 1:
                                    after += f'-{letters[j]}'
                                else:
                                    after += f'-{row[j]}*{letters[j]}'
                            elif row[j] < 0 and row[-1] != 0:
                                a = str(row[j])
                                a = a[1::]
                                a = float(a)
                                if a == 1:
                                    after += f' + {letters[j]}'
                                else:
                                    after += f' + {a}*{letters[j]}'
                            else:
                                if row[j] == 1:
                                    after += f' - {letters[j]}'
                                else:
                                    after += f' - {row[j]}*{letters[j]}'
                            
                pivots.append(string)
                variables.append(after)
            for piv, val, var2 in zip(pivots, solution, variables):
                if piv != '':
                    if val != 0:
                        string = f'{piv} = {val}{var2}'
                        result.append(string)
                    elif val == 0 and var2 == '':
                        string = f'{piv} = {val}'
                        result.append(string)
                    else:
                        string = f'{piv} = {var2}'
                        result.append(string)
            return f"There are infinitely many solutions: {result}"  
    return "Unexpected case."

def solve():
    global info_label
    global solution_label
    get_matrix()
    rows_m = len(m)
    cols_m = len(m[0])
    solution = solve_rref(m)
    info_label = tk.Label(root, text='Solution:')
    info_label.grid(row=rows_m+4, column=cols_m+1) 
    solution_label = tk.Label(root, text=solution)
    solution_label.grid(row=rows_m+6, column=cols_m+1)    

root = tk.Tk()
root.title("Solve equations")

# Entry widgets to enter the number of rows and columns
entry_rows = tk.Entry(root)
entry_rows.grid(row=0, column=1)
label_rows = tk.Label(root, text="Rows:")
label_rows.grid(row=0, column=0)

entry_cols = tk.Entry(root)
entry_cols.grid(row=1, column=1)
label_cols = tk.Label(root, text="Columns:")
label_cols.grid(row=1, column=0)


# A Button to create matrix
button_create = tk.Button(root, text="Create Matrix", command=create_matrix)
button_create.grid(row=2, column=0)

# A Button to get solution
button_sol = tk.Button(root, text="Solution", command=solve)
button_sol.grid(row=2, column=1)

root.mainloop()
