### LOAD ###
with open('path.json', 'r') as fp:    
    model_configs = json.load(fp)


### DUMP ###
with open('path.json', 'w') as fp:    
    json.dump(dictionary, fp)
