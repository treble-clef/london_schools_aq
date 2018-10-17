###############################
## Interactive Data Analysis ##
###############################
## The london_schools_aq module allows for the user to interactively select a specific city or school type to get the average NO2 level.
## User please remember to change the file location in line 5 to your own.

def london_schools_aq():
  import numpy as np
  import pandas as pd
  ## Change file location to yours:
  file = "C:/Users/mayda/Downloads/Schools_ParliamentaryConstituencies.csv"
  df = pd.read_csv(file)
  startpage = {"A":" NO2 Levels by City", "B":" NO2 Levels by School Type"}
  cities = {"a":"Barking and Dagenham", "b":"Barnet", "c":"Bexley", "d":"Brent", "e":"Bromley", 
  "f":"Camden", "g":"Croydon", "h":"Ealing", "i":"Enfield", "j":"Greenwich", "k":"Hackney",     
  "l":"Hammersmith and Fulham", "m":"Haringey", "n":"Harrow", "o":"Havering", "p":"Hillingdon", 
  "q":"Hounslow", "r":"Islington", "s":"Kensington and Chelsea", "t":"Kingston upon Thames", 
  "u":"Lambeth", "v":"Lewisham", "w":"City of London", "x":"Merton", "y":"Newham", "z":"Redbridge", 
  "aa":"Richmond upon Thames", "bb":"Southwark", "cc":"Sutton", "dd":"Tower Hamlets", 
  "ee":"Waltham Forest", "ff":"Wandsworth", "gg":"Westminster"}
  schooltypes = {"a":"Academy 16-19 Converter", "b":"Academy Alternative Provision Converter", 
  "c":"Academy Alternative Provision Sponsor Led", "d":"Academy Converter", "e":"Academy Special Converter", 
  "f":"Academy Special Sponsor Led", "g":"Academy Sponsor Led", "h":"City Technology College", 
  "i":"Community School", "j":"Community Special School", "k":"Foundation School", 
  "l":"Foundation Special School", "m":"Free Schools", "n":"Free Schools - 16-19", 
  "o":"Free Schools - Alternative Provision", "p":"Free Schools Special", "q":"Further Education",
  "r":"Higher Education Institutions", "s":"LA Nursery School", "t":"Non-Maintained Special School", 
  "u":"Other Independent School", "v":"Other Independent Special School", "w":"Pupil Referral Unit",
  "x":"Sixth Form Centres", "y":"Special Post 16 Institution", "z":"Studio Schools", 
  "aa":"University Technical College", "bb":"Voluntary Aided School", "cc":"Voluntary Controlled School",
  "dd":"Miscellaneous"} 
  print("")
  print("    WELCOME TO THE LONDON SCHOOLS ENVIRONMENTAL AIR QUALITY DATASET.")
  print("")
  print("The following data analysis options are available:")
  for key in startpage:
    print(key, ":", startpage[key])
  print("")
  inputoption1 = input("What do you want to analyze? (enter letter choice, case sensitive) ")
  print("")
  for key in startpage:
    if inputoption1 in startpage:
      print("You have chosen option: %s" %inputoption1)
      break
    else:
      print("You have chosen an invalid option. Please select again.")
      print("")
      inputoption1 = input("What do you want to analyze? ")
  if inputoption1 == "A": 
    print("")
    print("The following cities are available:")
    input("(press Enter to view cities...)")
    for key in cities:
      print(key, ":", cities[key])
    inputoption2 = input("Select a city to analyze (enter letter choice, case-sensitive letter):")
    for key in cities:
      if inputoption2 in cities:
        print("")
        inputcity = df["Local Authority name"] == cities[inputoption2]
        df2 = df[inputcity]
        cityavg = df2["NO2ug/m3 mean 2013"].mean()
        print("The average NO2 ug/m3 value for %s is: %.2f" %(cities[inputoption2], cityavg))
        break
      else:
        print("You have chosen an invalid option. Please select again.")
        print("")
        inputoption2 = input("Select a city to analyze (case-sensitive letter): ")
  elif inputoption1 == "B":
    print("")
    print("The following school types are available:")
    input("(press Enter to view school types...)")
    for key in schooltypes:
      print(key, ":", schooltypes[key])
    inputoption3 = input("Select a school type to analyze (letter): ")
    for key in schooltypes:
      if inputoption3 in schooltypes:
        print("")
        inputschool = df["Type of Establishment"] == schooltypes[inputoption3]
        df3 = df[inputschool]
        schoolavg = df3["NO2ug/m3 mean 2013"].mean()
        print("The average NO2 ug/m3 value for %s is: %.2f" %(schooltypes[inputoption3], schoolavg))
        break
      else:
        print("You have chosen an invalid option. Please select again.")
        print("")
        inputoption3 = input("Select a school type to analyze (letter): ")
