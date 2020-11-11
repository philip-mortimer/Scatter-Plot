"""
    Copyright 2019 Philip Mortimer
    
    This file is part of Philip Mortimer Example Programs.

    Philip Mortimer Example Programs is free software: you can redistribute it 
    and/or modify it under the terms of the GNU General Public License as 
    published by the Free Software Foundation, either version 3 of the License,
    or (at your option) any later version.

    Philip Mortimer Example Programs is distributed in the hope that it will be
    useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Philip Mortimer Example Programs.  If not, see 
    <https://www.gnu.org/licenses/>.
"""

plot_title = "Life Style and Life Expectancy"

# Path of CSV file from which to load data (note
# that example.csv was created to demonstrate this
# program and does not contain real world data).
csv_path = 'example.csv'

# Columns in the CSV file to be used for the x and y coordinate values 
# of each dot in the plot.
x_col_name = "Mean hours exercise per week"
y_col_name = "Mean units alcohol consumed per week"

# Column in the CSV file to be used for the colour value of each dot in
# the plot.
z_col_name = "Life expectancy years"

plot_file_path = 'scatter_plot'

dot_color_map = 'jet'

show_plot = True


