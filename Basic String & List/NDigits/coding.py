txt = str(input())

N = int(input())

M = len(txt)

# M > N (3, 2) ไม่เติม
# M = N ไม่เติม
# M < N เติม N-M
print("0"*(max(M,N)-M) + txt)
