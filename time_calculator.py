def add_time(start, duration,the_day_of_week=None):
  ##Convert to minute
  clock = start[-2:]
  time = start[:-3]

  start_hour = int(time.split(":")[0])
  start_minute = int(time.split(":")[1])
  if clock == "AM":
      start_time_as_minute = 60*start_hour + start_minute
  else:
      start_time_as_minute = 60*(start_hour+12) + start_minute
  duration_hour = int(duration.split(":")[0])
  duration_minute = int(duration.split(":")[1])
  duration_time_as_minute = duration_hour*60 + duration_minute
  ##calculate the duration days
  end_time_as_minute = start_time_as_minute + duration_time_as_minute
  if end_time_as_minute>(60*24):
      duration_day = -(-(end_time_as_minute- (60*24))//(60*24))
      new_time_hour = (int((end_time_as_minute- (60*24))/60))%24
      new_time_minute = (end_time_as_minute- (60*24))%60
      new_time_minute = str(new_time_minute).zfill(2)
  else:
      new_time_hour = (int(end_time_as_minute/60))%24
      new_time_minute = (end_time_as_minute)%60
      duration_day = 0
      new_time_minute = str(new_time_minute).zfill(2)
  
  ##print result according to the requiremets
  ## Time reqruiemnts
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
  ## Day requriments
  if duration_day == 1:
      new_time = new_time + " " + "(next day)"
  if duration_day >1:
      new_time = new_time + " "+ "("+ str(duration_day) + " " + "days later)"
  ##calculate the final day of week
  if the_day_of_week != None:
      the_day_of_week = the_day_of_week.lower()
      Week_name = ["monday","tuesday","wednesday","thursday",'friday','saturday','sunday']
      week_number = Week_name.index(the_day_of_week)
      final_day_of_week_number = (week_number + duration_day)%7
      final_day_of_week = Week_name[final_day_of_week_number].capitalize()
      final_day_of_week = ", "+final_day_of_week
    ##insert final day of week to new_time
      new_time_list = list(new_time)
      position = new_time_list.index("M")+1
      new_time_list.insert(position,final_day_of_week)
      new_time = "".join(new_time_list)
  return new_time


  
  
