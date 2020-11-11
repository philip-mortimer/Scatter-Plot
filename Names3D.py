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

class Names3D:
    def __init__(self,
            x = 'x',
            y = 'y',
            z = 'z'
            ):
        self.__x = x
        self.__y = y
        self.__z = z
    
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x
    

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y


    @property
    def z(self):
        return self.__z

    @z.setter
    def z(self, z):
        self.__z = z
