print("Month:")
month = str(input())
print("Leap Year? (Yes|No)")
leap = False
if input().lower == "yes": leap = True
if month.lower() == "january": print("31 days")
elif month.lower() == "february" and leap: print("29 days")
elif month.lower() == "february" and not leap: print("28 days")
elif month.lower() == "march": print("31 days")
elif month.lower() == "april": print("30 days")
elif month.lower() == "may": print("31 days")
elif month.lower() == "june": print("30 days")
elif month.lower() == "july": print("31 days")
elif month.lower() == "august": print("31 days")
elif month.lower() == "september": print("30 days")
elif month.lower() == "october": print("31 days")
elif month.lower() == "november": print("30 days")
elif month.lower() == "december": print("31 days")