import copy
my_dict = {
    'name':"dilshad",
    'age':19,
    'address':{
        'place':'mannarkkad'
    }
}

new_dict = {key:value for key,value in my_dict.items()}
my_dict['address']['place'] = 'kozhikkode'
# print(my_dict['address']['place'])
# print(new_dict['address']['place'])

# no matter in case of dict bcz evrything will be 
# ------------------------------- o (1)

hash_map = {
    'dilshad':8,
    'messi':11,
    'neymar':10,
    'cr7':7
}

print(sorted(hash_map,key=lambda x: (-hash_map[x],x)))