# Chava
cast1 = ["Vicky Kaushal","Smriti Mandana","Akshay Khanna","Vineet Kumar"]
# Dhurandar
cast2 = ["Rnaveer Singh","Saara Arjun","Akshay Khanna","Sanjay Dutt"]
# Raja Shivaji
cast3 = ["Riteish Deshmukh","Genelia Deshmukh","Sanjay Dutt","Abhishek Bachchan"]
# Kdf 2
cast4 = ["Yash","Srinidhi Shetty","Sanjay Dutt","Raveena Tandon","Prakash Raj"]
# Bhaubali 2
cast5= ["Prabhas","Anushka Shetty","Rana Daggubati","Tamannaah Bhatia"]


movies_db = {"Chava"       :cast1,
             "Dhurandar"   :cast2,
             "Raja Shivaji":cast3,
             "KGF 2"       :cast4,
             "Bhaubali 2"  :cast5,
             }

cast = cast1 + cast2 + cast3 + cast4 + cast5
chot_dict = {}

for name in cast:
    key = name
    value = cast.count(key)
    chot_dict[key]=value
print(chot_dict )
