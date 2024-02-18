class RepoError(Exception):
    def __init__(self,err):
        self.err=err
    def getErrors(self):
        return self.err
