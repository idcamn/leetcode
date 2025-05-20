class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for account in accounts:
            account_wealth = 0
            for bank in account:
                account_wealth += bank
            if max_wealth < account_wealth:
                max_wealth = account_wealth
        return max_wealth