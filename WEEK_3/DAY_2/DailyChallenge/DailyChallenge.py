class Pagination:
    def __init__(self, items=None, pageSize=10):
        self.items = items if items else []
        self.pageSize = int(pageSize)
        self.totalPages = max(1, (len(self.items) + self.pageSize - 1) // self.pageSize)
        self.currentPage = 1

    def getVisibleItems(self):
        start_idx = (self.currentPage - 1) * self.pageSize
        end_idx = min(start_idx + self.pageSize, len(self.items))
        return self.items[start_idx:end_idx]

    def prevPage(self):
        self.currentPage = max(1, self.currentPage - 1)
        return self

    def nextPage(self):
        self.currentPage = min(self.totalPages, self.currentPage + 1)
        return self

    def firstPage(self):
        self.currentPage = 1
        return self

    def lastPage(self):
        self.currentPage = self.totalPages
        return self

    def goToPage(self, pageNum):
        page = int(pageNum)
        self.currentPage = max(1, min(self.totalPages, page))
        return self


alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.getVisibleItems())  #["a", "b", "c", "d"]

p.nextPage().nextPage()
print(p.getVisibleItems())  #["e", "f", "g", "h"]

p.lastPage()
print(p.getVisibleItems())  #["y", "z"]

p.goToPage(10)
print(p.getVisibleItems())  #["y", "z"] last available page

p.goToPage(-3)
print(p.getVisibleItems())  #["a", "b", "c", "d"] first available pag
