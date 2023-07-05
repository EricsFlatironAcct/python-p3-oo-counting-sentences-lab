#!/usr/bin/env python3
import re
class MyString:
  def __init__(self, value=""):
    self.set_value(value)

  def is_sentence(self):
    return self.get_value()[-1]=="."
  
  def is_question(self):
    return self.get_value()[-1]=="?"

  def is_exclamation(self):
    return self.get_value()[-1]=="!"

  def count_sentences(self):
    split_values = re.split('[.?!]' , self.get_value())
    count = 0
    for val in split_values:
      if len(val)>0: 
        count+=1
    return count
  
  def set_value(self, value):
    self._value = value if isinstance(value, str) else print("The value must be a string.")

  def get_value(self):
    return self._value

  value = property(get_value, set_value)