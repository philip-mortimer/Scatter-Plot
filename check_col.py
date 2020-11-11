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

from pandas.api.types import is_numeric_dtype
from Object import ErrInfo

def check_numeric_col(df, col_name):
    """
        df:         pandas data frame
        col_name:   name of column to check
        
        Checks that column col_name 
        exists within df and is numeric.
    """
    if col_name in df.columns:
        if is_numeric_dtype(df[col_name]):
            # No error.
            return ErrInfo(err_detected=False)
        else:
            err_str = "'%s' is not numeric" % col_name
    else:
        err_str = "'%s' does not exist" % col_name
        
    return ErrInfo(err_detected=True, err_str=err_str)


def check_numeric_cols(df, *col_names):
    """
        df:         pandas data frame
        col_names:  names of columns to check
        
        Checks that columns whose names are specified
        by col_names in data frame df exist and are numeric.
        If any columns do not exist or are not numeric
        returns an ErrInfo object with err_detected attribute
        set to True and err_str attribute set to string stating 
        which columns do not exist or are not numeric. If
        no errors detected returns ErrInfo object with 
        err_detected attribute set to False.
    """
    results = [check_numeric_col(df, col_name) for col_name in col_names]
    error_strings = [result.err_str for result in results 
                     if result.err_detected] 

    if len(error_strings) == 0:
        return ErrInfo(err_detected=False)
    else:
        err_str = ";".join(error_strings)
        return ErrInfo(err_detected=True, err_str=err_str)
