from bs4 import BeautifulSoup #import Beautiful soup for html manipulation file

# Open file that holds imported team stats from football manager game
with open("stats.html", "r") as stats_file:
    player_stats = stats_file.read()

#configure bs
soup = BeautifulSoup(player_stats, 'html.parser')

stats_table = soup.find('table')
table_header = stats_table.find_all("tr")[0]
table_columns = table_header.find_all("th")
