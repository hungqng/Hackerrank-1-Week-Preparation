#     for a in range(q):
#         a = [[0 for j in range(2*q)] for i in range(2*q)]
        
#         for x in range(2*q):
#             c = [int(q) for q in input().strip().split('')]
#             a[x] = c
#         v = 0
#         for i in range(q):
#             for j in range(q):
#                 l = []
#                 l.append(a[i][j])
#                 l.append(a[2*q-1-i][j])
#                 l.append(a[i][2*q-1-j])
#                 l.append(a[2*q-1-i][2*n-1-j])
            
#                 maxv = max(l)
#                 v+= maxv
# return v