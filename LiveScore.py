import requests
import json
import asyncio
import websockets

exit = False
while exit == False:
  print("---------------------------------------------------------")
  print("Welcome!, Please select the appropriate option ")
  print("A. Leagues Standing")
  print("B. Players")
  print("C. Results ")
  print("E. Exit ")
  user_input = input("Please Choose an option (A , B , C , E) : ")

  if user_input == "e" or user_input == "E":
    user_input = input("Do You Want To Close Program? (Y. yes/N. no): ")  # Clearer prompt
    if user_input == "y" or user_input == "Y":
      print("Program Closed! Have a Nice Day!")
      exit()  # Exit the program
    else:
      pass  # Continue the program loop
   

   
  elif user_input == "a" or user_input == "A":
        print ("A. Spain (2023-2024)")
        print ("B. England (2023-2024)")
        print ("C. Itally (2023-2024)")
        user_input = input ("Pls Choose a Option (A , B , C) : ")
        if user_input ==  "A" or user_input == "a":

            laliga_url = "https://apiv3.apifootball.com/?action=get_standings&league_id=302&APIkey=6498a30fee58cfd2d3bcece08eeab77a25bd3cc54f2e5a4da2ee30316f796ce8"
            laliga_response = requests.get(laliga_url)

            if laliga_response.status_code == 200:
                laliga_data = laliga_response.json()

                sorted_teams = sorted(laliga_data, key=lambda x: x.get('points', 0), reverse=True)

                print("La Liga Standings :")
                print("-----------------| Team | pts | Wins | Losses |")
                print("---------------------------------")
                
                for index, team in enumerate(sorted_teams, start=1):
                    team_name = team['team_name']
                    position = index
                    pts = team['overall_league_PTS']
                    win = team['overall_league_W']
                    losses = team['overall_league_L']
                   

                    print(f"Position: {position}. {team_name} , {pts} , {win} , {losses} ")

            else:
                print("Error: ", laliga_response.status_code)

#این کد کامنت شده با کمک gemini نوشتم و خیلی تمیز بود اما برنامه درست اجرا نشد برا همین کامنتش کردم
# def get_league_data():
#     # API URL خود را با URL واقعی جایگزین کنید
#     api_url = "https://apiv3.apifootball.com/?action=get_standings&league_id=302&APIkey=6498a30fee58cfd2d3bcece08eeab77a25bd3cc54f2e5a4da2ee30316f796ce8" 

#     try:
#         response = requests.get(api_url)
#         if response.status_code == 200:
#             data = response.json()
#             return data
#         else:
#             print("Error:", response.status_code)
#             return None
#     except Exception as e:
#         print("Error:", e)
#         return None

# def print_league_table(league_data):
#     # عناوین جدول را چاپ کنید
#     print("---------------------------------------------------------")
#     

#     print("---------------------------------------------------------")

#     # اطلاعات هر تیم را در یک ردیف چاپ کنید
#     for team in league_data["teams"]:
#         print(f"| {team['name']:15} | {team['wins']:5} | {team['losses']:5} |")

#     print("---------------------------------------------------------")



  elif user_input == "C" or user_input == "c" :
        print ("A. Laliga(2023-2024)")
        print ("B. Premier Leauge(2023-2024)")
        print ("C. SerieA(2023-2024) ")
        user_input = input ("Pls Choose a Player (A , B , C) : ")
        if user_input == "B" or user_input == "b" :
           api_key = 'bb960424cbed4beca0834bf04e37164e'  

           leagues = ['PD', 'BL1', 'PL', 'FL1', 'SA']  

        for league in leagues:
          url = f'https://api.football-data.org/v2/competitions/{league}/matches'
          headers = {'X-Auth-Token': api_key}

          response = requests.get(url, headers=headers)

          if response.status_code == 200:
             matches = response.json()['matches']
             print(f'\n Live results of the French league {league}:')
             for match in matches:
               home_team = match['homeTeam']['name']
               away_team = match['awayTeam']['name']
               result = f"{home_team} {match['score']['fullTime']['homeTeam']} - {match['score']['fullTime']['awayTeam']} {away_team}"
               print(result) 
          else:
            print('No live games found.')
        else:
          print(f'Error getting league information{league}.')


  elif user_input == "b" or user_input =="B" :
        print ("A. Antoine Griezmann")
        print ("B. jude blingham")
        print ("C. loka modric")
        user_input = input ("Pls Choose a Player (A , B , C) : ")
        if user_input == "A" or user_input == "a" :
            players_url = ("https://apiv3.apifootball.com/?action=get_players&player_name=Griezmann&APIkey=6498a30fee58cfd2d3bcece08eeab77a25bd3cc54f2e5a4da2ee30316f796ce8")
            players_response = requests.get(players_url)

            if players_response.status_code == 200:
                players_data = players_response.json()
                if isinstance(players_data, list):
                    sorted_players = sorted(players_data, key=lambda x: (x.get('player_name', ''), x.get('age', 31)))
                    print ("Player Info :")
                
                    for index, player in enumerate(sorted_players, start=1):
                        player_name = player.get ("player_name" , "")
                        player_type = player.get("player_type" , "")
                        player_age  = player.get("player_age" , "31")
                        team_name   = player.get("team_name" , "")
                        player_match_played = player.get("player_match_played" , "")
                        playr_rating = player.get("player_rating" , "9/1")
                        player_goals = player.get("player_goals" , "")
                        player_assists = player.get("player_assists" , "")


                        print (f"Name: {player_name} , Type : {player_type} , Age :{player_age} , Team : {team_name} , Rate : {playr_rating} , player match played : {player_match_played} , player goals : {player_goals} , player_assists : {player_assists}  ")
                else :
                    print("Error: Invalid data format from API.")
            else:
                print("Error: ", player_response.status_code)           