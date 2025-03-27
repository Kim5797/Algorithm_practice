h_1, h_2 = map(int, input().split())
s_1, s_2 = map(int, input().split())
v_1, v_2 = map(int, input().split())
R, G, B = map(int, input().split())

M = max(R, G, B)
m = min(R, G, B)

# V 계산식
V = M

# S 계산식
S = 255 * (V - m) / V

# H 계산식
if V == R:
    H = 60 * (G - B) / (V - m)
elif V == G:
    H = 120 + 60 * (B - R) / (V - m)
elif V == B:
    H = 240 + 60 * (R - G) / (V - m)
else:
    print('error')

if H < 0:
    H += 360

if h_1 <= H <= h_2 and s_1 <= S <= s_2 and v_1 <= V <= v_2:
    print("Lumi will like it.")
else:
    print("Lumi will not like it.")