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

from ScatterPlotFromCSV import ScatterPlotFromCSV
from Names3D import Names3D
import params as prm


def main():
    # Create plot object.
    plot = ScatterPlotFromCSV()

    # Assign settings to plot object.    
    plot.plot_title = prm.PLOT_TITLE
    plot.csv_path = prm.CSV_PATH    
    plot.col_name = Names3D(prm.X_COL_NAME, 
                              prm.Y_COL_NAME, 
                              prm.Z_COL_NAME)    
    plot.plot_file_path = prm.PLOT_FILE_PATH
    plot.dot_color_map = prm.DOT_COLOR_MAP
 
    # Generate the file containing the plot,
    # and display the plot on the screen
    # if the show_plot parameter is True.
    if not plot.generate(prm.SHOW_PLOT):
        print(plot.err_str)
        return 1
    
    return 0


if __name__ == '__main__':
    exit_code = main()
    exit(exit_code)

