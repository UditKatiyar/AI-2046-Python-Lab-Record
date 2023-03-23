from datetime import timedelta,date
n =int(input(" enter number of days to be added:"))
datenew= date.today() +timedelta(days=n)
print(datenew)