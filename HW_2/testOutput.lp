\ Model RMExample
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  425 x0 + 350 x1 + 625 x2 + 450 x3 + 400 x4 + 300 x5 + 300 x6 + 300 x7
Subject To
 d0: x0 <= 30
 d1: x1 <= 50
 d2: x2 <= 40
 d3: x3 <= 65
 d4: x4 <= 50
 d5: x5 <= 80
 d6: x6 <= 0
 d7: x7 <= 0
 c0: x0 + x1 + x2 + x3 <= 100
 c1: x2 + x3 + x4 + x5 <= 100
Bounds
End
