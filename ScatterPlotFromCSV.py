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

import matplotlib.pyplot as plt
import pandas as pd
from Object import Object
from Names3D import Names3D
from check_col import check_numeric_cols

DEFAULT_DOT_COLOR_MAP = 'Spectral'
DEFAULT_DOT_SIZE = 10

class ScatterPlotFromCSV(Object):
    def __init__(self,
                 plot_title = '',
                 csv_path = '',
                 col_name = Names3D(),
                 plot_file_path = '',
                 dot_color_map = DEFAULT_DOT_COLOR_MAP,
                 dot_size = DEFAULT_DOT_SIZE            
            ):
                                    
        self.__plot_title = plot_title
        self.__csv_path = csv_path
        self.__col_name = col_name
        self.__plot_file_path = plot_file_path
        self.__dot_color_map = dot_color_map
        self.__dot_size = dot_size
    
    @property
    def plot_title(self):
        return self.__plot_title

    @plot_title.setter
    def plot_title(self, plot_title):
        self.__plot_title = plot_title


    @property
    def csv_path(self):
        return self.__csv_path

    @csv_path.setter
    def csv_path(self, csv_path):
        self.__csv_path = csv_path

        
    @property
    def col_name(self):
        return self.__col_name

    @col_name.setter
    def col_name(self, col_name):
        self.__col_name = col_name


    @property
    def plot_file_path(self):
        return self.__plot_file_path

    @plot_file_path.setter
    def plot_file_path(self, plot_file_path):
        self.__plot_file_path = plot_file_path


    @property
    def dot_color_map(self):
        return self.__dot_color_map

    @dot_color_map.setter
    def dot_color_map(self, dot_color_map):
        self.__dot_color_map = dot_color_map
        

    @property
    def dot_size(self):
        return self.__dot_size

    @dot_size.setter
    def dot_size(self, dot_size):
        self.__dot_size = dot_size
        
    
    def generate(self, show_plot=False):
        df = self.__load_data()
        if df is None:
            return False
        
        check_col_result = check_numeric_cols(df,
                                              self.col_name.x,
                                              self.col_name.y,
                                              self.col_name.z)
        if check_col_result.err_detected:
            preamble = "Errors detected for following columns in "
            err_str = "{}{}: {}".format(preamble, self.csv_path,
                    check_col_result.err_str)
            self.set_err(err_str)
            return False
    
        df.plot(kind='scatter',
                      title=self.plot_title,
                      x=self.col_name.x,
                      y=self.col_name.y,
                      c=self.col_name.z,
                      s=self.dot_size,
                      colormap=self.dot_color_map,
                      colorbar=True)
            
       
        if not self.__save_plot():
            return False
        
        if show_plot:
            plt.show()
            
        return True

        
    def __load_data(self):
        try:
            df = pd.read_csv(self.csv_path)
        except Exception as e:
            err_str = "Error reading csv file: %s" % str(e)
            self.set_err(err_str)
            df = None
        return df
    
    def __save_plot(self):
        try:
            plt.savefig(self.plot_file_path)
            ret = True
        except Exception as e:
            err_str = "Error saving plot: %s" % str(e)
            self.set_err(err_str)
            ret = False
        return ret
