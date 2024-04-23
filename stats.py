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


#calculate rating for wing back position

#calculate most preferred stats
stats_data['wb_essential'] = (stats_data['Spd'] + stats_data['Work'] + stats_data['Cro']) * 5

#calculate required stats rating
stats_data['wb_core'] = (stats_data['Dri'] + stats_data['Tck'] + stats_data['Tec'] + stats_data['Otb']
 + stats_data['Tea']) * 3

#calculate useful stats rating
stats_data['wb_secondary'] = (stats_data['Fir'] + stats_data['Mar'] + stats_data['Pas'] + stats_data['Ant']
+ stats_data['Cnt'] + stats_data['Dec'] + stats_data['Fla'] + stats_data['Pos'] + stats_data['Agi'] + stats_data['Bal'])

#Calculate final average for fullback rating
stats_data['fb'] = (stats_data['wb_essential'] + stats_data['wb_core'] + stats_data['wb_secondary']) / 40


#Calculate rating for centre back position

#calculate most preferred stats
stats_data['cb_essential'] = (stats_data['Hea'] + stats_data['Jum'] + stats_data['Ant'] + 
        stats_data['Dec'] + stats_data['Pos']) * 5

#calculate rating for required stats
stats_data['cb_core'] = (stats_data['Mar'] + stats_data['Tck'] + stats_data['Str']) * 3

#calculate rating for useful stats
stats_data['cb_secondary'] = (stats_data['Dri'] + stats_data['Fir'] + stats_data['Pas'] + stats_data['Tec']
+ stats_data['Agg'] + stats_data['Bra'] + stats_data['Spd'] + stats_data['Work'] + stats_data['Agi']
+ stats_data['Cnt'])

#calculate final average rating for centre back
stats_data['cb'] = (stats_data['cb_essential'] + stats_data['cb_core'] + stats_data['cb_secondary']) / 45
