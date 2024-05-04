from task import Task
class TaskList():
  '''
  A list to store and iterate tasks
  _tlist - a list of task objects
  n - iterator
  add_task(desc,date,time) - Creates a new task and adds it to tlist
  get_current_task(self) - returns the task from the beginning of tlist
  mark_complete(self) - removes and returns the first task in tlist
  __len__() - length
  __itr__ - initializes n and returns self
  __next__ - basic iteration, iterates one position at a time, returns tlist[n+1] or raises StopIteration
  '''

  def __init__(self):
    '''initializes tlist by reading off of tasklist.txt'''
    self._tlist = []
    with open("tasklist.txt") as my_file:
        lines = my_file.readlines()
        for line in lines:
            parts = line.strip().split(",")
            if len(parts) == 3:  
                self._tlist.append(Task(parts[0], parts[1], parts[2]))

    self._tlist.sort()
    
    '''self._tlist = []
    #Read file
    my_file = open("tasklist.txt")
    usable = my_file.read()
    lines = usable.split("\n")
    for line in lines:
      parts = line.split(",")
      self._tlist.append(Task(parts[0],parts[1],parts[2]))

    #organize by date
    self._tlist.sort()'''

  def add_task(self, desc, date, time):
    '''Adds a news task to tlist'''
    self._tlist.append(Task(desc,date,time))
    self._tlist.sort()

  def get_current_task(self):
    '''Returns the first task in tlist'''
    if self._tlist:
      return self._tlist[0]
    else:
      return None

  def mark_complete(self):
    '''Removes and returns the first task in tlist'''
    current_task = self.get_current_task()
    if current_task:
      self._tlist.remove(current_task)
      return current_task
    else:
      return None

  def __len__(self):
    '''returns the length of tlist'''
    return len(self._tlist)

  def __iter__(self):
    self._n = 0
    return self

  def __next__(self):
    if self._n < len(self._tlist):
      current_task = self._tlist[self._n]
      self._n += 1
      return current_task
    else:
      raise StopIteration
      
    '''if(self._n + 1 < len(self._tlist)):
      #+1 because the next element is returned
      self._n += 1
      return self._tlist[self._n]
    else:
      raise StopIteration'''