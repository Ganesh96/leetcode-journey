from collections import defaultdict
from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Step 1: Define the find and union functions
        def find(n1):
            res = n1
            while res != par[res]:
                par[res] = par[par[res]]  # Path compression
                res = par[res]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0  # Already in the same set
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1  # Successfully merged

        n = len(accounts)
        global par, rank
        par = [i for i in range(n)]
        rank = [1] * n

        # Step 3: Map emails to their owner and union accounts with shared emails
        email_to_owner = {}
        for i, (name, *emails) in enumerate(accounts):
            for email in emails:
                if email in email_to_owner:
                    # print(email_to_owner)
                    union(i, email_to_owner[email])
                email_to_owner[email] = i

        root_to_emails = defaultdict(list)
        for email, owner in email_to_owner.items():
            root = find(owner)
            root_to_emails[root].append(email)

        # Step 5: Format the result
        result = []
        for root, emails in root_to_emails.items():
            name = accounts[root][0]
            result.append([name] + sorted(emails))

        return result