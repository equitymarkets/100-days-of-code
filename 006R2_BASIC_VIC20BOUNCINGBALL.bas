10 PRINT "X"
20 POKE 36879,8
30 POKE 36878,15
32 FOR L = 1 TO 10
35 POKE 7680 + INT(RND(1)*506),155
37 NEXT
40 X = 1
50 Y = 1
60 DX = 1
70 DY = 1
80 POKE 7680 + X + 22*Y,81
90 FOR T = 1 TO 15: NEXT
100 POKE 7680 + X + 22*Y,32
110 X = X + DX
120 IF X = 0 OR X = 21 THEN DX = -DX: POKE 36876, 220
130 Y = Y + DY
140 IF Y = 0 OR Y = 22 THEN DY = -DY: POKE 36786, 230
150 POKE 36876, 0
155 IF PEEK (7680 + X + 22*Y)=102 THEN DX=-DX:DY=-DY:POKE 36876, 180: GOTO 110
160 GOTO 80

