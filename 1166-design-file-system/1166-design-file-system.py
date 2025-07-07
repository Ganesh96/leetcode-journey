class FileSystem:
    def __init__(self):
        # The dictionary will store path -> value mappings.
        # We initialize with a dummy root to simplify the parent check.
        self.paths = {"": 0}

    def createPath(self, path: str, value: int) -> bool:
        # Rule: The path cannot already exist.
        if path in self.paths:
            return False

        # Find the parent path by finding the last '/'.
        # e.g., for "/a/b/c", rfind('/') is at index 3, path[:3] is "/a/b".
        # e.g., for "/a", rfind('/') is at index 0, path[:0] is "".
        parent_path = path[:path.rfind('/')]
        
        # Rule: The parent path must exist.
        # Our dummy "" entry handles the root's children like "/a".
        if parent_path not in self.paths:
            return False
            
        # If all checks pass, create the path.
        self.paths[path] = value
        return True

    def get(self, path: str) -> int:
        # Use .get() with a default value of -1 to handle non-existent paths.
        return self.paths.get(path, -1)