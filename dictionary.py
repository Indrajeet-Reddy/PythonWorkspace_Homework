

movies_db = {"Chava"       :["Vicky Kaushal","Smriti Mandana","Akshay Khanna","Vineet Kumar"],
             "Dhurandar"   :["Rnaveer Singh","Saara Arjun","Akashay Khanna","Sanjay Dutt"],
             "Raja Shivaji":["Riteish Deshmukh","Genelia Deshmukh","Sanjay Dutt","Abhishek Bachchan"],
             "KGF 2"       :["Yash","Srinidhi Shetty","Sanjay Dutt","Raveena Tandon","Prakash Raj"],
             "Bhaubali 2"  :["Prabhas","Anushka Shetty","Rana Daggubati","Tamannaah Bhatia"]
             }

print(len(movies_db))
print(type(movies_db))

for movie , casts in movies_db.items():
    if "Sanjay Dutt" in casts:
        print(movie)



