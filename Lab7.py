import pandas as pd
'''#Zadanie 1

df = pd.read_csv('demografia.csv')
print(df,"\n")

#Zadanie 2

plik = 'demografia.csv'

plik = 'demografia.csv'
dane = pd.read_csv(
    plik,
    decimal=',',
    na_values=['NA', 'n/a', 'NaN']
)
index_max = dane['2022'].idxmax(skipna=True)
kraj = dane.loc[index_max, 'KRAJE']
print ("max przyrost ludnosci w 2022r jest w:", kraj,"z przyrostem:",index_max)

#Zadanie 3
plik = 'demografia.csv'

dane = pd.read_csv(plik, decimal=',', na_values=['NA', 'n/a', 'Nan'])
dane_bezkraju = dane.drop(columns=["KRAJE"])
max_przyrost = dane_bezkraju.max().max()
rok_max_przyrost = dane_bezkraju.max().idxmax()
index_max_przyrost = dane_bezkraju[rok_max_przyrost].idxmax()
kraj = dane.loc[index_max_przyrost, "KRAJE"]
print("\n",kraj)
'''
#Zadanie 4
data = {
    "ID": [1, 2, 3, 4, 5],
    "Imię": ["Anna", "Jan", "Katarzyna", "Tomasz", "Michał"],
    "Nazwisko": ["Kowalska", "Nowak", "Wiśniewska", "Kaczmarek", "Zieliński"],
    "Stanowisko": ["Manager", "Programista", "Konsultant", "Programista", "Manager"],
    "Wiek": [35, 28, 40, 30, 45],
    "Pensja": [8000, 4500, 6000, 5500, 7000]
}
df = pd.DataFrame(data)

# a) 

większą_pensja = df[df["Pensja"] > 5000]
print(większą_pensja,"\n")

# b) 
sorted_by_age = df.sort_values(by="Wiek")
print(sorted_by_age,"\n")
# c)
avg_salary_by_position = df.groupby("Stanowisko")["Pensja"].mean().reset_index()
print(avg_salary_by_position,"\n")
# d) 
promotion_data = {
    "ID": [2, 4],
    "Nowe Stanowisko": ["Senior Programista", "Team Leader"]
}
promotions = pd.DataFrame(promotion_data)
merged_data = df.merge(promotions, on="ID", how="left")
print(merged_data,"\n")
# e)
#csv_file_path = "/mnt/data/employees_data.csv"
#merged_data.to_csv(csv_file_path, index=False)

# f) 
##csv_file_path, loaded_data.head()
