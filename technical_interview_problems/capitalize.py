# Capitalize the first letter at the beginning of a new word 


def runner_up(name):
  full_name = name.split(' ')

  

  return ' '.join([word.capitalize() for word in full_name])

        
print(runner_up("andre adam williams"))


# Variable Table 

# Variable      Content
# name       andre adam williams
# full_name    ['andre', 'adam', 'williams']
