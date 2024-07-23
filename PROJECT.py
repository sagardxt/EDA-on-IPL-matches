import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# Load the fmri dataset this data is inbuild in seaborn
fmri = sns.load_dataset("fmri")

# Print the first few rows of the dataset
print(fmri.head())

sns.lineplot(x="timepoint" , y="signal" , data=fmri)
sns.lineplot(x="timepoint" , y="signal" , data=fmri , hue="event")
sns.lineplot(x="timepoint" , y="signal" , hue="event" , style="event" , markers=True , data=fmri)
print(plt.show())

#seaborn scatterplot on csv data set
iris = pd.read_csv(r'C:\Users\ASUS\Downloads\dataset.csv')
print(iris.head())

sns.scatterplot(x="Period",y="Data_value",data=iris)
print(plt.show())

#IPL DATASET
ipl = pd.read_csv(r'C:\Users\ASUS\Documents\datasets for visulaization\matches.csv')
#print first five rows and columns
print(ipl.head())
#rows and coulmns
print(ipl.shape)

#getting the frequency of man of the match
v = ipl['venue'].value_counts()
print(v)
w = ipl['winner'].value_counts()[0:10]
print(w)
#first 5 players
pom = ipl['player_of_match'].value_counts()[0:5]
print(pom)
#print only names
pom = ipl['player_of_match'].value_counts()[0:5].keys()

#barplot between the player of the match andno of player of the match
plt.figure(figsize=(8,5))
plt.bar(list(ipl['player_of_match'].value_counts()[0:5].keys()),list(ipl['player_of_match'].value_counts()[0:5]),color="g")
print(plt.show())

#getting the frequency of result coulmns
res = ipl['result'].value_counts()
print(res)

#getting the tosswinner
tw = ipl['toss_winner'].value_counts()
print(tw)

#extracting the win by runs in separate variable called as batting first
batting_first = ipl[ipl['win_by_runs']!=0]

# Assuming batting_first is a DataFrame and 'win_by_runs' is a column in it
plt.figure(figsize=(5, 7))
plt.hist(batting_first['win_by_runs'])
plt.title("Distribution of Runs")
plt.xlabel("Runs")
plt.show()

#finding out the no of the winss w.r.t each team after batting first
w = batting_first['winner'].value_counts()
print(w)

#making a bar plot for top 3 teams with most wins
plt.figure(figsize=(6,6))
plt.bar(list(batting_first['winner'].value_counts()[0:3].keys()),list(batting_first['winner'].value_counts()[0:3]),color=['blue','yellow','orange'])
print(plt.show())

#making a pie-chart
plt.figure(figsize=(6,6))
plt.pie(list(batting_first['winner'].value_counts()),labels=list(batting_first['winner'].value_counts().keys()),autopct='%0.1f%%')
print(plt.show())

#now extracting the data where teams won after batting second as a variable calle batting second
batting_second = ipl[ipl['win_by_wickets']!=0]

#histogram for frequency of wins w.r.t no of wickets
plt.figure(figsize=(7,7))
plt.hist(batting_second['win_by_wickets'],bins=30)
print(plt.show())
win = batting_second['winner'].value_counts()
print(win)

#making a bar plot for top 3 teams with most wins
plt.figure(figsize=(7,7))
plt.bar(list(batting_second['winner'].value_counts()[0:3].keys()),list(batting_second['winner'].value_counts()[0:3]),color=['red','black','orange'])
print(plt.show())

#making a pie-chart
plt.figure(figsize=(6,6))
plt.pie(list(batting_second['winner'].value_counts()),labels=list(batting_second['winner'].value_counts().keys()),autopct='%0.1f%%')
print(plt.show())

#no of matches played each seasons
season = ipl['season'].value_counts()
print(season)

#no of matches played in cities
city = ipl['city'].value_counts()
print(city)

#NEW DATASET FOR THE DELIVERIES
deliveries = pd.read_csv(r"C:\Users\ASUS\Documents\datasets for visulaization\deliveries.csv")
print(deliveries.head())

matchid = deliveries['match_id'].unique()
print(matchid)
match_1 = deliveries[deliveries['match_id']==1]
print(match_1.head())
srh = match_1[match_1['inning']==1]
print(srh.head())
br = srh['batsman_runs'].value_counts()
print(br)

#collecting the data of team RCB
rcb = match_1[match_1['inning']==2]
br = rcb['batsman_runs'].value_counts()
dk = rcb['dismissal_kind'].value_counts()
print(br)
print(dk)