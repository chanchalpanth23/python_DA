#pandas-> excel features(data read,filter,visualize)
#DataFrame-> allow raw data convert into excel like sheet


# data={
#     "name":["a","b","c"],
#     "age":[10,32,12]
# }
# df=pd.DataFrame(data)
# print(df)
# print(df.head(1))                 #start from top(indexing start from 1)
# print(df.tail(2))                 #start from bottom
# print(df.shape)  
# print(df.columns)
# print(df["age"]>18)    
# df["modified_age"]= df["age"]+2
# print(df)  
#loc->for print exact value
# print(df.loc[1,"name"])

#max,min,mean
# print(df["age"].max())
# print(df["age"].min())
# print(df["age"].mean())

#sorting(ascending-descending)
# data={
#     "name":["a","b","c"],
#     "age":[20,22,20],
#     "marks":[88,34,78]
# }
# df=pd.DataFrame(data)
# df=df.sort_values("age")
# print(df)
# df=df.sort_values("name",ascending=False)
# print(df)
# df=df.sort_values(["age","marks"])   #indexing does'nt change in sorting
# print(df)

#sort index-> customized index
# df=pd.DataFrame(data,index=[2,0,1])
# print(df)
# df=df.sort_index()
# print(df)
#PD SERIES-> 1 dimensional table create(single columnn but multiple rows)
# df2=pd.Series([10,12,3,4])
# print(df2)
#   
#groupby
# data={
#     "students":["a","b","a","c","b","a","c","b","c"],
#     "marks":[20,34,12,67,90,45,68,38,50]
# }
# df=pd.DataFrame(data)
# print(df)
# print(df.groupby("students")["marks"].sum())
# sum->aggregrate function(multiple value into single)
#APPLY FUNCTION

# data={
#     "employee":["chanchal","charu","chitra"],
#     "department":["HR","manager","teacher"],
#     "salary":[35000,25000,30000]
# }
# df=pd.DataFrame(data)
# # print(df)
# def increase(sal):
#     return(sal*1.10)
# df["increment"]= df["salary"].apply(increase)
# print(df)
# import pandas as pd
# matches= pd.read_csv("IPL_Matches_2008_2022.csv")
# print(matches)
# scores= pd.read_csv("IPL_Ball_by_Ball_2008_2022.csv")
# print(scores)
# print(scores.head(1))
# print(matches.head(1),matches.tail(1))
# filtered_data= matches[matches["WinningTeam"]=="Kolkata Knight Riders"]
# print(filtered_data["WinningTeam"])
# filtered_data=matches[matches["TossWinner"]==matches["WinningTeam"]]
# print(filtered_data)
# print(filtered_data.shape[0])
# filtered_data=matches[matches["TossWinner"]==matches["WinningTeam"]].value_counts()
# print(filtered_data)
# print(matches.columns,matches.shape)

# print(scores.groupby("batter")["batsman_run"].sum())
# total=len(matches)

# data=len(matches[matches["WinningTeam"]=="Royal Challengers Bangalore"])
# print(data)
# Winningpercentage=(data/total)*100
# print(Winningpercentage)
    
# def checkstatus(runs):
#     if runs>100:
#         return "high runs"
#     else:
#         return " low runs"
# runsByBatters=scores.groupby("batter")["batsman_run"].sum().reset_index()
# runsByBatters["status"]=runsByBatters["batsman_run"].apply(checkstatus)
# print(runsByBatters)
#aese batsman ke name jiske highest run top 10 descending order
# top_ten=scores.groupby("batter")["batsman_run"].sum().sort_values(ascending=False).head(10)
# print(top_ten)
#batter ke total run ,total run ka mean,max,min
# run=scores.groupby("batter")["batsman_run"].agg(
#     total_run="sum",
#     max_run="max",
#     mean_run="mean",
#     min_run="min",
# )
# print(run)

#strike rate of batsman
# runs=scores.groupby("batter")["batsman_run"].sum()
# balls=scores.groupby("batter")["ballnumber"].count()
# Strike_rate=(runs/balls)*100
# print(Strike_rate)

#top batsman with most sixes
# top_sixes=scores[scores["batsman_run"]==6].groupby("batter")["batsman_run"].count().sort_values(ascending=False)
# print(top_sixes.head(10))

#top batsman with most fours
# top_fours=scores[scores["batsman_run"]==4].groupby("batter")["batsman_run"].count().sort_values(ascending=False)
# print(top_fours)

#no. of sixes by batsman
# sixes= scores[scores["batsman_run"]==6].groupby("batter")["batsman_run"].count()
# print(sixes)

#no. of four by batsman
# fours= scores[scores["batsman_run"]==4].groupby("batter")["batsman_run"].count()
# print(fours)

#total balls played by each batsman
# balls=scores.groupby("batter")["ballnumber"].count()
# print(balls)

#highest single-ball runs by each batsman
# max_runs= scores.groupby("batter")["batsman_run"].max()
# print(max_runs)

#top 5 bowlers with wicket
# wickets=scores[scores["isWicketDelivery"]==1].groupby("bowler")["isWicketDelivery"].count().sort_values(ascending=False).head(5)
# print(wickets)

#teamwise totalrun
# total_run=scores.groupby("BattingTeam")["total_run"].sum()
# print(total_run)

#highest score by batsman in one match
# highest_score=scores.groupby("batter")["batsman_run"].sum().sort_values(ascending=False)
# print(highest_score)

#economy rate of bowler
# runs=scores.groupby("bowler")["total_run"].sum()
# balls=scores.groupby("bowler")["ballnumber"].count()
# economy=(runs/balls)*6

#death overs me sbse jyda run kis bowler ne diye
# death_overs= scores[scores["overs"]>=16]
# death_runs=death_overs.groupby("bowler")["total_run"].sum().sort_values(ascending=False).head(10)
# print(death_runs)

#powerplay mehighest strike rate batsman
# (powerplay=over 1-6)
# pp=scores[scores["overs"]<=6]
# runs=scores.groupby("batter")("batsman_run").sum()
# balls=scores.groupby("batter")("ballnumber").count()
# strike_rate=(runs/balls)*100
# print(strike_rate.sort_values(ascending=False).head(10))

#win percentge of each team
# matches=matches.groupby("Team1")["ID"].nunique()+matches.groupby("Team2")["ID"].nunique()
# wins=matches["WinningTeam"].value_counts()
# win_percentage=((wins/matches)*100).sort_values(ascending=False)
# print(win_percentage)

#total wins of each team
# wins=matches["WinningTeam"].value_counts()
# print(wins)

#matches won by batting first
# bat_first= matches[matches["WonBy"]=='Runs']
# print(bat_first.shape[0])

#matches won by bowling first
# bowling_first=matches[matches["WonBy"]=='Wickets']
# print(bowling_first)

#total tosswinner of each team
# print(matches["TossWinner"].value_counts())

#player with most player of the match awards
# most_player=matches["Player_of_Match"].value_counts().head(1)
# print(most_player)

#Average victory margins by runs
# run_wins=matches[matches["WonBy"]=='Runs']
# print(run_wins['Margin'].mean())
#TEAM THAT NEVER WON IPL TROPHY
# champions=matches.groupby('Season').last()['WinningTeam']
# all_teams= set(matches['Team1']).union(set(matches['Team2']))
# never_won=all_teams-set(champions)
# print(never_won)
#top 5 venues with maximum matches
# max_match=matches['Venue'].value_counts().head(5)
# print(max_match)

# battingteam=scores.groupby("BattingTeam")["innings"].count()
# print(battingteam)

# wins=matches["WinningTeam"].value_counts().sort_values().sort_values(ascending=False)
# print(wins)


#PIVOT TABLE->columns ko allow krta h row me use krne ke liye
# pt=scores.pivot_table(
#     values="total_run",
#     index="BattingTeam",
#     aggfunc="mean"
# )
# print(pt)

# pd.set_option('display.max_columns',None)
# pd.set_option('display.max_rows',None)


# pt= scores.pivot_table(
#     index="batter",
#     columns="bowler",
#     values="batsman_run",
#     aggfunc="sum"
# )
# print(pt.head(5))

# pt=scores.pivot_table(
#     values="batter",
#     index="batsman_run",
#     aggfunc="sum"
    
# )
# print(pt)
#at least 2 pivot tables #dataframe(data filtering,new column,data sort,value_count,apply fn)

# data={
#     "name":['chanchal','harshita','kavish','charu'],
#     "Department":['IT','HR','Manager','Teacher'],
#     "Salary":[40000,25000,35000,25000]
# }
# df= pd.DataFrame(data)
# filtering_data=df[df["Department"]=='HR']
# print(filtering_data)

# df["bonus"]=df['Salary']*1.1

# df=df.sort_values(["Salary"])
# print(df)
# data={
#     "student":['A','B','C','D'],
#     "subject":['maths','english','science','hindi'],
#     "marks":[80,78,82,90]
# }
# df=pd.DataFrame(data)

# print(df)
# def increase(marks):
#     return(marks*1.10)
# df["increment"]= df["marks"].apply(increase)
# print(df)

# pivot=pd.pivot_table(
#     df,
    
#     values='marks',
#     index='student',
#     columns='subject',
#     aggfunc='mean'
# )
# print(pivot)
# import numpy as np
# import pandas as pd

# df=pd.DataFrame({
#     "name":["chanchal","ritika","charu","ishant","None"],
#     "age":[22,19,None,np.nan,110],
#     "salary":[10000,20000,5000,2500,50000]
# })
# print(df.isnull()) 
# print(df.isnull().sum())        # column wise run
# print(df)
# print(df.notnull())
# print(df.dropna())            # row remove if coumnn have none
# df.fillna({
#     "name": "abc",
#     "age":0,
#     "salary":0
#     },inplace=True)  
# print(df)
   #original table ko remove krne ke liye inplace true
# print(df.dropna(subset=["name"]))
# print(df["age"].fillna(df["age"].mean()))    #mean-> use for if outlier not have
# print(df["age"].fillna(df["age"].median()))
# df=pd.DataFrame({
#     "name":["chanchal",'ritika',"saifi","gaurav","ishant","None","ishant","chanchal"],
#     "age":[22,19,None,np.nan,20,110,20,22],
#     "salary":[10000,20000,5000,2500,50000,7,10000,10000]
# })
# print(df.duplicated())
# print(df.drop_duplicates(subset=["name"]))          #subset-> name column me duplicate wo drop kr dega
# df=pd.DataFrame({
#     "name":["chanchal",'ritika',"saifi","gaurav","ishant","None","ishant","chanchal"],
#     "age":[22,19,20,24,20,110,20,22],
#     "salary":[10000,20000,5000,2500,50000,7,10000,10000]
# })
# df["ageinc"]  = [df["age"]>20]
# 20< -> senior
# 20> junior

# def age(gap):
#      if ("age is lesser than 20"):
#        print("senior")
#      else:("age is greater than 20")
#      print("senior")
#      return
# df["age"]= df["age"].applyfn("gap")
# print(df)

# df=pd.DataFrame({
#     "name":["chanchal panth",'ritika sharma',"saifi sharma","gaurav sharma","ishant sharma","abc sharma ","ishant sharma","chanchal sharma"],
#     "age":[22,19,20,24,20,110,20,22],
#     "salary":[10000,20000,5000,2500,50000,7,10000,10000],
#     "email":["abc@gmail.com","abc@gmail.com","abc@gmail.com","abc@gmail.com","abc@gmil.com","abc@gmail.com","abc@gmail.com","abc@gmail.com"]
# })
# print(df)
# df["name"]= df["name"].str.strip()                 # spaces remove karta hai
# df["name"] = df["name"] .str.title()                # first letter capital kr dega
# df.replace("Abc","def",inplace=True)
# print(df)
# print(df["email"].str.contains("@gmail.com"))
# print(df["name"].str.isnumeric())
# print(df["name"].str.isalnum())
# print(df)
# df["name"]=df["name"].str.split().str.get(0)
# print(df)


#merge

# df1=pd.DataFrame({
#     'id':[1,2,3],
#     'name':["chanchal","charu","kavish"],
# })
# df2=pd.DataFrame({
#     'id':[1,2,4],
#     'marks':[80,92,89]
# })
# df3=pd.merge(df1,df2,on='id',how='inner')    #inner join only on=common
# df3=pd.merge(df1,df2,on='id',how='outer')
# print(df3)
# df1=pd.DataFrame({
#     'id':[1,2,4],
#     'name':["chanchal","charu","kavish"],
# })
# df2=pd.DataFrame({
#     'id':[1,2,3],
#     'marks':[80,92,89]
# })
# df3=pd.merge(df1,df2,on='id',how='left')
# print(df3)
# df3=pd.merge(df1,df2,on='id',how='right')
# print(df3)
    
# df1=pd.DataFrame({
#      'name':["chanchal","charu"],
#     'index':[1,2],
# })
# df2=pd.DataFrame({
#     'marks':[80,92],
#     'index':[1,2],
# })
# result=df1.join(df2)
# print(result)
# data={
#     "name":["charu","chanchal","kavish"],
#     "marks":[78,86,90]
# }
# df=pd.DataFrame(data)

# df['upper_name']=df['name'].apply(lambda x:x.upper())
# print(df)

# df=pd.DataFrame({
#     'Number':[20,23,56,23]
# })
# df['type']=df['Number'].apply(lambda x:'even' if x%2==0 else 'odd')
# print(df)

# df=pd.DataFrame({
#     'Price':[100,20,45],
#     'Quantity':[3,7,3]

# })
# df['total']=df.apply(lambda x:x['Price']*x['Quantity'],axis=1)
# print(df)

#-> basic graph bnane ki library hai web based
# shop ki monthly sale dekhna

#seaborn-> matplotlib graph ka stylish version hai.ye automatically sundar graph banata hai aur data analysis me use hota hai.
#students ke marks ko compare krneke liye(attractive visually)

#plotly -> interactive graph bnanata h.graph ko zoom,move hover kar skte ho(3-d graph ke liye best h)

import matplotlib.pyplot as plt

# x=[10,20,30,40]
# y=[1,2,3,4]
# plt.plot(x,y,marker="*",linestyle="--")
# plt.title("x-y chart")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.show()

# name=["charu","chanchal","utkarsh","Ishant","chirag"]
# marks=[80,90,78,85,60]
#  plt.plot(name,marks,marker=".",linestyle=":")
# bars=plt.bar(name,marks,width=0.3,color="orange",edgecolor="black",hatch="/")
# for i in bars:
#     a=i.get_height()
#     plt.text(i.get_x()+2, a+1,a)
# plt.title("result chart",fontsize=26,fontstyle="italic")
# plt.xlabel("name")
# plt.ylabel("marks")
# plt.pie(marks,labels=name)
# x=[2,4,7,1,23,56]
# plt.hist(x,bins=7)

# plt.show()
# fig=plt.figure()
# plt.plot([1,2,3],[4,5,6])
# plt.show()
# x=["a","b","c","d","e","f","g","h","i","j"]
# y=[10,20,30,40,50,60,70,80,90,100]
# plt.plot(x,y)
# x_highest=max(x)
# y_highest=max(y)
# x_lowest=min(x)
# x_lowest=min(y)
# plt.annotate("highest",(x_highest),y_highest)
# plt.annotate("lowest,(x_lowest,y_lowest)")
# plt.text(x_highest,y_highest,"highest")
# plt.show()

# data=[10,12,15,18,20,22,25,118,56]
# plt.boxplot(data)
# plt.show()

#IQ->interquartile range
# import pandas as pd

# data= snb.load_dataset("flights")
# print(data.head(5))
# bar=snb.barplot(x="month",y="passengers",data=data,errorbar=None)
# data={
#     "x":[10,20,30,40,50],
#     "y":[100,20,300,30,500]
# }
# df=pd.DataFrame(data)
# snb.heatmap(df.corr())
# plt.show()
#positive correlation-> light
#negative-> dark
# import pandas as pd
# import seaborn as snb
# data={
#     "x":[1,2,3,4,5],
#     "y":[10,25,30,30,50]
# }
    
# df=pd.DataFrame(data)
# snb.scatterplot(data=data,x="x",y="y")
# # snb.heatmap(df.corr(),annot=True)
# plt.show()

#ewm
# [1,2,3,4]

import seaborn as snb
import pandas as pd
import numpy as np

# print(pd.Series([1,2,3,4]).ewm(alpha=0.7).mean())
#scatterplot->
# data={
#     "sex":["female","female","male","female","male"],
#     "bills":[10000,21000,14200,20000,10000],
#     "tips":[100,107,43,30,109]
# }
# df=pd.DataFrame(data)
# snb.scatterplot(data=data,x="bills",y="tips",hue="sex",palette={
#     "female":"pink",
#     "male":"blue"
# plt.plot([10000,21000,14200,20000,10000],[100,150,40,300,130])
# snb.lineplot(data=data,x="bills",y="tips")


# plt.show()
# data=[10,20,23,12,3,22]
# snb.kdeplot(data)
# plt.show()

# fig,ax=plt.subplots(2,2)
# ax[0,0].plot([1,2,3],[10,20,30])
# ax[0,1].pie([10,30,50,60])
# ax[1,0].bar([1,2,3,4],[10,45,78,90])
# ax[1,1].hist([1,1,1,2,2,3,3,4])
# plt.show()

# tips2=snb.load_dataset("tips")
# print(tips2.tail(5))
# snb.regplot(x="total_bill",y="tip",data=tips2)
# snb.countplot(x="sex",data=tips2)
# snb.jointplot(x="total_bill",y="tip",data=tips2)
# snb.clustermap(tips2.corr(numeric_only=True),annot=True)
# plt.show()

