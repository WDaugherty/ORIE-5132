\ Model HW_2_Problem_1
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  200 x0 + 230 x1 + 320 x2 + 420 x3 + 400 x4 + 490 x5 + 250 x6 + 290 x7
   + 410 x8 + 550 x9 + 450 x10 + 550 x11 + 200 x12 + 230 x13 + 250 x14
   + 300 x15
Subject To
 c0: x0 + x1 + x2 + x3 + x4 + x5 <= 200
 c1: x6 + x7 + x8 + x9 + x10 + x11 <= 200
 c2: x2 + x3 + x8 + x9 + x12 + x13 <= 200
 c3: x4 + x5 + x10 + x11 + x14 + x15 <= 200
 d0: x0 <= 25
 d1: x1 <= 20
 d2: x2 <= 55
 d3: x3 <= 40
 d4: x4 <= 65
 d5: x5 <= 25
 d6: x6 <= 24
 d7: x7 <= 16
 d8: x8 <= 65
 d9: x9 <= 50
 d10: x10 <= 40
 d11: x11 <= 35
 d12: x12 <= 21
 d13: x13 <= 20
 d14: x14 <= 25
 d15: x15 <= 14
Bounds
End
