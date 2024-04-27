import sqlite3
import openpyxl
import pandas as pd
import inquirer
conn = sqlite3.connect("Airline.db")
c = conn.cursor()

#Create a table for Pilot
c.execute("""CREATE TABLE IF NOT EXISTS pilot (
pilot_ID CHAR(50), 
pilot_name CHAR(50), 
pilot_age INTEGER, 
PRIMARY KEY(pilot_ID)
)""")

#Create a table for Aircraft
c.execute("""CREATE TABLE IF NOT EXISTS  aircraft(
aircraft_ID CHAR(50), 
aircraft_type CHAR[50], 
aircraft_company CHAR[50], 
PRIMARY KEY(aircraft_ID)
)""")

#Create a table for Flight
c.execute("""CREATE TABLE IF NOT EXISTS flight(
flight_ID CHAR(50), 
flight_date DATE, 
flight_departure CHAR[50], 
flight_arrival CHAR[50], 
PRIMARY KEY(flight_ID)
)""")

#Create a table for Pilot_Flight
c.execute("""CREATE TABLE IF NOT EXISTS pf_info(
pf_ID CHAR[50], 
pilot_ID CHAR[50], 
flight_ID CHAR[50], 
PRIMARY KEY(pf_ID), 
FOREIGN KEY(pilot_ID) 
REFERENCES pilot(pilot_ID), 
FOREIGN KEY(flight_ID) 
REFERENCES flight(flight_ID)
)""")

#Read excel data to sqlite as initail data by Pandas.
dfp = pd.read_excel('Airline.xlsx', sheet_name = 'pilot')
dfa = pd.read_excel('Airline.xlsx', sheet_name = 'aircraft')
dff = pd.read_excel('Airline.xlsx', sheet_name = 'flight')
try:
  dfp.to_sql('pilot',conn, if_exists='append', index= False)
  dfa.to_sql('aircraft',conn, if_exists='append', index= False)
  dff.to_sql('flight',conn, if_exists='append', index= False)
except:
  pass

conn.commit()
conn.close()


#Operation part
#Insert functions for pilot
def Insert_pilot(input1, input2, input3):
  conn = sqlite3.connect('Airline.db')
  c = conn.cursor()
  try:
    c.execute(f"INSERT INTO pilot (pilot_ID, pilot_name, pilot_age) VALUES ({input1}, '{input2}', {input3})")
    conn.commit()
    Select_pilot()
    print ("\nData insert successfully! \n")
  except :
    Select_pilot() 
    print("\nError, please insert again.\n")
  conn.close()

#Insert functions for aircraft
def Insert_aircraft(input1, input2, input3):
  conn = sqlite3.connect('Airline.db')
  c = conn.cursor()
  try:
    c.execute(f"INSERT INTO aircraft (aircraft_ID, aircraft_type, aircraft_company) VALUES ({input1}, '{input2}', '{input3}')")
    conn.commit()
    Select_aircraft()
    print ("\nData insert successfully! \n")
  except :
    Select_aircraft()
    print("\nError, please insert again.\n")
  conn.close()

#Insert functions for flight
def Insert_flight(input1, input2, input3, input4):
  conn = sqlite3.connect('Airline.db')
  c = conn.cursor()
  try:
    c.execute(f"INSERT INTO flight (flight_ID, flight_date, flight_departure, flight_arrival) VALUES ({input1}, '{input2}', '{input3}', '{input4}')")
    conn.commit()
    Select_flight()
    print ("\nData insert successfully! \n")
  except :
    Select_flight() 
    print("\nError, please insert again.\n")
  conn.close()

#Select functions for pilot
def Select_pilot():
  conn = sqlite3.connect('Airline.db')
  c = conn.cursor()

  cursor = c.execute("SELECT pilot_ID, pilot_name, pilot_age from pilot")
  for row in cursor:
    print("Pilot_ID = ", row[0])
    print("pilot_name = ", row[1])
    print("pilot_age = ", row[2], "\n")

  conn.close()

#Select functions for aircraft
def Select_aircraft():
  conn = sqlite3.connect('Airline.db')
  c = conn.cursor()

  cursor = c.execute("SELECT aircraft_ID, aircraft_type, aircraft_company from aircraft")
  for row in cursor:
    print("Aircraft_ID = ", row[0])
    print("Aircraft_type = ", row[1])
    print("Aircraft_company = ", row[2], "\n")

  conn.close()

#Select functions for flight
def Select_flight():
  conn = sqlite3.connect('Airline.db')
  c = conn.cursor()

  cursor = c.execute("SELECT flight_ID, flight_date, flight_departure, flight_arrival from flight")
  for row in cursor:
    print("Flight_ID = ", row[0])
    print("Flight_Date = ", row[1])
    print("Flight_Departure = ", row[2])
    print("Flight_Arrival = ", row[3], "\n")

  conn.close()


#Delete functions for pilot
def Delete_pilot(input1):
  conn = sqlite3.connect('Airline.db')
  try:
    c = conn.cursor()

    c.execute(f"DELETE from pilot where pilot_ID={input1};")    
  except:
    print("Error, please try again.")

  conn.commit()
  Select_pilot()
  print("\nTotal number of rows deleted :", conn.total_changes)
  print("Data delete successfully")
  print("")
  conn.close()

#Delete functions for aircraft
def Delete_aircraft(input1):
  conn = sqlite3.connect('Airline.db')
  try:
    c = conn.cursor()

    c.execute(f"DELETE from aircraft where aircraft_ID={input1};")    
  except:
    print("Error, please try again.")

  conn.commit()
  Select_aircraft()
  print("\nTotal number of rows deleted :", conn.total_changes)
  print("Data delete successfully")
  print("")
  conn.close()

#Delete functions for flight
def Delete_flight(input1):
  conn = sqlite3.connect('Airline.db')
  try:
    c = conn.cursor()

    c.execute(f"DELETE from flight where flight_ID={input1};")    
  except:
    print("Error, please try again.")

  conn.commit()
  Select_flight()
  print("\nTotal number of rows deleted :", conn.total_changes)
  print("Data delete successfully")
  print("")
  conn.close()

#Update functions for pilot
def Update_pilot(input1, input2, input3):
  conn = sqlite3.connect('Airline.db')
  try:
    c = conn.cursor()
    if input2 == "Pilot_name":
      c.execute(f"UPDATE pilot set pilot_name = '{input3}' where pilot_ID={input1}")
    elif input2 == "Pilot_age":
      c.execute(f"UPDATE pilot set pilot_age = {input3} where pilot_ID={input1}")
  except:
    print("Error, please try again.")  

  conn.commit()
  Select_pilot()
  print("\nTotal number of rows updated :", conn.total_changes)
  print("Data update successfully")
  print("")
  conn.close()

#Update functions for aircraft
def Update_aircraft(input1, input2, input3):
  conn = sqlite3.connect('Airline.db')
  try:
    c = conn.cursor()
    if input2 == "Aircraft_type":
      c.execute(f"UPDATE aircraft set aircraft_type = '{input3}' where aircraft_ID={input1}")
    elif input2 == "Aircraft_company":
      c.execute(f"UPDATE aircraft set aircraft_company = '{input3}' where aircraft_ID={input1}")
  except:
    print("Error, please try again.")  

  conn.commit()
  Select_aircraft()
  print("\nTotal number of rows updated :", conn.total_changes)
  print("Data update successfully")
  print("")
  conn.close()

#Update functions for flight
def Update_flight(input1, input2, input3):
  conn = sqlite3.connect('Airline.db')
  try:
    c = conn.cursor()
    if input2 == "Flight_date":
      c.execute(f"UPDATE flight set flight_date = '{input3}' where flight_ID={input1}")
    elif input2 == "Flight_departure":
      c.execute(f"UPDATE flight set flight_departure = '{input3}' where flight_ID={input1}")
    elif input2 == "Flight_arrival":
      c.execute(f"UPDATE flight set flight_arrival = '{input3}' where flight_ID={input1}")
  except:
    print("Error, please try again.")  

  conn.commit()
  Select_flight()
  print("\nTotal number of rows updated :", conn.total_changes)
  print("Data update successfully")
  print("")
  conn.close()



#Start running questions
#1. Choose operations
#2. Choose table
#3. Insert data
def run():
  questions1 = [
    inquirer.List('operation',
      message="What operation do you need?",
      choices=['Select data', 'Insert data', 'Delete data', 'Update data'],),
  ]
  answers1 = inquirer.prompt(questions1)

  #Select process
  if answers1['operation'] == "Select data":
    questions2 = [
    inquirer.List('datatable',
      message="Which table do you need to select?",
      choices=['Pilot', 'Aircraft', 'Flight'],),  
  ]
    answers2 = inquirer.prompt(questions2)
    if answers2['datatable'] == "Pilot":
      Select_pilot()
    elif answers2['datatable'] == "Aircraft":
      Select_aircraft()
    elif answers2['datatable'] == "Flight":
      Select_flight()

  #Insert process
  elif answers1['operation'] == "Insert data":
    questions2 = [
    inquirer.List('datatable',
      message="Which table do you need to insert?",
      choices=['Pilot', 'Aircraft', 'Flight'],),  
  ]
    answers2 = inquirer.prompt(questions2)

    if answers2['datatable'] == "Pilot":
      questions3 = [
      inquirer.Text('Pilot_ID', message="Insert Pilot_ID, ex: 123"),
      inquirer.Text('Pilot_name', message="Insert Pilot_name, ex: Rick"),
      inquirer.Text('Pilot_age', message="Insert Pilot_age, ex: 29"),
  ]
      answers3 = inquirer.prompt(questions3)

      input1 = answers3['Pilot_ID']
      input2 = answers3['Pilot_name']
      input3 = answers3['Pilot_age']
      Insert_pilot(input1, input2, input3)

    elif answers2['datatable'] == "Aircraft":
      questions3 = [
      inquirer.Text('Aircraft_ID', message="Insert Aircraft_ID, ex: 123"),
      inquirer.Text('Aircraft_type', message="Insert Aircraft_type, ex: Airbus A320"),
      inquirer.Text('Aircraft_company', message="Insert Aircraft_company, ex: Emirates"),
  ]
      answers3 = inquirer.prompt(questions3)

      input1 = answers3['Aircraft_ID']
      input2 = answers3['Aircraft_type']
      input3 = answers3['Aircraft_company']
      Insert_aircraft(input1, input2, input3)

    elif answers2['datatable'] == "Flight":
      questions3 = [
      inquirer.Text('Flight_ID', message="Insert Flight_ID, ex: 123"),
      inquirer.Text('Flight_date', message="Insert Flight_date, ex: YYYY-MM-DD"),
      inquirer.Text('Flight_departure', message="Insert Flight_departure, ex: LHR"),
      inquirer.Text('Flight_arrival', message="Insert Flight_arrival, ex: TPE"),
  ]
      answers3 = inquirer.prompt(questions3)

      input1 = answers3['Flight_ID']
      input2 = answers3['Flight_date']
      input3 = answers3['Flight_departure']
      input4 = answers3['Flight_arrival']
      Insert_flight(input1, input2, input3, input4)

  #Delete process  
  elif answers1['operation'] == "Delete data":
    questions2 = [
    inquirer.List('datatable',
      message="Which table do you need to delete?",
      choices=['Pilot', 'Aircraft', 'Flight'],),  
  ]
    answers2 = inquirer.prompt(questions2)
    if answers2['datatable'] == "Pilot":
      questions3 = [
      inquirer.Text('Pilot_ID', message="Which Pilot_ID do you need to delete? ex: 123"),
  ]
      answers3 = inquirer.prompt(questions3)

      input1 = answers3['Pilot_ID']
      Delete_pilot(input1)

    elif answers2['datatable'] == "Aircraft":
      questions3 = [
      inquirer.Text('Aircraft_ID', message="Which Aircraft_ID do you need to delete? ex: 123"),
  ]
      answers3 = inquirer.prompt(questions3)

      input1 = answers3['Aircraft_ID']
      Delete_aircraft(input1)

    elif answers2['datatable'] == "Flight":
      questions3 = [
      inquirer.Text('Flight_ID', message="Which Flight_ID do you need to delete? ex: 123"),
  ]
      answers3 = inquirer.prompt(questions3)

      input1 = answers3['Flight_ID']
      Delete_flight(input1)

  #Update process
  elif answers1['operation'] == "Update data":
    questions2 = [
    inquirer.List('datatable',
      message="Which table do you need to update?",
      choices=['Pilot', 'Aircraft', 'Flight'],),  
  ]
    answers2 = inquirer.prompt(questions2)

    if answers2['datatable'] == "Pilot":    
      questions3 = [
      inquirer.Text('Pilot_ID', message="Which Pilot_ID do you need to update? ex: 123"),
      inquirer.List('Pilot_list', 
      message="Which information do you need to update?", 
      choices=['Pilot_name', 'Pilot_age'],),
      inquirer.Text('Pilot_change', message="Please insert the new value"),
  ]
      answers3 = inquirer.prompt(questions3)

      input1 = answers3['Pilot_ID']
      input2 = answers3['Pilot_list']
      input3 = answers3['Pilot_change']
      Update_pilot(input1, input2, input3)

    elif answers2['datatable'] == "Aircraft":    
      questions3 = [
      inquirer.Text('Aircraft_ID', 
      message="Which Aircraft_ID do you need to update? ex: 123"),
      inquirer.List('Aircraft_list', 
      message="Which information do you need to update?",
      choices=['Aircraft_type', 'Aircraft_company'],),
      inquirer.Text('Aircraft_change',
      message="Please insert the new value"),
  ]
      answers3 = inquirer.prompt(questions3)

      input1 = answers3['Aircraft_ID']
      input2 = answers3['Aircraft_list']
      input3 = answers3['Aircraft_change']
      Update_aircraft(input1, input2, input3)    


    elif answers2['datatable'] == "Flight":    
      questions3 = [
      inquirer.Text('Flight_ID', message="Which Flight_ID do you need to update? ex: 123"),
      inquirer.List('Flight_list', 
      message="Which information do you need to update?",
      choices=['Flight_date', 'Flight_departure', 'Flight_arrival'],),
      inquirer.Text('Flight_change',                    message="Please insert the new value"),
  ]
      answers3 = inquirer.prompt(questions3)

      input1 = answers3['Flight_ID']
      input2 = answers3['Flight_list']
      input3 = answers3['Flight_change']
      Update_flight(input1, input2, input3)




def main(): 
  run()

if __name__ == "__main__": 
  while True:
      main()