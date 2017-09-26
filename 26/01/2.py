import math
print(math.acos(1))
print(math.asin(1))
print(math.atan(1))
print(math.atan2(1,2))
print(math.cos(1))
print(math.hypot(1,2))
print(math.sin(1))
print(math.tan(1))


#算数、数学が苦手でまったく理解できない。
#三角関数
# * 直角三角形のとき、ある角の角度は、ある辺の長さから求まる？
#
# 　　／｜
# ａ／　｜ｂ
# ／θ　｜
# ￣ｃ￣￣
#
# sinθ = b/a
# cosθ = c/a
# tanθ = b/c
#
# * sinθ = 1/2 のときのθを求める
# * sin45 = a/2 のときのaを求める
# 
#http://www8.plala.or.jp/ap2/suugaku/sankakukansuunoshoho.html
# 　　／｜
# １／　｜sinθ
# ／θ　｜
# ￣cosθ
#
# 　　／θ
# １／　｜cosθ
# ／　　｜
# ￣sinθ
#
# 以下の数字は何？　何がどうなったときの、何が求まった値？
print(math.sin(math.radians(45)))
print(math.sin(math.radians(60)))
print(math.sin(math.radians(90)))

print(math.cos(math.radians(90)))
print(math.tan(math.radians(90)))
