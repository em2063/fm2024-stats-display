import pandas as pd #import pd for html manipulation

# Open file that holds imported team stats from football manager game
with open("stats.html", "r") as stats_file:
    player_stats = stats_file.read()

#configure pd
stats_data_list = pd.read_html(player_stats, header=0, encoding="utf-8")
stats_data = stats_data_list[0] #turn into dataframe

#calculate basic workrate factors to add into dataframe
stats_data['Spd'] = (stats_data['Acc'] + stats_data['Pac']) / 2 #Calculate speed
stats_data['Work'] = (stats_data['Wor'] + stats_data['Sta']) / 2 #Calculate Workrate
stats_data['SetP'] = (stats_data['Jum'] + stats_data['Bra'])

#calculate rating for goalkeeper position
stats_data['gk_essential'] = (stats_data['Agi'] + stats_data['Ref']) * 5 #calculate most preferred stats rating

stats_data['gk_core'] = (stats_data['Cmd'] + stats_data['Kic'] + stats_data['1v1']
 + stats_data['Ant'] + stats_data['Cnt'] + stats_data['Pos']) * 3 #calculate required stats rating

stats_data['gk_secondary'] = (stats_data['Aer'] + stats_data['Com'] + stats_data['Fir'] + stats_data['Han']
 + stats_data['Pas'] + stats_data['TRO'] + stats_data['Thr'] + stats_data['Vis'] + stats_data['Dec'] + stats_data['Acc']
 + stats_data['Cmp']) #calculate rating for useful stats

#Calculate final average for goalkeeper stats
stats_data['gk'] = (stats_data['gk_essential'] + stats_data['gk_core'] + stats_data['gk_secondary']) / 39
