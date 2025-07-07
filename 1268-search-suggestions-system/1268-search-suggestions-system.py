import bisect

class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        products.sort()
        res = list()
        l,r = 0,len(products)-1

        for ind in range(len(searchWord)):
            c = searchWord[ind]
            while(l<=r and (len(products[l])<=ind or products[l][ind]!=c)):
                l+=1
            while(l<=r and (len(products[r])<=ind or products[r][ind]!=c)):
                r-=1
            res.append([])
            remain = r-l+1
            for j in range(min(remain,3)):
                res[-1].append(products[l+j])
        return res



