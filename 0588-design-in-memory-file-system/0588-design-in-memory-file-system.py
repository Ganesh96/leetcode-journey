from collections import defaultdict
class FileSystem:

    def __init__(self):
        self.paths = defaultdict(list)
        self.files = defaultdict(str)

    def ls(self, path: str) -> List[str]:
        if path in self.files:
            return [path.split("/")[-1]]
        return self.paths[path]


    def mkdir(self, path: str) -> None:
        dirs = path.split("/")

        for i in range(1,len(dirs)):
            cur = "/".join(dirs[:i]) or "/"

            if cur not in self.paths or dirs[i] not in self.paths[cur]:
                bisect.insort(self.paths[cur],dirs[i])


    def addContentToFile(self, filePath: str, content: str) -> None:
        if filePath not in self.paths:
            self.mkdir(filePath)
        self.files[filePath] += content

    def readContentFromFile(self, filePath: str) -> str:
        return self.files[filePath]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)