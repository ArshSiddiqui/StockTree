import sqlite3

connection = sqlite3.connect('StockTreeDB.db')
c = connection.cursor()

# COMPANY DATA INSERTION

list_company_names = ["'JPMorgan Chase'", "'Saudi Aramco'", "'Industrial and Commercial Bank of China'", "'China Construction Bank'", "'Agricultural Bank of China'", "'Bank of America'", "'ExxonMobil'", "'Shell'", "'Bank of China'", "'Toyoto Motor'", "'Samsung Electronics'", "'UnitedHealth Group'", "'Ping An Insurance Group'", "'Wells Fargo'", "'Chevron'", "'Petro China'", "'HSBC Holdings'"]

list_company_industry = ["'Financial Services'", "'Oil Producer'", "'Financial Services'", "'Financial Services'", "'Financial Services'", "'Financial Services'", "'Oil Producer'", "'Oil Producer'", "'Financial Services'", "'Automotive Industry'", "'Technlogy'", "'Healthcare'", "'Insurance'", "'Financial Services'", "'Oil Producer'", "'Oil Producer'", "'Financial Services'"]

list_company_abbreviation = ["'jpm'", "'2222'", "'idcbf'", "'cichy'", "'acgbf'", "'bac'", "'xom'", "'shel'", "'bachy'", "'tm'", "'005930'", "'unh'", "'pngay'", "'wfc'", "'cvx'", "'pccyf'", "'hsbc'"]

list_company_ceos = ["'Jamie Dimon'", "'Amin H. Nasser'", "'Chen Siqing'", "'Tain Guoli'", "'Gu Shu'", "'Brian Moynihan'", "'Darren Woods'", "'Wael Sawan'", "'Liu Liange'", "'Koji Sato'", "'Kye-Hyun Kyung'", "'Andrew Witty'", "'Xie Yonglin; Jessica Tan'", "'Charles W. Scharf'", "'Mike Wirth'", "'Zhou Jiping'", "'Noel Quinn'"]

#for i in range(0, len(list_company_names)):
#  print(list_company_names[i])
#    c.execute("INSERT INTO COMPANY VALUES ("+list_company_ceos[i]+", "+list_company_industry[i]+", "+list_company_abbreviation[i]+", "+list_company_names[i]+")")

# COUNTRY DATA INSERTION

list_country_names = ["'Panama'", "'Peru'", "'Brazil'", "'Argentina'", "'Spain'", "'The United Kingdom'", "'Ethiopia'", "'Pakistan'", "'Bangladesh'", "'Nepal'", "'Japan'", "'South Korea'", "'Malaysia'", "'Egypt'", "'Saudi Arabia'"]

list_country_unemployment_rate = [8.79, 3.66, 9.46, 6.49, 11.6, 4.3, 4.02, 6.42, 4.70, 11.12, 2.64, 2.3, 3.4, 7.00, 5.64]

list_country_gdps = [63610000000, 232200000000, 1609000000000, 487200000000, 1427000000000, 3131000000000, 111300000000, 348300000000, 416300000000, 36290000000, 4941000000000, 1811000000000, 373000000000, 404100000000, 833500000000]

list_country_inflation_rate = [2.86, 5.04, 3.2, 138.0, 2.4, 6.7, 28.8, 31.4, 7.7, 7.6, 3.3, 3.7, 2.0, 39.7, 1.7]

# for i in range(0, len(list_country_names)):
#    print(list_country_names[i])
#    c.execute("INSERT INTO COUNTRY VALUES ("+str(list_country_unemployment_rate[i])+", "+str(list_country_gdps[i])+", "+list_country_names[i]+", "+str(list_country_inflation_rate[i])+")")

# EMPLOYEE NAME INSERTION

empl_fname = ["'Arsh'", "'Namita'", "'Vaishnavi'", "'Jessie'", "'John'", "'Adam'", "'Aidan'","'Matt'","'Ahmed'","'Alex'","'Andrew'","'Andy'","'Angeline'","'Brian'","'Cedric'","'Christeana'","'Connor'","'Chelsea'","'Caleb'","'David'"]
empl_minit = ["'M'", "''", "''", "''", "'A'", "'B'", "'C'", "'D'", "'E'","'F'", "'G'", "'H'", "'J'","'K'", "'L'", "'M'", "'N'", "'O'","'P'", "'Q'"]
empl_lname = ["'Siddiqui'", "'Shashidar'", "'Alavala'", "'Dertke'", "'Johnson'", "'Smith'", "'Frost'", "'Singh'", "'Xu'", "'Azim'", "'Williamson'", "'Phuong'", "'Eggeman'", "'West'", "'White'", "'Hughes'", "'Arkellian'", "'Julia'", "'Alvari'", "'Soliman'"]
empl_ssn = ["'000000000'", "'000000001'", "'000000002'", "'000000003'", "'000000004'", "'000000005'", "'000000006'", "'000000007'", "'000000008'", "'000000009'", "'000000010'", "'000000011'", "'000000021'", "'000000031'", "'000000041'", "'000000051'", "'000000061'", "'000000071'", "'000000081'", "'000000091'"]
empl_addr = ["'1401 S State St'", "'222 N Main St'", "'333 N Main St'","'444 N Main St'", "'111 S Main Street'", "'1200 N State St'", "'14 S Wabash St'", "'77 W Wacker Drive'", "'140 N Clark St'", "'20 S Cicero Ave'","'600 S Michigan Ave'", "'140 Lake Shore Dr'", "'200 North Wells St'", "'4000 S Cermak St'", "'12 N Damen Dr'", "'1700 S Damen Dr'", "'300 W Logal Blvd'", "'200 S Addison St'", "'14 W Randolph St'","'200 W Randolph St'"]
empl_num =  ["'000000000'", "'000000001'", "'000000002'", "'000000003'", "'000000004'", "'000000005'", "'000000006'", "'000000007'", "'000000008'", "'000000009'", "'000000010'", "'000000011'", "'000000021'", "'000000031'", "'000000041'", "'000000051'", "'000000061'", "'000000071'", "'000000081'", "'000000091'"]
empl_salary = [0, 0, 0, 0, 0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
empl_id = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
empl_cname = ["'Databses Limited'","'Databses Limited'","'Databses Limited'","'Databses Limited'","'Databses Limited'","'Agricultural Bank of China'","'Agricultural Bank of China'","'Agricultural Bank of China'","'Agricultural Bank of China'", "'Samsung'", "'Samsung'", "'Samsung'", "'Samsung'", "'Samsung'", "'Samsung'","'Wells Fargo'","'Wells Fargo'","'Wells Fargo'","'Wells Fargo'","'Wells Fargo'"]

# for i in range(0, len(empl_fname)):
#     print(empl_fname[i])
# c.execute("INSERT INTO EMPLOYEE VALUES ("+empl_fname[i]+", "+empl_minit[i]+", "+empl_lname[i]+", "+empl_ssn[i]+", "+empl_addr[i]+", "+empl_num[i]+", "+str(empl_salary[i])+", "+str(empl_id[i])+", "+empl_cname[i]+")")

# FINANCIAL MARKET INSERTION

import requests
from bs4 import BeautifulSoup

fm_URL = "https://en.wikipedia.org/wiki/List_of_stock_exchanges"
fm_page = requests.get(fm_URL)
fm_soup = BeautifulSoup(fm_page.content, "html.parser")

exchanges_table = fm_soup.find(id="exchanges_table")
exchanges_table_rows = exchanges_table.find_all("tr")
exchanges_table_data = []
for r in exchanges_table_rows:
    col = r.find_all("td")
    col = [t.text.strip() for t in col]
    exchanges_table_data.append([e for e in col if e])

exchanges_table_data = exchanges_table_data[3:]
fm_market = []
fm_monthly_trade_vol = []
fm_abbreviation = []
fm_market_cap = []

for i in range(0, 15):
    fm_market.append(exchanges_table_data[i][2])
    fm_monthly_trade_vol.append(exchanges_table_data[i][7])
    fm_abbreviation.append(exchanges_table_data[i][3])
    fm_market_cap.append(exchanges_table_data[i][6])

fm_monthly_trade_vol = [float(n.replace(",","")) if str.isnumeric(n.replace(",","")) else 0 for n in fm_monthly_trade_vol]
fm_market_cap = [float(n) for n in fm_market_cap]

# for i in range(0, len(fm_market)):
    # print(fm_market[i])
    # c.execute(f"INSERT INTO FINANCIAL_MARKET VALUES ('{fm_market[i]}', '{str(fm_abbreviation[i])}', {fm_market_cap[i]}, {fm_monthly_trade_vol[i]})")

# REGULATORY BODY INSERTION

rb_name = ["'Securities and Exchange Comission'", "'Federal Reserve Board'", "'Federal Deposit Insurance Corp'", 
            "'Autorité des Marchés Financiers'", "'The Financial Consumer Agency of Canada'", "'The National Banking and Securities Commission'",
            "'Reserve Bank of India'", "'IRDAI'", "'PFRDA'","'National Administration of Financial Regulation'",
            "'The Superintendency of Banks of Panama'","'The Superintendencia de Banca, Seguros y Administradoras Privadas de Fondos de Pensiones'",
            "'National Monetary Council'", "'Banco Central do Brasil'", "'Securities Commission'", "'The Banco Central de la República Argentina'",
            "'The Bank of Spain'", "'The Financial Conduct Authority'", "'National Bank of Ethiopia'", "'State Bank of Pakistan'",
            "'Bangladesh Bank'"]
rb_country_name = ["'United States of America'","'United States of America'","'United States of America'","'France'","'Canada'","'Mexico'","'India'","'India'","'India'","'China'","'Panama'","'Peru'","'Brazil'","'Brazil'","'Brazil'","'Argentina'",
                    "'Spain'","'The United Kingdom'","'Ethiopia'","'Pakistan'","'Bangladesh'"]
rb_sectors = ["'Securities'", "'Banking'", "'Banking'", "'General'", "'General'","'General'","'Banking, Payment Systems'", "'Financial Entities'",
                "'Insurance'", "'Pensions'", "'General'","'General'", "'General'", "'General'","'General'","'Banking'","'General'",
                "'General'", "'General'", "'General'", "'General'"]

# for i in range(0, len(rb_name)):
    # print(rb_name[i])
    # c.execute(f"INSERT INTO REGULATORY_BODY VALUES ({rb_sectors[i]}, {rb_name[i]}, {rb_country_name[i]})")



# STOCKHOLDER INFORMATION INSERT

sh_fname = ["'Arsh'", "'Namita'", "'Vaishnavi'", "'Jessie'", "'John'", "'Adam'", "'Aidan'","'Matt'","'Ahmed'","'Alex'","'Andrew'","'Andy'","'Angeline'","'Brian'","'Cedric'","'Christeana'","'Connor'","'Chelsea'","'Caleb'","'David'"]
sh_minit = ["'M'", "''", "''", "''", "'A'", "'B'", "'C'", "'D'", "'E'","'F'", "'G'", "'H'", "'J'","'K'", "'L'", "'M'", "'N'", "'O'","'P'", "'Q'"]
sh_lname = ["'Siddiqui'", "'Shashidar'", "'Alavala'", "'Dertke'", "'Johnson'", "'Smith'", "'Frost'", "'Singh'", "'Xu'", "'Azim'", "'Williamson'", "'Phuong'", "'Eggeman'", "'West'", "'White'", "'Hughes'", "'Arkellian'", "'Julia'", "'Alvari'", "'Soliman'"]
sh_amt_invested = [0, 0, 0, 0, 100, 1000, 10000, 45, 745.92, 10, 145, 456, 100002, 1013258, 238964, 9009, 555, 444, 1827, 14]
sh_id = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
sh_bank_ac = [1234567890, 2345678765, 2345432, 234567, 9876543, 34567, 987654323456, 789876543456, 87654567, 3456765,
                234564, 456765, 876567, 4567865, 678765, 345654, 8765678, 987,89098, 34567]

# for i in range(0, len(sh_fname)):
    # print(sh_fname[i])
    # c.execute(f"INSERT INTO STOCKHOLDER VALUES ({sh_fname[i]}, {sh_minit[i]}, {sh_lname[i]}, {str(sh_amt_invested[i])}, {str(sh_id[i])}, {str(sh_bank_ac[i])})")


# STOCK INFORMATION INSERT

# s_URLs = ["https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch","https://finance.yahoo.com/quote/MSFT?p=MSFT&.tsrc=fin-srch",
#         "https://finance.yahoo.com/quote/JPM?p=JPM&.tsrc=fin-srch","https://finance.yahoo.com/quote/GOOGL?p=GOOGL&.tsrc=fin-srch",
#         "https://finance.yahoo.com/quote/1398.HK?p=1398.HK&.tsrc=fin-srch","https://finance.yahoo.com/quote/AMAT?p=AMAT&.tsrc=fin-srch"
#         "https://finance.yahoo.com/quote/0939.HK?p=0939.HK&.tsrc=fin-srch","https://finance.yahoo.com/quote/T?p=T&.tsrc=fin-srch"
#         "https://finance.yahoo.com/quote/BAC?p=BAC&.tsrc=fin-srch", "https://finance.yahoo.com/quote/LUV?p=LUV&.tsrc=fin-srch",
#         "https://finance.yahoo.com/quote/SHEL?p=SHEL&.tsrc=fin-srch","https://finance.yahoo.com/quote/3988.HK?p=3988.HK&.tsrc=fin-srch",
#         "https://finance.yahoo.com/quote/TM?p=TM&.tsrc=fin-srch","https://finance.yahoo.com/quote/LRCX?p=LRCX&ncid=yahooproperties_peoplealso_km0o32z3jzm",
#         "https://finance.yahoo.com/quote/UNH?p=UNH&.tsrc=fin-srch","https://finance.yahoo.com/quote/ADI?p=ADI&ncid=yahooproperties_peoplealso_km0o32z3jzm",
#         "https://finance.yahoo.com/quote/WFC?p=WFC&.tsrc=fin-srch","https://finance.yahoo.com/quote/CVX?p=CVX&.tsrc=fin-srch",
#         "https://finance.yahoo.com/quote/HSBC?p=HSBC&.tsrc=fin-srch","https://finance.yahoo.com/quote/NFLX?p=NFLX&.tsrc=fin-srch",
#         "https://finance.yahoo.com/quote/DB?p=DB&ncid=yahooproperties_peoplealso_km0o32z3jzm","https://finance.yahoo.com/quote/UBS?p=UBS&ncid=yahooproperties_peoplealso_km0o32z3jzm"]
# 
# s_cname = []
# s_name = []
# s_mkt = []
# s_price = []
# s_open = []
# s_ask = []
# s_day_range = []
# s_volume = []
# s_volume = []
# s_bid = []
# 
# for i in range(0, len(s_URLs)):
#     s_page = requests.get(s_URLs[i])
#     s_soup = BeautifulSoup(s_page.content, "html.parser")
#     s_head = s_soup.find("h1").text
#     print(s_head)
#     s_cname.append(s_head.split(" (")[0])
#     s_name.append(s_head.split(" (")[1].split(")")[0])
#     s_mkt.append(s_soup.find(id="Lead-5-QuoteHeader-Proxy").find("span").text.split(" - ")[0])
#     s_price.append(float(s_soup.find(id="Lead-5-QuoteHeader-Proxy").find("fin-streamer").text.replace(",","")))
#     s_left_table = s_soup.find(id="quote-summary")
#     s_left_table_rows = s_left_table.find_all("tr") 
#     for r in s_left_table_rows:
#         col = r.find_all("td")
#         col = [t.text.strip() for t in col]
#         if (col[0] == "Open"):
#             s_open.append(float(col[1].replace(",","")))
#         elif (col[0] == "Ask"):
#             s_ask.append(col[1])
#         elif (col[0] == "Day's Range"):
#             s_day_range.append(col[1])
#         elif (col[0] == "Volume"):
#             s_volume.append(int(col[1].replace(",","")))
#         elif (col[0] == "Bid"):
#             s_bid.append(col[1])
# 
# for i in range(0, len(s_bid)):
#     print(s_name[i])
#     c.execute(f"INSERT INTO STOCK VALUES ('{s_name[i]}', {s_price[i]}, {s_open[i]}, '{s_ask[i]}', '{s_day_range[i]}', {s_volume[i]}, '{s_cname[i]}', '{s_bid[i]}', '{'X'+s_mkt[i]}')"


# INSERT INTO OPERATES_IN

oi_company = ["'JPMorgan Chase'", "'Saudi Aramco'", "'Industrial and Commercial Bank of China'", "'China Construction Bank'", "'Agricultural Bank of China'", "'Bank of America'", "'ExxonMobil'", "'Shell'", "'Bank of China'", "'Toyoto Motor'", "'Samsung Electronics'", "'UnitedHealth Group'", "'Ping An Insurance Group'", "'Wells Fargo'", "'Chevron'", "'Petro China'", "'HSBC Holdings'"]
oi_country = ["United States of America","Saudi Arabia","China","China","China","United States of America", "United States of America", "United States of America", "China", "Japan", "South Korea", "United States of America", "China", "United States of America", "United States of America","China","The United Kingdom"]

# for i in range(0, len(oi_company)):
    # print(oi_company[i])
    # c.execute(f"INSERT INTO OPERATES_IN VALUES ('{oi_country[i]}', {oi_company[i]})")

owns_sname = ["AAPL", "MSFT","GOOGL","AMAT","UBS","DB","NFLX","UNH","TM","TM","LUV","LUV","LUV","LUV","T","LRCX","TM","SHEL","1398.HK","GOOGL"]
owns_id = [8,8,8,8,8,8,8,8,9,10,11,12,13,14,15,16,17,18,19,20]
owns_amt_share = [2, 2, 2, 2, 2, 2, 2, 2, 1, 4, 67, 9, 3, 1, 4, 56, 12, 65, 47, 1]
owns_fmarket = ["XNAS","XNAS","XNAS","XNAS","XNYS","XNYS","XNAS","XNYS","XNYS","XNYS","XNYS","XNYS","XNYS","XNYS","XNYS","XNAS","XNYS","XNYS","XNYS","XNAS"]

for i in range(0, len(owns_amt_share)):
    print(owns_sname[i])
    c.execute(f"INSERT INTO OWNS VALUES ('{owns_sname[i]}', {owns_id[i]}, {owns_amt_share[i]}, '{owns_fmarket[i]}')")

connection.commit()
