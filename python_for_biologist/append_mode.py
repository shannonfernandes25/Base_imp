#python code to illustrate append mode
data=open("seq.txt","a")
data.write("atgccagact")
data.close()

'''
output
it doesnt overwrite....it continues writing in the file
'''