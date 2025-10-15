#Python script to create user defined function to calculate the percentage of marks scored in three subjects
def mark_per(x,y,z):
    tot=x+y+z
    marks=(tot/300)*100
    percentage=('%.2f' % marks)
    return(percentage)
print(mark_per(97,85,81))

'''
output
87.67
'''
