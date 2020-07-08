import pandas as pd

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index) 
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
def answer_one():
    return df['Gold'].idxmax()
print(answer_one())

def answer_two():
    summer = df['Gold']
    winter = df['Gold.1']
    delt = summer - winter
    return delt[delt == max(delt)].index[0]
print(answer_two())

def answer_three():
    f1 = df[df['Gold']>0]
    f2 = f1[f1['Gold.1']>0]
    summer = f2['Gold']
    winter = f2['Gold.1']
    total = summer + winter
    relative = (summer - winter) / total
    return relative[relative == max(relative)].index[0]
print(answer_three())

def answer_four():
    Points = df['Gold.2'] * 3 + df['Silver.2'] * 2 + df['Bronze.2'] * 1
    return Points
print(answer_four())

census_df = pd.read_csv('census.csv')


def answer_six():
    f1 = census_df[census_df['SUMLEV'] == 50].groupby('STNAME')['CENSUS2010POP'].apply(lambda x: x.nlargest(3).sum()).nlargest(3).index.values.tolist()
    return f1
print(answer_six())

def answer_seven():
    f1 = census_df[census_df['SUMLEV'] == 50].set_index(['STNAME','CTYNAME']).loc[:,['POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']].stack()
    f2 = f1.max(level=['STNAME','CTYNAME']) - f1.min(level=['STNAME','CTYNAME'])
    return f2.idxmax()[1]
print(answer_seven())

def answer_eight():
    f1 = census_df[(census_df['POPESTIMATE2015'] > census_df['POPESTIMATE2014']) & ((census_df['REGION'] == 1) | (census_df['REGION'] == 2))]
    f1 = f1[f1['CTYNAME'].str.startswith('Washington')]
    return f1.loc[:,['STNAME', 'CTYNAME']]
print(answer_eight())