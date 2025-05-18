class Solution:
    def convertDateToBinary(self, date: str) -> str:
        dateList = date.split("-")
        for i in range(len(dateList)):
            dateList[i] = bin(int(dateList[i]))[2:]
        return "-".join(dateList)