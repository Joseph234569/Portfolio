# Joseph
# 12/01/2023

# A while loop that intializes a counter at 0 and will run untill the counter reaches 50. appends th value to the list called tens
counter = 0
tens = []
while(counter<=50):
    if(counter%10==0):
        tens.append(counter)
    counter += 1
print(tens)
