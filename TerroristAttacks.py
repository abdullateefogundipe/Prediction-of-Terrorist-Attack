# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:51:19 2020
@author: win10
"""
from pydantic import BaseModel
# 2. Class which describes success of terrorist attacks measurements
class TerroristAttack(BaseModel):
    Year: float
    Month: float 
    Day: float 
    Extended: float
    Country: float
    Region: float 
    Suicide: float
    Attack_Type: float
    Target_Type: float 
    individual: float 
    Nationality_target: float 
    Attack_Group: float
    Weapon: float 
    Number_of_Killed: float 
  