def add_time(start, duration,the_day_of_week=None):
  
  ##Convert to minute
  time = start[:-3]
  clock = start[-2:]
  start_hour = int(time.split(":")[0])
  start_minute = int(time.split(":")[1])
  duration_hour = int(duration.split(":")[0])
  duration_minute = int(duration.split(":")[1])
  
  ##generate the time and duration days
  if clock == "AM":
      new_time_hour = start_hour + duration_hour   
  else:
      new_time_hour = (start_hour+12) + duration_hour 
  new_time_minute = start_minute + duration_minute
  
  if new_time_minute >=60 :
      new_time_minute -=60
      new_time_hour +=1
      
  duration_day = new_time_hour//24
  new_time_hour %=24
  new_time_minute = str(new_time_minute).zfill(2)
  
  if new_time_hour == 0:
      new_time ="12:"+ new_time_minute + " "+"AM"
  else:
    if new_time_hour < 12:
        new_time = str(new_time_hour)+":"+ new_time_minute + " "+"AM"
    else:
        if new_time_hour == 12:
            new_time = str(new_time_hour) + ":" + new_time_minute + " "+"PM"
        else:
            new_time =  str(new_time_hour-12)+ ":" + new_time_minute + " "+"PM"
  
  ##calculate the final day of week
  if the_day_of_week :
    the_day_of_week = the_day_of_week.lower().capitalize()
    Week_name = ["Monday","Tuesday","Wednesday","Thursday",'Friday','Saturday','Sunday']
    final_day_of_week = Week_name[(Week_name.index(the_day_of_week)+duration_day)%7]
    new_time += ", "+final_day_of_week
  
  ##generate final settting
  if duration_day == 1:
      new_time +=" (next day)"
  elif duration_day > 1:
      new_time +=" "+"(" + str(duration_day) + " days later)"

  return new_time


  
  

