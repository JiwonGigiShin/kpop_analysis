from lyrics_scraping_melon import scraping


#Decade | Year
# 2020 - 1 | 2 - 1
# 2010 - 2 | 10 - 1
# 2000 - 3 | 5 - 1

#2000s
for i in range(1,6):
    scraping(3,i)


#2010s
for i in range(1,11):
    scraping(2,i)


#2020s

for i in range(1,3):
    scraping(1,i)
