dictonary={
    "name":"Yash",
    "tuple":(1,2,3),
    "address":["Maharashtra",402803, {
        "Street":"Mainroad",
        12:13
    }],

}

# print(dictonary["address"][2][12])

nul_dict={}
# nul_dict["name"]="apna_college";

# print(nul_dict["name"])
# print(type(nul_dict))


newDict={
    "name":"Yash",
    "age":22,
    "address":{
        "Road":"Mainroad",
        "Pincode":412803
    }
}

print("Length = ",len(newDict.keys()),"\n")
print( len(list(newDict.values())),"\n")
print(newDict.items(),"\n")

print(newDict.get("age"),"\n")

# newDict.update({"aaa":})

print(newDict.update({'naaam':'aaa'}))

print("New Dic",newDict.values())



