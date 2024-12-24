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
print(my_dict['address']['place'])
print(new_dict['address']['place'])

# no matter in case of dict bcz evrything will be 
# ------------------------------- o (1)