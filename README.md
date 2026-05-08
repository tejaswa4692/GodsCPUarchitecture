finally working NewCPU.circ is the final prototype using 

<img width="161" height="265" alt="image" src="https://github.com/user-attachments/assets/db78ca37-da09-44e3-adbf-f41804376ab4" />

ics and can be made irl

opcodes are

0000 0000 -> LOAD A immediate 
0001 0000 -> LOAD B immediate
0010 0000 -> MOV_AB
0011 0000 -> MOV_BA
0100 0000 -> ALU_ADD
0101 0000 -> ALU_SUB
0110 0000 -> ALU_AND
0111 0000 -> ALU_OR

More instructions gonna be coming soon, finna make this shit with proper I/O and Display drivers

added a python assembler in this too incase you need to program your opcodes
