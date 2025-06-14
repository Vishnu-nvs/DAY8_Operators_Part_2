# DAY8_Operators_Part_2
Identity and Membership and bitwise Operators Concept



Identity_Op_Sample.py(Output)

Memory location of A is : 140730087076936
Memory location of B is : 140730087076936
True 

Memory location of C is : 140730087077256
Memory location of D is : 1979032512240
False



Identity_Op_NOT_Sample.py  (Output)
	
Memory location of A is : 140730087076936
Memory location of B is : 140730087077256
True 

Memory location of c is : 140730087076936
Memory location of d is : 140730087076936
False


membership_Op_Sample.py (Output)
True
False
0    
1    
2    
3    
4    
5    
6    
7    
8    
9    


membership_Op_NOT_Sample.py (Output)

True
False


Bitwise_&(AND) _OP_Sample.py(Output)

Binary form of A is : 0b1010
Binary form of B is : 0b1111
10

Explain:-

A=10,B=15   A&B=10
0	0	0	0	1	0	1	0    ---->A=10

0	0	0	0	1	1	1	1    ---->B=15

0	0	0	0	1	0	1	0    ---->OUTPUT A&B=10

2 power of 0,,2 power of 1,2 power of 2,………………
2 power of 0 * 0= 1 *0 = 0
2 power of 1 * 1= 2 *1 = 2
2 power of 2 * 0= 4 *0 = 0
2 power of 3 * 1= 8 *1 = 8
0+2+0+8=10

Bitwise_(OR) _OP_Sample.py(Output)

Binary form of A is : 0b1010
Binary form of B is : 0b1111
15

Explain:-

A=10,B=15   A|B=15
0	0	0	0	1	0	1	0    ---->A

0	0	0	0	1	1	1	1    ---->B

0	0	0	0	1	1	1	1    ---->OUTPUT

2 power of 0,,2 power of 1,2 power of 2,………………
2 power of 0 * 1= 1 *1 = 1
2 power of 1 * 1= 2 *1 = 2
2 power of 2 * 1= 4 *1 = 4
2 power of 3 * 1= 8 *1 = 8
1+2+4+8=15


Bitwise_(XOR_^) _OP_Sample.py(Output)

Binary form of A is : 0b1010
Binary form of B is : 0b1111
5

A=10,B=15   A ^ B=5
0	0	0	0	1	0	1	0    ---->A

0	0	0	0	1	1	1	1    ---->B

0	0	0	0	0	1	0	1    ---->OUTPUT (5)

2 power of 0,,2 power of 1,2 power of 2,………………
2 power of 0 * 1= 1 *1 = 1
2 power of 1 * 0= 2 *0 = 0
2 power of 2 * 1= 4 *1 = 4

1+0+4=5

Bitwise_(NOT~) _OP_Sample.py(Output)

-11

Explain:-

A=10
Print(~A)

0	0	0	0	1	0	1	0

1’s com
1	1	1	1	0	1	0	1

0	0	0	0	0	0	0	1   ^
--------------------------------------------------------------
1	1	1	1	0	1	0	0
----------------------------------------------------------------

1’s+1’s = 2’s Comp
-(0	0	0	0	1	0	1	1 )
1+2+8=-11


Note :Synatax or logic: -(given number +1)=-(10+1)=-11


Bitwise_(RightShift) _OP_Sample(Output)
0
4
4

----Explain:---------
A=33
0	0	1	0	0	0	0	1

A>>7

0	0	1	0	0	0	0	1
	0	0	1	0	0	0	0
		0	0	1	0	0	0
			0	0	1	0	0
				0	0	1	0
					0	0	1
						0	0
							0
------------------------------------------------------------
0	0	0	0	0	0	0	0
----------------------------------------------------------

0b0=0

A=33

0	0	1	0	0	0	0	1

A>>3


0	0	1	0	0	0	0	1

_	0	0	1	0	0	0	0
	
_	_	0	1	0	0	0	0

_	_	_	0	0	1	0	0
-------------------------------------------------------------
0	0	0	0	0	1	0	0
-----------------------------------------------------------

0b100


Bitwise_(LeftShift) _OP_Sample.py (Output)
2176
2176
------ExP------------
A=34
0b100010
					0	0	1	0	0	0	1	0

				0	0	1	0	0	0	1	0	_

			0	0	1	0	0	0	1	0	_	_	

		0	0	1	0	0	0	1	0	_	_	_
		
	0	0	1	0	0	0	1	0	_	_	_	_
			
	0	0	1	0	0	0	1	0	_	_	_	_
				
0	0	1	0	0	0	1	0	_	_	_	_	_

-----------------------------------------------------------------------------------------------------------						
0	0	1	0	0	0	1	0	0	0	0	0	0	0
----------------------------------------------------------------------------------------------------------


0b100o10000000


Bitwise_(NOT~) _OP_Task.py (Output)

Given value a is 12: -13 

Explanation :-

a=12    #0b1100
Print(~a)

0	0	0	0	1	1	0	0

1’s com
1	1	1	1	0	0	1	1

0	0	0	0	0	0	0	1   ^
--------------------------------------------------------------
1	1	1	1	0	0	1	0
----------------------------------------------------------------

1’s+1’s = 2’s Comp
-( 0	0	0	0	1	1	0	1 )
2 power of 0 * 0= 1 *1 = 1
2 power of 1 * 0= 2 *0 = 0
2 power of 2 * 1= 4 *1 = 4
2 power of 3 * 1= 8 *1 = 8
-(1+0+4+8)=-13



Given value b is 23: -24 

Explanation :-

a=23    #0b10111
Print(~a)

0 0 0 1 0 1 1 1
1’s com
1 1 1 0 1 0 0 0
0 0 0 0 1 1 1 1
--------------------------------------------------------------
1 1 1 0 0 1 1 1
----------------------------------------------------------------
1’s+1’s = 2’s Comp
-( 0	0	0	1	1	0	0	0 )
2 power of 0 * 0= 1 *0 = 0
2 power of 1 * 0= 2 *0 = 0
2 power of 2 * 1= 4 *0 = 0
2 power of 3 * 1= 8 *1 = 1
2 power of 4 * 1= 16*1 = 16  
-(0+0+0+8+16 )= -24

Given value c is -18: 17     

Explanation :-

a=-18    -#0b10010
Print(~a)

0 0 0 1 0 0 1 0
1’s com
1 1 1 0 1 1 0 1
0 0 0 0 0 0 1 1
--------------------------------------------------------------
1 1 1 0 1 1 1 0
----------------------------------------------------------------
1’s+1’s = 2’s Comp
( 0	0	0	1	0	0	0	1 )
2 power of 0 * 0= 1 *1 = 1
2 power of 1 * 0= 2 *0 = 0
2 power of 2 * 1= 4 *0 = 0
2 power of 3 * 1= 8 *0 = 0
2 power of 4 * 1= 16*1 = 16  
(1+0+0+0+16 )= 17
     

Given value d is -20: 19                       

Explanation :-

a=-20    -#0b10100 
Print(~a)

0 0 0 1 0 1 0 0
1’s com
1 1 1 0 1 0 1 1
0 0 0 0 0 1 1 1
--------------------------------------------------------------
1 1 1 0 1 1 0 0
----------------------------------------------------------------
1’s+1’s = 2’s Comp
( 0	0	0	1	0	0	1	1 )
2 power of 0 * 0= 1 *1 = 1
2 power of 1 * 0= 2 *1 = 2
2 power of 2 * 1= 4 *0 = 0
2 power of 3 * 1= 8 *0 = 0
2 power of 4 * 1= 16*1 = 16  
(1+2+0+0+16)=  19  

 

Given value e is 18: -19                        

Explanation :-

a=18    #0b10010
Print(~a)

0 0 0 1 0 0 1 0
1’s com
1 1 1 0 1 1 0 1
0 0 0 0 0 0 0 1
--------------------------------------------------------------
1 1 1 0 1 1 0 0
----------------------------------------------------------------
1’s+1’s = 2’s Comp
( 0	0	0	1	0	0	1	1 )
2 power of 0 * 0= 1 *1 = 1
2 power of 1 * 0= 2 *1 = 2
2 power of 2 * 1= 4 *0 = 0
2 power of 3 * 1= 8 *0 = 0
2 power of 4 * 1= 16*1 = 16  
-(1+2+0+0+16 )=  -19     





