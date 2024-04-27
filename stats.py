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

#calculate most preferred stats rating
stats_data['gk_essential'] = (stats_data['Agi'] + stats_data['Ref']) * 5

#calculate required stats rating
stats_data['gk_core'] = (stats_data['Cmd'] + stats_data['Kic'] + stats_data['1v1']
                        + stats_data['Ant'] + stats_data['Cnt'] + stats_data['Pos']) * 3

#Calculate rating for useful stats
stats_data['gk_secondary'] = (stats_data['Aer'] + stats_data['Com'] + stats_data['Fir'] + stats_data['Han']
                            + stats_data['Pas'] + stats_data['TRO'] + stats_data['Thr'] + stats_data['Vis'] + 
                            stats_data['Dec'] + stats_data['Acc'] + stats_data['Cmp'])

#Calculate final average for goalkeeper stats
stats_data['gk'] = (stats_data['gk_essential'] + stats_data['gk_core'] + stats_data['gk_secondary']) / 39


#calculate rating for wing back position

#calculate most preferred stats
stats_data['wb_essential'] = (stats_data['Spd'] + stats_data['Work'] + stats_data['Cro']) * 5

#calculate required stats rating
stats_data['wb_core'] = (stats_data['Dri'] + stats_data['Tck'] + stats_data['Tec'] + stats_data['OtB']
                        + stats_data['Tea']) * 3

#calculate useful stats rating
stats_data['wb_secondary'] = (stats_data['Fir'] + stats_data['Mar'] + stats_data['Pas'] + stats_data['Ant']
                            + stats_data['Cnt'] + stats_data['Dec'] + stats_data['Fla'] + stats_data['Pos'] +  
                            stats_data['Agi'] + stats_data['Bal'])

#Calculate final average for fullback rating
stats_data['fb'] = (stats_data['wb_essential'] + stats_data['wb_core'] + stats_data['wb_secondary']) / 40


#Calculate rating for centre back position

#calculate most preferred stats
stats_data['cb_essential'] = (stats_data['Hea'] + stats_data['SetP'] + stats_data['Ant'] + 
                                stats_data['Dec'] + stats_data['Pos']) * 5

#calculate rating for required stats
stats_data['cb_core'] = (stats_data['Mar'] + stats_data['Tck'] + stats_data['Str']) * 3

#calculate rating for useful stats
stats_data['cb_secondary'] = (stats_data['Dri'] + stats_data['Fir'] + stats_data['Pas'] + stats_data['Tec']
                            + stats_data['Agg'] + stats_data['Spd'] + stats_data['Work'] + stats_data['Agi']
                            + stats_data['Cnt'])

#calculate final average rating for centre back
stats_data['cb'] = (stats_data['cb_essential'] + stats_data['cb_core'] + stats_data['cb_secondary']) / 45


#Calculate rating for defensive midifled position

#calculate rating for essential stats
stats_data['dm_essential'] = (stats_data['Pos'] + stats_data['Tck'] + stats_data['Ant'] + stats_data['Dec']) * 5

#calculate rating for required stats
stats_data['dm_required'] = (stats_data['Cnt'] + stats_data['Tea'] + stats_data['Work']) * 3

#calculate rating for useful stats
stats_data['dm_secondary'] = (stats_data['Fir'] + stats_data['Mar'] + stats_data['Agg'] + stats_data['Cmp'] 
                              + stats_data['Str'])

#Calculate final rating for defensive midfielder
stats_data['dm'] = (stats_data['dm_essential'] + stats_data['dm_required'] + stats_data['dm_secondary']) / 34


#Calculate rating for ball-winning-midfielder

#calculate rating for essential stats
stats_data['bwm_essential'] = (stats_data['Pas'] + stats_data['Tck'] + stats_data['Cmp'] + stats_data['Dec']) * 5

#calculate rating for required stats
stats_data['bwm_required'] = (stats_data['Cnt'] + stats_data['Tea'] + stats_data['Work'] + stats_data['Spd']) * 3

#calculate rating for useful stats
stats_data['bwm_secondary'] = (stats_data['Fir'] + stats_data['Mar'] + stats_data['Agg'] + stats_data['Bra'] 
                              + stats_data['Str'])

#Calculate final rating for defensive midfielder
stats_data['bwm'] = (stats_data['bwm_essential'] + stats_data['bwm_required'] + stats_data['bwm_secondary']) / 37


#Calculate attribute rating for winger position

#calculate essential attribute rating
stats_data['w_essential'] = (stats_data['Spd'] + stats_data['Agi'] + stats_data['Cro'] + stats_data['Dri']) * 5

#calculate required attribute rating
stats_data['w_required'] = (stats_data['Tck'] + stats_data['Work']) * 3

#calculate useful attributes rating
stats_data['w_secondary'] = (stats_data['Fir'] + stats_data['Pas'] + stats_data['OtB'] + stats_data['Bal'])

stats_data['w'] = (stats_data['w_essential'] + stats_data['w_required'] + stats_data['w_secondary']) / 30

#Calculate attribute rating for STRIKER position

#calculate rating for essential attributes
stats_data['str_essential'] = (stats_data['Fin'] + stats_data['Cmp'] + stats_data['Dec'] + stats_data['Spd'] +
                               stats_data['Work']) * 5

#calculate rating for required attributes
stats_data['str_required'] = (stats_data['OtB'] + stats_data['Tck'] + stats_data['Fir'] + stats_data['Dri'] + 
                              stats_data['Ant']) * 3

#calculate rating for useful attributes
stats_data['str_secondary'] = stats_data['Pas'] + stats_data['Bal']

#Calculate final rating for STRIKER position
stats_data['str'] = (stats_data['str_essential'] + stats_data['str_required'] + stats_data['str_secondary']) / 42


#Create a new dataframe with only the data we want to view
final_ratings = stats_data[['Inf', 'Name', 'Age', 'Position', 'Personality', 'Media Handling', 'Left Foot', 'Right Foot',
                             'Av Rat', 'Height','gk', 'fb', 'cb', 'dm', 'bwm', 'w', 'str']].copy()

#export as html file for clear data viewing
final_ratings.to_html('team_ratings.html')
