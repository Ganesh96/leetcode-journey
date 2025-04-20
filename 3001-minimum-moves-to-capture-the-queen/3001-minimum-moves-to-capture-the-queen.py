class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        rook = (a,b)
        bishop = (c,d)
        queen = (e,f)
        if a==e:
            if  c != a or not (min(b, f) < d < max(b, f)):
                return 1
        if b==f:
            if d != b or not (min(a, e) < c < max(a, e)):
                return 1
        
        
        #8,8>>3,3 2,4
        diff_x = abs(e-c)
        diff_y = abs(f-d)
        nc, nd = 1,1
        if diff_x==diff_y:
            if c>e:
                nc = -1
            if d>f:
                nd = -1
            
            x,y = c+nc,d+nd
            rook_block = False
            while(x!=e and y!=f):
                if (x,y)==rook:
                   rook_block= True
                   break
                x+=nc
                y+=nd
            if not rook_block:
                return 1
        return 2
            