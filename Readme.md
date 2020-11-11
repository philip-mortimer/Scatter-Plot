# Scatter Plot Program

This program generates a scatter plot from the data in a CSV (comma separated values) file. The path of this file is specified by the value of the **csv_path** variable in the file **params.py**. Each row in the CSV file specifies the x, y and colour values of a dot in the plot. The **x_col_name**, **y_col_name** and **z_col_name** variables in **params.py** specify the names of the columns in the CSV file to be be used for the x values, y values and colour values respectively.

If the value of the **show_plot** variable in **params.py** is True then the program will display the plot on the screen as well as save it to the file whose path is specified by the **plot_file_path** variable in **params.py**.

Note that the file **example.csv** was created to demonstrate the program and does not contain real world data.

## How to run the program

Run the file **main.py**. 

Note that Python 3 must be installed. The **pandas** and **matplotlib** python libraries must also be installed.


    

