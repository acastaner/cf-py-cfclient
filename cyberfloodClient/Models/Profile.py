class Profile:

    def __init__(self):
        self.id = ""
        self.name = ""
        self.description = ""
        self.scenarios = []
        self.scenarioTypes = []
        self.category = ""
        self.author = ""
        self.updatedBy = ""
        self.updatedAt = ""
        self.createdAt = ""


class AttackProfile(Profile):
    def __init__(self):
        self.uri = "/profiles/attacks"


class ApplicationProfile(Profile):
    def __init__(self):
        self.uri = "/profiles/apps"


class MalwareProfile(Profile):
    def __init__(self):
        self.uri = "/profiles/malware"
