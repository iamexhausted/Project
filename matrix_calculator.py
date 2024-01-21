import tkinter as tk

matrix_entries = []
rref_matrix_entries = []

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
    
    # Clear any existing Entry widgets in the rref matrix
    for entry in rref_matrix_entries:
        entry.destroy()
    rref_matrix_entries.clear()

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
                result = tk.Label(root, text="Result")
                result.grid(row=i+rows+4, column=j+1)
                k = 1
            

root = tk.Tk()
root.title("Matrix Creator")

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

# A Button to get rref matrix
button_rref = tk.Button(root, text="RREF Matrix", command=get_matrix)
button_rref.grid(row=2, column=1)

root.mainloop()
