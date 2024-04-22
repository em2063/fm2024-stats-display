import pandas as pd #import pd for html manipulation

# Open file that holds imported team stats from football manager game
with open("stats.html", "r") as stats_file:
    player_stats = stats_file.read()

#configure pd
stats_data_list = pd.read_html(player_stats, header=0, encoding="utf-8")
stats_data = stats_data_list[0]