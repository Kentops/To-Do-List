class Task():
  '''
  The Task Class
  _description: string - Describes the task
  <<get>> _date: string - due date mm/dd/yyyy
  _time: string - due time hh/mm
  __lt__ compares by time
  '''

  def __init__(self,desc,date,time):
    '''Constructor'''
    self._description = desc
    self._date = date
    self._time = time

  def __str__(self):
    '''String representation'''
    return f"{self._description} - Due: {self._date} at {self._time}"

  def __repr__(self):
    '''Formatted representation, used when describing the object, not when expressing a string.'''
    return f"{self._description},{self._date},{self._time}"

  def __lt__(self,other):
    '''Overrides less than. Compare by time, largest to smallest'''
    #Check each layer, [inclucive : exclusive]
    if(self._date[6:] == other._date[6:]):
      if(self._date[0:2] == other._date[0:2]):
        if(self._date[3:5] == other._date[3:5]):
          if(self._time[0:2] == other._time[0:2]):
            return self._time[3:] < other._time[3:]
          else:
            return self._time[0:2] < other._time[0:2]
        else:
          return self._date[3:5] < other._date[3:5]
      else:
        return self._date[0:2] < other._date[0:2]
    else:
      return self._date[6:] < other._date[6:]

  @property
  def date(self):
    '''Date accessor method'''
    return self._date