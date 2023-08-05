import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup as bs
import requests


header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}

races = ["Tour de France", "Giro d Italia", "Vuelta a Espana", "Dauphine", "Paris Nice", "Tirreno Adriatico", "Volta a Catalunya", "Tour de Romandie", "Tour de Suisse"]
years = range(1993, 2024)

dfComplete = pd.DataFrame()

for race in races:
    name = race.lower().replace(' ', '-')
    for year in years:
        gc_url = f"https://www.procyclingstats.com/race/{name}/{year}/gc"
        r = requests.get(gc_url, headers=header)
        soup = bs(r.text, 'html.parser')
        # some races (catalunya 2020) didnt happen due to covid!
        head1 = soup.select_one('div[class=main]>h1')
        if head1 != None:
            print(head1.text)
            print("Page not found" in head1.text)
        if (head1 != None) and ("Page not found" in head1.text):
            continue
        cancelled = soup.select_one("div[class=text-regular]>div")
        if (cancelled != None) and ('Race is cancelled' in cancelled.text):
            print(f'race cancelled {race} {year}')
            continue
        
        tables = soup.findAll('table')
        table = tables[1]
        df_gc = pd.read_html(table.prettify())[0]
        
        df_gc['Team']=df_gc['Team'].fillna('NoTeam')
        df_gc['RiderName'] = [a.replace(b, '').strip() for a, b in zip(df_gc['Rider'], df_gc['Team'])]
        df_gc['FinalGC'] = df_gc['Rnk'].astype(int)
        df_gc = df_gc[['RiderName', 'FinalGC']]
        print(df_gc[['RiderName', 'FinalGC']][:11])
        if (soup.select_one('h1').text == "Page not found"):
            break
        for stage in range(0, 22):
            if stage == 0:
                url = f"https://www.procyclingstats.com/race/{name}/{year}/prologue"
            else:
                url = f"https://www.procyclingstats.com/race/{name}/{year}/stage-{stage}"
                
            print(url)
            r = requests.get(url, headers=header)
            soup = bs(r.text, 'html.parser')
            if (soup.select_one('h1').text == "Page not found"):
                if (stage == 0):
                    continue
                else:
                    break
                    

            if (stage > 0) and (not ('(ITT)' in soup.select_one("div>div>div>span[class=blue]").text)):
                continue
                
            print(f'Processing ITT stage {name} - stage {stage}')

            # get result tables
            tables = soup.findAll('table')
            table = tables[0]
            df = pd.read_html(table.prettify())[0]
            
            df = df[df['Avg'].notna()]
            df = df[df['GC'].notna()]
            df = df.astype({"GC": int})
            
            df['Team']=df['Team'].fillna('NoTeam')

            ul = soup.find('ul', class_='infolist')
            lis = ul.find_all('li')
            for li in lis:
                divs = li.find_all('div')
                if 'Date:' in divs[0].getText():
                    date = divs[1].getText()
                if 'Distance:' in divs[0].getText():
                    distance = divs[1].getText()
                if 'ProfileScore:' in divs[0].getText():
                    profile_score = divs[1].getText()

            df['Race'] = race
            df['Year'] = year
            df['Stage'] = stage
            df['Date'] = date
            df['Distance'] = distance
            df['ProfileScore'] = profile_score
            df['RiderName'] = [a.replace(b, '').strip() for a, b in zip(df['Rider'], df['Team'])]
            df['AvgTop10'] = (df['Avg'] / df['Avg'][:10].mean()) - 1
            df['AvgAll'] = (df['Avg'] / df['Avg'].mean()) - 1
            
            cols = df_gc.columns.difference(df.columns)
            df2 = df.join(df_gc.set_index('RiderName')[cols], on='RiderName').fillna({'FinalGC':1111})
            df2['FinalGC'] = df2['FinalGC'].astype(int)
            df2 = df2[['Rnk', 'GC', 'FinalGC', 'RiderName', 'Age', 'Specialty', 'Team', 'Avg', 'Race', 'Year', 'Stage', 'Date', 'Distance', 'ProfileScore', 'AvgTop10', 'AvgAll']]
            
            dfComplete = pd.concat([dfComplete, df2])
            
            
            if ('(Final)' in soup.select_one("div>div>div>span[class=blue]").text):
                # last stage
                break

            #ax = df.plot.hist(column=['AvgTop10', 'AvgAll'], bins=12, alpha=0.5, range=[min(df['AvgTop10'].min(), df['AvgAll'].min()), max(df['AvgTop10'].max(), df['AvgAll'].max())])
            #plt.show()
path = r'C:\Users\aleks\Desktop\\'
dfComplete.to_csv(path+'ITT_complete.csv', index=False)
#dfComplete.to_csv(path+'ITT2.csv', mode='a', index=False, header=False)