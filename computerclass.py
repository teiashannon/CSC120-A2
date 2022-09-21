from ast import Add
from typing import Union, Dict


class Computer:


    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):

        self.__description = description
        self.__processor_type = processor_type
        self.__hard_drive_capacity = hard_drive_capacity
        self.__memory = memory
        self.__operating_system = operating_system
        self.__year_made = year_made
        self.__price = price
        print(f"{description} successfully added. Initial price: ${self.__price}.\n")

            

'''Adding information about a computer to the computer class'''
