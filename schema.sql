--
-- File generated with SQLiteStudio v3.4.4 on Sun Dec 3 23:17:49 2023
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: ACCOUNT_TYPE
CREATE TABLE IF NOT EXISTS ACCOUNT_TYPE (Type TEXT PRIMARY KEY);
INSERT INTO ACCOUNT_TYPE (Type) VALUES ('Stockholder');
INSERT INTO ACCOUNT_TYPE (Type) VALUES ('Company');
INSERT INTO ACCOUNT_TYPE (Type) VALUES ('Admin');

-- Table: ACCOUNTS
CREATE TABLE IF NOT EXISTS ACCOUNTS (Username TEXT PRIMARY KEY NOT NULL UNIQUE, Password TEXT NOT NULL, Ac_type TEXT REFERENCES ACCOUNT_TYPE (Type) ON UPDATE CASCADE NOT NULL, ID INTEGER);
INSERT INTO ACCOUNTS (Username, Password, Ac_type, ID) VALUES ('stockholder0', 'password', 'Stockholder', 8);
INSERT INTO ACCOUNTS (Username, Password, Ac_type, ID) VALUES ('company0', 'password', 'Company', 0);
INSERT INTO ACCOUNTS (Username, Password, Ac_type, ID) VALUES ('stockholder1', 'password1', 'Stockholder', 4);
INSERT INTO ACCOUNTS (Username, Password, Ac_type, ID) VALUES ('Admin0', 'admin', 'Admin', 0);
INSERT INTO ACCOUNTS (Username, Password, Ac_type, ID) VALUES ('Lam Research Corporation', 'pass', 'Company', 0);
INSERT INTO ACCOUNTS (Username, Password, Ac_type, ID) VALUES ('Samsung', 'Samsung', 'Company', 0);
INSERT INTO ACCOUNTS (Username, Password, Ac_type, ID) VALUES ('user10', 'user10', 'stockholder', 8);
INSERT INTO ACCOUNTS (Username, Password, Ac_type, ID) VALUES ('gencompany', 'pass', 'company', 0);

-- Table: COMPANY
CREATE TABLE IF NOT EXISTS COMPANY (CEO TEXT NOT NULL, Industry TEXT NOT NULL, Abbreviation TEXT, Name TEXT PRIMARY KEY NOT NULL UNIQUE);
INSERT INTO COMPANY (CEO, Industry, Abbreviation, Name) VALUES ('Tim Cook', 'Technology', 'aapl', 'Apple');
INSERT INTO COMPANY (CEO, Industry, Abbreviation, Name) VALUES ('Satya Nadella', 'Technology', 'msft', 'Microsoft');
INSERT INTO COMPANY (CEO, Industry, Abbreviation, Name) VALUES ('Sundar Pichai', 'Technology', 'googl', 'Google');
INSERT INTO COMPANY (CEO, Industry, Abbreviation, Name) VALUES ('Jamie Dimon', 'Financial Services', 'jpm', 'JPMorgan Chase');
INSERT INTO COMPANY (CEO, Industry, Abbreviation, Name) VALUES ('Amin H. Nasser', 'Oil Producer', '2222', 'Saudi Aramco');
INSERT INTO COMPANY (CEO, Industry, Abbreviation, Name) VALUES ('Chen Siqing', 'Financial Services', 'idcbf', 'Industrial and Commercial Bank of China');
INSERT INTO COMPANY (CEO, Industry, Abbreviation, Name) VALUES ('Tain Guoli', 'Financial Services', 'cichy', 'China Construction Bank');
INSERT INTO COMPANY (CEO, Industry, Abbreviation, Name) VALUES ('Gu Shu', 'Financial Services', 'acgbf', 'Agricultural Bank of China');
INSERT INTO COMPANY (CEO, Industry, Abbreviation, Name) VALUES ('Brian Moynihan', 'Financial Services', 'bac', 'Bank of America');
INSERT INTO COMPANY (CEO, Industry, Abbreviation, Name) VALUES ('Darren Woods', 'Oil Producer', 'xom', 'ExxonMobil');
INSERT INTO COMPANY (CEO, Industry, Abbreviation, Name) VALUES ('Wael Sawan', 'Oil Producer', 'shel', 'Shell');
INSERT INTO COMPANY (CEO, Industry, Abbreviation, Name) VALUES ('Liu Liange', 'Financial Services', 'bachy', 'Bank of China');
INSERT INTO COMPANY (CEO, Industry, Abbreviation, Name) VALUES ('Koji Sato', 'Automotive Industry', 'tm', 'Toyoto Motor');
INSERT INTO COMPANY (CEO, Industry, Abbreviation, Name) VALUES ('Kye-Hyun Kyung', 'Technlogy', '005930.KS', 'Samsung');
INSERT INTO COMPANY (CEO, Industry, Abbreviation, Name) VALUES ('Andrew Witty', 'Healthcare', 'unh', 'UnitedHealth Group');
INSERT INTO COMPANY (CEO, Industry, Abbreviation, Name) VALUES ('Xie Yonglin; Jessica Tan', 'Insurance', 'pngay', 'Ping An Insurance Group');
INSERT INTO COMPANY (CEO, Industry, Abbreviation, Name) VALUES ('Charles W. Scharf', 'Financial Services', 'wfc', 'Wells Fargo');
INSERT INTO COMPANY (CEO, Industry, Abbreviation, Name) VALUES ('Mike Wirth', 'Oil Producer', 'cvx', 'Chevron');
INSERT INTO COMPANY (CEO, Industry, Abbreviation, Name) VALUES ('Zhou Jiping', 'Oil Producer', 'pccyf', 'Petro China');
INSERT INTO COMPANY (CEO, Industry, Abbreviation, Name) VALUES ('Noel Quinn', 'Financial Services', 'hsbc', 'HSBC Holdings');
INSERT INTO COMPANY (CEO, Industry, Abbreviation, Name) VALUES ('Timothy Archer', 'Technology', 'lrcx', 'Lam Research Corporation');

-- Table: COUNTRY
CREATE TABLE IF NOT EXISTS COUNTRY (Unemployment_rate NUMERIC (0, 100), GDP NUMERIC (0), Name TEXT PRIMARY KEY UNIQUE, Inflation_rate NUMERIC, Population INTEGER);
INSERT INTO COUNTRY (Unemployment_rate, GDP, Name, Inflation_rate, Population) VALUES (3.8, 233200000000000, 'United States of America', 3.7, 331900000);
INSERT INTO COUNTRY (Unemployment_rate, GDP, Name, Inflation_rate, Population) VALUES (7.3, 2958000000000, 'France', 5.7, 67750000);
INSERT INTO COUNTRY (Unemployment_rate, GDP, Name, Inflation_rate, Population) VALUES (5.5, 198800000000000, 'Canada', 3.8, 38250000);
INSERT INTO COUNTRY (Unemployment_rate, GDP, Name, Inflation_rate, Population) VALUES (3, 1273000000000, 'Mexico', 4.45, 126700000);
INSERT INTO COUNTRY (Unemployment_rate, GDP, Name, Inflation_rate, Population) VALUES (7.33, 3176000000000, 'India', 1.54, 1408000000);
INSERT INTO COUNTRY (Unemployment_rate, GDP, Name, Inflation_rate, Population) VALUES (5, 17730000000000, 'China', 1.9, 1412000000);
INSERT INTO COUNTRY (Unemployment_rate, GDP, Name, Inflation_rate, Population) VALUES (8.79, 63610000000, 'Panama', 2.86, 4351000);
INSERT INTO COUNTRY (Unemployment_rate, GDP, Name, Inflation_rate, Population) VALUES (3.66, 232200000000, 'Peru', 5.04, 33720000);
INSERT INTO COUNTRY (Unemployment_rate, GDP, Name, Inflation_rate, Population) VALUES (9.46, 1609000000000, 'Brazil', 3.2, 214300000);
INSERT INTO COUNTRY (Unemployment_rate, GDP, Name, Inflation_rate, Population) VALUES (6.49, 487200000000, 'Argentina', 138, 45810000);
INSERT INTO COUNTRY (Unemployment_rate, GDP, Name, Inflation_rate, Population) VALUES (11.6, 1427000000000, 'Spain', 2.4, 47420000);
INSERT INTO COUNTRY (Unemployment_rate, GDP, Name, Inflation_rate, Population) VALUES (4.3, 3131000000000, 'The United Kingdom', 6.7, 67330000);
INSERT INTO COUNTRY (Unemployment_rate, GDP, Name, Inflation_rate, Population) VALUES (4.02, 111300000000, 'Ethiopia', 28.8, 120300000);
INSERT INTO COUNTRY (Unemployment_rate, GDP, Name, Inflation_rate, Population) VALUES (6.42, 348300000000, 'Pakistan', 31.4, 231400000);
INSERT INTO COUNTRY (Unemployment_rate, GDP, Name, Inflation_rate, Population) VALUES (4.7, 416300000000, 'Bangladesh', 7.7, 169400000);
INSERT INTO COUNTRY (Unemployment_rate, GDP, Name, Inflation_rate, Population) VALUES (11.12, 36290000000, 'Nepal', 7.6, 30030000);
INSERT INTO COUNTRY (Unemployment_rate, GDP, Name, Inflation_rate, Population) VALUES (2.64, 4941000000000, 'Japan', 3.3, 125700000);
INSERT INTO COUNTRY (Unemployment_rate, GDP, Name, Inflation_rate, Population) VALUES (2.3, 1811000000000, 'South Korea', 3.7, 51740000);
INSERT INTO COUNTRY (Unemployment_rate, GDP, Name, Inflation_rate, Population) VALUES (3.4, 373000000000, 'Malaysia', 2, 33570000);
INSERT INTO COUNTRY (Unemployment_rate, GDP, Name, Inflation_rate, Population) VALUES (7, 404100000000, 'Egypt', 39.7, 109300000);
INSERT INTO COUNTRY (Unemployment_rate, GDP, Name, Inflation_rate, Population) VALUES (5.64, 833500000000, 'Saudi Arabia', 1.7, 35950000);
INSERT INTO COUNTRY (Unemployment_rate, GDP, Name, Inflation_rate, Population) VALUES (3.611, 25462700000000, 'usa', 8.00279982052117, NULL);
INSERT INTO COUNTRY (Unemployment_rate, GDP, Name, Inflation_rate, Population) VALUES (6.416, 376532751806.989, 'pakistan', 19.8738599646653, NULL);

-- Table: EMPLOYEE
CREATE TABLE IF NOT EXISTS EMPLOYEE (FName TEXT NOT NULL, Minit TEXT (1, 1), LName TEXT NOT NULL, SSN TEXT (9, 9) PRIMARY KEY UNIQUE NOT NULL, Address TEXT, Phone_Num TEXT (10, 10), Salary NUMERIC (0), ID NUMERIC (9, 0) UNIQUE NOT NULL REFERENCES STOCKHOLDER (FName) ON DELETE SET NULL ON UPDATE CASCADE, Cname TEXT REFERENCES COMPANY (Name) ON DELETE SET NULL ON UPDATE CASCADE NOT NULL);
INSERT INTO EMPLOYEE (FName, Minit, LName, SSN, Address, Phone_Num, Salary, ID, Cname) VALUES ('Arsh', 'M', 'Siddiqui', '000000000', '1401 S State St', '000000000', 0, 1, 'Databses Limited');
INSERT INTO EMPLOYEE (FName, Minit, LName, SSN, Address, Phone_Num, Salary, ID, Cname) VALUES ('Namita', '', 'Shashidar', '000000001', '222 N Main St', '000000001', 0, 2, 'Databses Limited');
INSERT INTO EMPLOYEE (FName, Minit, LName, SSN, Address, Phone_Num, Salary, ID, Cname) VALUES ('Vaishnavi', '', 'Alavala', '000000002', '333 N Main St', '000000002', 0, 3, 'Databses Limited');
INSERT INTO EMPLOYEE (FName, Minit, LName, SSN, Address, Phone_Num, Salary, ID, Cname) VALUES ('Jessie', '', 'Dertke', '000000003', '444 N Main St', '000000003', 0, 4, 'Databses Limited');
INSERT INTO EMPLOYEE (FName, Minit, LName, SSN, Address, Phone_Num, Salary, ID, Cname) VALUES ('John', 'A', 'Johnson', '000000004', '111 S Main Street', '000000004', 0, 5, 'Databses Limited');
INSERT INTO EMPLOYEE (FName, Minit, LName, SSN, Address, Phone_Num, Salary, ID, Cname) VALUES ('Adam', 'B', 'Smith', '000000005', '1200 N State St', '000000005', 0, 6, 'Agricultural Bank of China');
INSERT INTO EMPLOYEE (FName, Minit, LName, SSN, Address, Phone_Num, Salary, ID, Cname) VALUES ('Aidan', 'C', 'Frost', '000000006', '14 S Wabash St', '000000006', 0, 7, 'Agricultural Bank of China');
INSERT INTO EMPLOYEE (FName, Minit, LName, SSN, Address, Phone_Num, Salary, ID, Cname) VALUES ('Matt', 'D', 'Singh', '000000007', '77 W Wacker Drive', '000000007', 0, 8, 'Agricultural Bank of China');
INSERT INTO EMPLOYEE (FName, Minit, LName, SSN, Address, Phone_Num, Salary, ID, Cname) VALUES ('Ahmed', 'E', 'Xu', '000000008', '140 N Clark St', '000000008', 0, 9, 'Agricultural Bank of China');
INSERT INTO EMPLOYEE (FName, Minit, LName, SSN, Address, Phone_Num, Salary, ID, Cname) VALUES ('Alex', 'F', 'Azim', '000000009', '20 S Cicero Ave', '000000009', 100, 10, 'Samsung');
INSERT INTO EMPLOYEE (FName, Minit, LName, SSN, Address, Phone_Num, Salary, ID, Cname) VALUES ('Andrew', 'G', 'Williamson', '000000010', '600 S Michigan Ave', '000000010', 100000, 11, 'Samsung');
INSERT INTO EMPLOYEE (FName, Minit, LName, SSN, Address, Phone_Num, Salary, ID, Cname) VALUES ('Jen', 'H', 'Phuong', '000000011', '140 Lake Shore Dr', '000000011', 1400000, 12, 'Samsung');
INSERT INTO EMPLOYEE (FName, Minit, LName, SSN, Address, Phone_Num, Salary, ID, Cname) VALUES ('Angeline', 'J', 'Eggeman', '000000021', '200 North Wells St', '000000021', 40000, 13, 'Samsung');
INSERT INTO EMPLOYEE (FName, Minit, LName, SSN, Address, Phone_Num, Salary, ID, Cname) VALUES ('Brian', 'K', 'West', '000000031', '4000 S Cermak St', '000000031', 120000, 14, 'Samsung');
INSERT INTO EMPLOYEE (FName, Minit, LName, SSN, Address, Phone_Num, Salary, ID, Cname) VALUES ('Cedric', 'L', 'White', '000000041', '12 N Damen Dr', '000000041', 50000, 15, 'Samsung');
INSERT INTO EMPLOYEE (FName, Minit, LName, SSN, Address, Phone_Num, Salary, ID, Cname) VALUES ('Christeana', 'M', 'Hughes', '000000051', '1700 S Damen Dr', '000000051', 0, 16, 'Wells Fargo');
INSERT INTO EMPLOYEE (FName, Minit, LName, SSN, Address, Phone_Num, Salary, ID, Cname) VALUES ('Connor', 'N', 'Arkellian', '000000061', '300 W Logal Blvd', '000000061', 0, 17, 'Wells Fargo');
INSERT INTO EMPLOYEE (FName, Minit, LName, SSN, Address, Phone_Num, Salary, ID, Cname) VALUES ('Chelsea', 'O', 'Julia', '000000071', '200 S Addison St', '000000071', 0, 18, 'Wells Fargo');
INSERT INTO EMPLOYEE (FName, Minit, LName, SSN, Address, Phone_Num, Salary, ID, Cname) VALUES ('Caleb', 'P', 'Alvari', '000000081', '14 W Randolph St', '000000081', 0, 19, 'Wells Fargo');
INSERT INTO EMPLOYEE (FName, Minit, LName, SSN, Address, Phone_Num, Salary, ID, Cname) VALUES ('David', 'Q', 'Soliman', '000000091', '200 W Randolph St', '000000091', 0, 20, 'Wells Fargo');

-- Table: FINANCIAL_MARKET
CREATE TABLE IF NOT EXISTS FINANCIAL_MARKET (Name TEXT NOT NULL, Abbreviation TEXT PRIMARY KEY UNIQUE NOT NULL, Market_Cap NUMERIC, Monthly_Trade_Volume INTEGER);
INSERT INTO FINANCIAL_MARKET (Name, Abbreviation, Market_Cap, Monthly_Trade_Volume) VALUES ('New York Stock Exchange', 'XNYS', 27.69, 1452);
INSERT INTO FINANCIAL_MARKET (Name, Abbreviation, Market_Cap, Monthly_Trade_Volume) VALUES ('Nasdaq', 'XNAS', 24.56, 1262);
INSERT INTO FINANCIAL_MARKET (Name, Abbreviation, Market_Cap, Monthly_Trade_Volume) VALUES ('Shanghai Stock Exchange', 'XSHG', 8.15, 536);
INSERT INTO FINANCIAL_MARKET (Name, Abbreviation, Market_Cap, Monthly_Trade_Volume) VALUES ('Euronext', 'XAMS', 7.33, 174);
INSERT INTO FINANCIAL_MARKET (Name, Abbreviation, Market_Cap, Monthly_Trade_Volume) VALUES ('Japan Exchange Group', 'XJPX', 6.54, 0);
INSERT INTO FINANCIAL_MARKET (Name, Abbreviation, Market_Cap, Monthly_Trade_Volume) VALUES ('Shenzhen Stock Exchange', 'XSHE', 6.22, 0);
INSERT INTO FINANCIAL_MARKET (Name, Abbreviation, Market_Cap, Monthly_Trade_Volume) VALUES ('Hong Kong Stock Exchange', 'XHKG', 5.43, 182);
INSERT INTO FINANCIAL_MARKET (Name, Abbreviation, Market_Cap, Monthly_Trade_Volume) VALUES ('Bombay Stock Exchange', 'XBOM', 3.8, 0);
INSERT INTO FINANCIAL_MARKET (Name, Abbreviation, Market_Cap, Monthly_Trade_Volume) VALUES ('National Stock Exchange', 'XNSE', 3.27, 481);
INSERT INTO FINANCIAL_MARKET (Name, Abbreviation, Market_Cap, Monthly_Trade_Volume) VALUES ('Toronto Stock Exchange', 'XTSE', 3.26, 97);
INSERT INTO FINANCIAL_MARKET (Name, Abbreviation, Market_Cap, Monthly_Trade_Volume) VALUES ('London Stock Exchange', 'XLON', 3.18, 219);
INSERT INTO FINANCIAL_MARKET (Name, Abbreviation, Market_Cap, Monthly_Trade_Volume) VALUES ('Saudi Stock Exchange (Tadawul)', 'XSAU', 2.71, 0);
INSERT INTO FINANCIAL_MARKET (Name, Abbreviation, Market_Cap, Monthly_Trade_Volume) VALUES ('Korea Exchange', 'XKOS', 1.83, 277);
INSERT INTO FINANCIAL_MARKET (Name, Abbreviation, Market_Cap, Monthly_Trade_Volume) VALUES ('Deutsche Börse AG', 'XFRA', 2.1, 140);
INSERT INTO FINANCIAL_MARKET (Name, Abbreviation, Market_Cap, Monthly_Trade_Volume) VALUES ('SIX Swiss Exchange', 'XSWX', 1.95, 77);
INSERT INTO FINANCIAL_MARKET (Name, Abbreviation, Market_Cap, Monthly_Trade_Volume) VALUES ('Nasdaq Nordic', 'OMX', 1.94, 72);
INSERT INTO FINANCIAL_MARKET (Name, Abbreviation, Market_Cap, Monthly_Trade_Volume) VALUES ('Taiwan Stock Exchange', 'XTAI', 1.59, 75);
INSERT INTO FINANCIAL_MARKET (Name, Abbreviation, Market_Cap, Monthly_Trade_Volume) VALUES ('Australian Securities Exchange', 'XASX', 1.55, 0);
INSERT INTO FINANCIAL_MARKET (Name, Abbreviation, Market_Cap, Monthly_Trade_Volume) VALUES ('Johannesburg Stock Exchange', 'XJSE', 1.36, 29);
INSERT INTO FINANCIAL_MARKET (Name, Abbreviation, Market_Cap, Monthly_Trade_Volume) VALUES ('Blacksburg Stock Exchange', 'BSX', 2.7, 23);
INSERT INTO FINANCIAL_MARKET (Name, Abbreviation, Market_Cap, Monthly_Trade_Volume) VALUES ('Korean Stock Exchange', 'XKSE', '1,610.10', 240);

-- Table: OPERATES_IN
CREATE TABLE IF NOT EXISTS OPERATES_IN (Country_name TEXT REFERENCES COUNTRY (Name) ON DELETE CASCADE ON UPDATE CASCADE NOT NULL, CName TEXT REFERENCES COMPANY (Name) ON DELETE CASCADE ON UPDATE CASCADE NOT NULL, PRIMARY KEY (Country_name, CName));
INSERT INTO OPERATES_IN (Country_name, CName) VALUES ('United States of America', 'JPMorgan Chase');
INSERT INTO OPERATES_IN (Country_name, CName) VALUES ('Saudi Arabia', 'Saudi Aramco');
INSERT INTO OPERATES_IN (Country_name, CName) VALUES ('China', 'Industrial and Commercial Bank of China');
INSERT INTO OPERATES_IN (Country_name, CName) VALUES ('China', 'China Construction Bank');
INSERT INTO OPERATES_IN (Country_name, CName) VALUES ('China', 'Agricultural Bank of China');
INSERT INTO OPERATES_IN (Country_name, CName) VALUES ('United States of America', 'Bank of America');
INSERT INTO OPERATES_IN (Country_name, CName) VALUES ('United States of America', 'ExxonMobil');
INSERT INTO OPERATES_IN (Country_name, CName) VALUES ('United States of America', 'Shell');
INSERT INTO OPERATES_IN (Country_name, CName) VALUES ('China', 'Bank of China');
INSERT INTO OPERATES_IN (Country_name, CName) VALUES ('Japan', 'Toyoto Motor');
INSERT INTO OPERATES_IN (Country_name, CName) VALUES ('South Korea', 'Samsung');
INSERT INTO OPERATES_IN (Country_name, CName) VALUES ('United States of America', 'UnitedHealth Group');
INSERT INTO OPERATES_IN (Country_name, CName) VALUES ('China', 'Ping An Insurance Group');
INSERT INTO OPERATES_IN (Country_name, CName) VALUES ('United States of America', 'Wells Fargo');
INSERT INTO OPERATES_IN (Country_name, CName) VALUES ('United States of America', 'Chevron');
INSERT INTO OPERATES_IN (Country_name, CName) VALUES ('China', 'Petro China');
INSERT INTO OPERATES_IN (Country_name, CName) VALUES ('The United Kingdom', 'HSBC Holdings');
INSERT INTO OPERATES_IN (Country_name, CName) VALUES ('United States of America', 'Lam Research Corporation');

-- Table: OWNS
CREATE TABLE IF NOT EXISTS OWNS (SName TEXT REFERENCES STOCK (Name) ON DELETE CASCADE ON UPDATE CASCADE, ID NUMERIC (9, 0) REFERENCES STOCKHOLDER (ID) ON DELETE CASCADE ON UPDATE CASCADE, Amt_Share NUMERIC NOT NULL CHECK (Amt_Share > 0), FMarket TEXT REFERENCES FINANCIAL_MARKET (Abbreviation) ON DELETE CASCADE ON UPDATE CASCADE, PRIMARY KEY (SName, ID, FMarket));
INSERT INTO OWNS (SName, ID, Amt_Share, FMarket) VALUES ('AAPL', 8, 5, 'XNAS');
INSERT INTO OWNS (SName, ID, Amt_Share, FMarket) VALUES ('MSFT', 8, 2, 'XNAS');
INSERT INTO OWNS (SName, ID, Amt_Share, FMarket) VALUES ('GOOGL', 8, 2, 'XNAS');
INSERT INTO OWNS (SName, ID, Amt_Share, FMarket) VALUES ('AMAT', 8, 2, 'XNAS');
INSERT INTO OWNS (SName, ID, Amt_Share, FMarket) VALUES ('UBS', 8, 2, 'XNYS');
INSERT INTO OWNS (SName, ID, Amt_Share, FMarket) VALUES ('NFLX', 8, 2, 'XNAS');
INSERT INTO OWNS (SName, ID, Amt_Share, FMarket) VALUES ('UNH', 8, 2, 'XNYS');
INSERT INTO OWNS (SName, ID, Amt_Share, FMarket) VALUES ('TM', 9, 1, 'XNYS');
INSERT INTO OWNS (SName, ID, Amt_Share, FMarket) VALUES ('TM', 10, 4, 'XNYS');
INSERT INTO OWNS (SName, ID, Amt_Share, FMarket) VALUES ('LUV', 11, 67, 'XNYS');
INSERT INTO OWNS (SName, ID, Amt_Share, FMarket) VALUES ('LUV', 12, 9, 'XNYS');
INSERT INTO OWNS (SName, ID, Amt_Share, FMarket) VALUES ('LUV', 13, 3, 'XNYS');
INSERT INTO OWNS (SName, ID, Amt_Share, FMarket) VALUES ('LUV', 14, 1, 'XNYS');
INSERT INTO OWNS (SName, ID, Amt_Share, FMarket) VALUES ('T', 15, 4, 'XNYS');
INSERT INTO OWNS (SName, ID, Amt_Share, FMarket) VALUES ('LRCX', 16, 56, 'XNAS');
INSERT INTO OWNS (SName, ID, Amt_Share, FMarket) VALUES ('TM', 17, 12, 'XNYS');
INSERT INTO OWNS (SName, ID, Amt_Share, FMarket) VALUES ('SHEL', 18, 65, 'XNYS');
INSERT INTO OWNS (SName, ID, Amt_Share, FMarket) VALUES ('1398.HK', 19, 47, 'XNYS');
INSERT INTO OWNS (SName, ID, Amt_Share, FMarket) VALUES ('GOOGL', 20, 1, 'XNAS');
INSERT INTO OWNS (SName, ID, Amt_Share, FMarket) VALUES ('1398.HK', 8, 24, 'XHKG');
INSERT INTO OWNS (SName, ID, Amt_Share, FMarket) VALUES ('3988.HK', 8, 2, 'HKSE ');
INSERT INTO OWNS (SName, ID, Amt_Share, FMarket) VALUES ('DB', 8, 1, 'NYSE ');

-- Table: REGULATORY_BODY
CREATE TABLE IF NOT EXISTS REGULATORY_BODY (Sectors_required TEXT, Name TEXT UNIQUE, Country_name TEXT REFERENCES COUNTRY (Unemployment_rate) ON DELETE CASCADE ON UPDATE CASCADE, PRIMARY KEY (Name, Country_name));
INSERT INTO REGULATORY_BODY (Sectors_required, Name, Country_name) VALUES ('Securities', 'Securities and Exchange Comission', 'United States of America');
INSERT INTO REGULATORY_BODY (Sectors_required, Name, Country_name) VALUES ('Banking', 'Federal Reserve Board', 'United States of America');
INSERT INTO REGULATORY_BODY (Sectors_required, Name, Country_name) VALUES ('Banking', 'Federal Deposit Insurance Corp', 'United States of America');
INSERT INTO REGULATORY_BODY (Sectors_required, Name, Country_name) VALUES ('General', 'Autorité des Marchés Financiers', 'France');
INSERT INTO REGULATORY_BODY (Sectors_required, Name, Country_name) VALUES ('General', 'The Financial Consumer Agency of Canada', 'Canada');
INSERT INTO REGULATORY_BODY (Sectors_required, Name, Country_name) VALUES ('General', 'The National Banking and Securities Commission', 'Mexico');
INSERT INTO REGULATORY_BODY (Sectors_required, Name, Country_name) VALUES ('Banking, Payment Systems', 'Reserve Bank of India', 'India');
INSERT INTO REGULATORY_BODY (Sectors_required, Name, Country_name) VALUES ('Financial Entities', 'IRDAI', 'India');
INSERT INTO REGULATORY_BODY (Sectors_required, Name, Country_name) VALUES ('Insurance', 'PFRDA', 'India');
INSERT INTO REGULATORY_BODY (Sectors_required, Name, Country_name) VALUES ('Pensions', 'National Administration of Financial Regulation', 'China');
INSERT INTO REGULATORY_BODY (Sectors_required, Name, Country_name) VALUES ('General', 'The Superintendency of Banks of Panama', 'Panama');
INSERT INTO REGULATORY_BODY (Sectors_required, Name, Country_name) VALUES ('General', 'The Superintendencia de Banca, Seguros y Administradoras Privadas de Fondos de Pensiones', 'Peru');
INSERT INTO REGULATORY_BODY (Sectors_required, Name, Country_name) VALUES ('General', 'National Monetary Council', 'Brazil');
INSERT INTO REGULATORY_BODY (Sectors_required, Name, Country_name) VALUES ('General', 'Banco Central do Brasil', 'Brazil');
INSERT INTO REGULATORY_BODY (Sectors_required, Name, Country_name) VALUES ('General', 'Securities Commission', 'Brazil');
INSERT INTO REGULATORY_BODY (Sectors_required, Name, Country_name) VALUES ('Banking', 'The Banco Central de la República Argentina', 'Argentina');
INSERT INTO REGULATORY_BODY (Sectors_required, Name, Country_name) VALUES ('General', 'The Bank of Spain', 'Spain');
INSERT INTO REGULATORY_BODY (Sectors_required, Name, Country_name) VALUES ('General', 'The Financial Conduct Authority', 'The United Kingdom');
INSERT INTO REGULATORY_BODY (Sectors_required, Name, Country_name) VALUES ('General', 'National Bank of Ethiopia', 'Ethiopia');
INSERT INTO REGULATORY_BODY (Sectors_required, Name, Country_name) VALUES ('General', 'State Bank of Pakistan', 'Pakistan');
INSERT INTO REGULATORY_BODY (Sectors_required, Name, Country_name) VALUES ('General', 'Bangladesh Bank', 'Bangladesh');

-- Table: STOCK
CREATE TABLE IF NOT EXISTS STOCK (Name TEXT UNIQUE NOT NULL, Price NUMERIC CONSTRAINT "Greater than 0" CHECK (Price >= 0) NOT NULL, Open NUMERIC CONSTRAINT "Greater than 0" CHECK (Open >= 0) NOT NULL, Ask TEXT CONSTRAINT "Greater than 0" CHECK (Ask >= 0) NOT NULL, Day_range TEXT, Volume INTEGER CONSTRAINT "Greater than 0" CHECK (Volume >= 0) NOT NULL, CName TEXT REFERENCES COMPANY (Name) ON DELETE CASCADE ON UPDATE CASCADE, Bid TEXT CONSTRAINT "Greater than 0" CHECK (Bid >= 0) NOT NULL, FMarket TEXT REFERENCES FINANCIAL_MARKET (Abbreviation) ON DELETE CASCADE ON UPDATE CASCADE NOT NULL, PRIMARY KEY (Name, FMarket));
INSERT INTO STOCK (Name, Price, Open, Ask, Day_range, Volume, CName, Bid, FMarket) VALUES ('AAPL', 177.5, 176.04, '177.54 x 1000', '175.46 - 177.84', 31304744, 'Apple Inc.', '177.56 x 1800', 'XNAS');
INSERT INTO STOCK (Name, Price, Open, Ask, Day_range, Volume, CName, Bid, FMarket) VALUES ('MSFT', 335.22, 332.15, '336.19 x 900', '332.05 - 336.88', 13951605, 'Microsoft Corporation', '336.10 x 900', 'XNAS');
INSERT INTO STOCK (Name, Price, Open, Ask, Day_range, Volume, CName, Bid, FMarket) VALUES ('JPM', 146.42, 145.48, '146.31 x 900', '144.88 - 147.01', 4814512, 'JPMorgan Chase & Co.', '146.33 x 800', 'XNYS');
INSERT INTO STOCK (Name, Price, Open, Ask, Day_range, Volume, CName, Bid, FMarket) VALUES ('GOOGL', 138.81, 138.5, '138.61 x 1100', '138.01 - 139.66', 7910782, 'Alphabet Inc.', '138.61 x 900', 'XNAS');
INSERT INTO STOCK (Name, Price, Open, Ask, Day_range, Volume, CName, Bid, FMarket) VALUES ('1398.HK', 3.92, 3.91, '3.920 x 0', '3.820 - 3.950', 675968330, 'Industrial and Commercial Bank of China Limited', '3.910 x 0', 'XHKG');
INSERT INTO STOCK (Name, Price, Open, Ask, Day_range, Volume, CName, Bid, FMarket) VALUES ('AMAT', 136.4, 142.84, '136.64 x 1000', '133.77 - 143.05', 5288737, 'Applied Materials, Inc.', '136.57 x 800', 'XNAS');
INSERT INTO STOCK (Name, Price, Open, Ask, Day_range, Volume, CName, Bid, FMarket) VALUES ('T', 15.45, 15.37, '15.45 x 21500', '15.16 - 15.65', 63807665, 'AT&T Inc.', '15.44 x 4000', 'XNYS');
INSERT INTO STOCK (Name, Price, Open, Ask, Day_range, Volume, CName, Bid, FMarket) VALUES ('LUV', 24.83, 24.66, '24.76 x 800', '24.56 - 24.97', 3412711, 'Southwest Airlines Co.', '24.75 x 800', 'XNYS');
INSERT INTO STOCK (Name, Price, Open, Ask, Day_range, Volume, CName, Bid, FMarket) VALUES ('SHEL', 68.28, 67.76, '68.14 x 1000', '67.44 - 68.39', 2755018, 'Shell plc', '68.13 x 1300', 'XNYS');
INSERT INTO STOCK (Name, Price, Open, Ask, Day_range, Volume, CName, Bid, FMarket) VALUES ('3988.HK', 2.85, 2.82, '2.850 x 0', '2.800 - 2.870', 630614125, 'Bank of China Limited', '2.840 x 0', 'XHKG');
INSERT INTO STOCK (Name, Price, Open, Ask, Day_range, Volume, CName, Bid, FMarket) VALUES ('TM', 176.16, 176.62, '176.10 x 1000', '175.00 - 176.88', 181603, 'Toyota Motor Corporation', '175.95 x 1000', 'XNYS');
INSERT INTO STOCK (Name, Price, Open, Ask, Day_range, Volume, CName, Bid, FMarket) VALUES ('LRCX', 612.86, 626.95, '613.62 x 1000', '600.57 - 632.49', 1596501, 'Lam Research Corporation', '612.81 x 1200', 'XNAS');
INSERT INTO STOCK (Name, Price, Open, Ask, Day_range, Volume, CName, Bid, FMarket) VALUES ('UNH', 534.23, 536.82, '535.03 x 800', '529.25 - 537.51', 1057416, 'UnitedHealth Group Incorporated', '534.61 x 800', 'XNYS');
INSERT INTO STOCK (Name, Price, Open, Ask, Day_range, Volume, CName, Bid, FMarket) VALUES ('ADI', 171.01, 172.93, '171.53 x 900', '169.05 - 173.03', 1296664, 'Analog Devices, Inc.', '171.25 x 800', 'XNAS');
INSERT INTO STOCK (Name, Price, Open, Ask, Day_range, Volume, CName, Bid, FMarket) VALUES ('WFC', 41.94, 41.48, '41.99 x 800', '41.46 - 42.22', 7815391, 'Wells Fargo & Company', '41.98 x 900', 'XNYS');
INSERT INTO STOCK (Name, Price, Open, Ask, Day_range, Volume, CName, Bid, FMarket) VALUES ('CVX', 169.65, 168.7, '169.65 x 1000', '167.51 - 170.16', 2941908, 'Chevron Corporation', '169.62 x 2200', 'XNYS');
INSERT INTO STOCK (Name, Price, Open, Ask, Day_range, Volume, CName, Bid, FMarket) VALUES ('HSBC', 39.35, 39.17, '39.38 x 1800', '39.01 - 39.41', 1601087, 'HSBC Holdings plc', '39.37 x 1400', 'XNYS');
INSERT INTO STOCK (Name, Price, Open, Ask, Day_range, Volume, CName, Bid, FMarket) VALUES ('NFLX', 404.61, 404.74, '400.10 x 900', '392.26 - 408.94', 19606720, 'Netflix, Inc.', '399.88 x 1800', 'XNAS');
INSERT INTO STOCK (Name, Price, Open, Ask, Day_range, Volume, CName, Bid, FMarket) VALUES ('UBS', 24.33, 24.16, '24.34 x 4000', '24.11 - 24.40', 1864232, 'UBS Group AG', '24.33 x 3100', 'XNYS');
INSERT INTO STOCK (Name, Price, Open, Ask, Day_range, Volume, CName, Bid, FMarket) VALUES ('005930.KS', '72,800.00', '72,800.00', '72,700.00 x 0', '72,500.00 - 72,900.00', '3,960,059', 'Samsung', '72,600.00 x 0', 'XKSE');
INSERT INTO STOCK (Name, Price, Open, Ask, Day_range, Volume, CName, Bid, FMarket) VALUES ('DB', 12.59, 12.42, '14.65 x 3000', '12.42 - 12.60', '2,234,700', 'Deutsche Bank Aktiengesellschaft', '11.00 x 4000', 'NYSE ');

-- Table: STOCKHOLDER
CREATE TABLE IF NOT EXISTS STOCKHOLDER (FName TEXT NOT NULL, Minit TEXT (1), LName TEXT NOT NULL, Amt_invested NUMERIC (0), ID NUMERIC (9, 0) PRIMARY KEY UNIQUE, Bank_Ac NUMERIC (0) NOT NULL);
INSERT INTO STOCKHOLDER (FName, Minit, LName, Amt_invested, ID, Bank_Ac) VALUES ('Arsh', 'M', 'Siddiqui', 0, 1, 1234567890);
INSERT INTO STOCKHOLDER (FName, Minit, LName, Amt_invested, ID, Bank_Ac) VALUES ('Namita', '', 'Shashidar', 0, 2, 2345678765);
INSERT INTO STOCKHOLDER (FName, Minit, LName, Amt_invested, ID, Bank_Ac) VALUES ('Vaishnavi', '', 'Alavala', 0, 3, 2345432);
INSERT INTO STOCKHOLDER (FName, Minit, LName, Amt_invested, ID, Bank_Ac) VALUES ('Jessie', '', 'Dertke', 0, 4, 234567);
INSERT INTO STOCKHOLDER (FName, Minit, LName, Amt_invested, ID, Bank_Ac) VALUES ('John', 'A', 'Johnson', 100, 5, 9876543);
INSERT INTO STOCKHOLDER (FName, Minit, LName, Amt_invested, ID, Bank_Ac) VALUES ('Adam', 'B', 'Smith', 1000, 6, 34567);
INSERT INTO STOCKHOLDER (FName, Minit, LName, Amt_invested, ID, Bank_Ac) VALUES ('Aidan', 'C', 'Frost', 10000, 7, 987654323456);
INSERT INTO STOCKHOLDER (FName, Minit, LName, Amt_invested, ID, Bank_Ac) VALUES ('Matt', 'D', 'Singh', 45, 8, 789876543456);
INSERT INTO STOCKHOLDER (FName, Minit, LName, Amt_invested, ID, Bank_Ac) VALUES ('Ahmed', 'E', 'Xu', 745.92, 9, 87654567);
INSERT INTO STOCKHOLDER (FName, Minit, LName, Amt_invested, ID, Bank_Ac) VALUES ('Alex', 'F', 'Azim', 10, 10, 3456765);
INSERT INTO STOCKHOLDER (FName, Minit, LName, Amt_invested, ID, Bank_Ac) VALUES ('Andrew', 'G', 'Williamson', 145, 11, 234564);
INSERT INTO STOCKHOLDER (FName, Minit, LName, Amt_invested, ID, Bank_Ac) VALUES ('Andy', 'H', 'Phuong', 456, 12, 456765);
INSERT INTO STOCKHOLDER (FName, Minit, LName, Amt_invested, ID, Bank_Ac) VALUES ('Angeline', 'J', 'Eggeman', 100002, 13, 876567);
INSERT INTO STOCKHOLDER (FName, Minit, LName, Amt_invested, ID, Bank_Ac) VALUES ('Brian', 'K', 'West', 1013258, 14, 4567865);
INSERT INTO STOCKHOLDER (FName, Minit, LName, Amt_invested, ID, Bank_Ac) VALUES ('Cedric', 'L', 'White', 238964, 15, 678765);
INSERT INTO STOCKHOLDER (FName, Minit, LName, Amt_invested, ID, Bank_Ac) VALUES ('Christeana', 'M', 'Hughes', 9009, 16, 345654);
INSERT INTO STOCKHOLDER (FName, Minit, LName, Amt_invested, ID, Bank_Ac) VALUES ('Connor', 'N', 'Arkellian', 555, 17, 8765678);
INSERT INTO STOCKHOLDER (FName, Minit, LName, Amt_invested, ID, Bank_Ac) VALUES ('Chelsea', 'O', 'Julia', 444, 18, 987);
INSERT INTO STOCKHOLDER (FName, Minit, LName, Amt_invested, ID, Bank_Ac) VALUES ('Caleb', 'P', 'Alvari', 1827, 19, 89098);
INSERT INTO STOCKHOLDER (FName, Minit, LName, Amt_invested, ID, Bank_Ac) VALUES ('David', 'Q', 'Soliman', 14, 20, 34567);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
