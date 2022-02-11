#python 2.7.5

#f = open("./gop.txt", 'r')
f = open("gop.txt", 'r')

I_frame=0
P_frame=0
B_frame=0
frame_type_list=[]

# read file and make frame type list 
while True:
    line = f.readline()
    I = "I" in line
    B = "B" in line
    P = "P" in line	
    
    

    if I:
	frame_type_list.append("I")	
    elif P:
	frame_type_list.append("P")
    elif B:
	frame_type_list.append("B")	


    if not line: break
 
f.close()

print( "whole frame : " + str( len( frame_type_list) ) )
print( "I frame : " + str( frame_type_list.count("I") ) )
print( "P frame : " + str( frame_type_list.count("P") ) )
print( "B frame : " + str( frame_type_list.count("B") ) )
print( " " )

# get I frame index 
I_list=[]
n=0
for i in frame_type_list:
	
	if i=="I":
		I_list.append(n)
	n+=1
I_list.append(n)

# print frame type by gop 
gop=[]
for i in range( len(I_list)-1 ) :
	gop= frame_type_list[ I_list[i] : I_list[i+1] ]
	for j in gop:
		if j == "I" :
			I_frame+=1
		elif j == "P" :
			P_frame +=1
		elif j == "B" :
			B_frame +=1
	print( "GOP " + str(i+1) )
	print("I_frame : " + str(I_frame) )
	print("P_frame : " + str(P_frame) )
	print("B_frame : " + str(B_frame) )
	I_frame=0
	P_frame=0
	B_frame=0
	



