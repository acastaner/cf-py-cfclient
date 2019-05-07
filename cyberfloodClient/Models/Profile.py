class Profile:

    def __init__(self):
        self.name = ""
        self.description = ""
        self.category = ""
        self.scenarioTypes = []
        self.scenarios = []


class AttackProfile(Profile):
    def __init__(self):
        self.uri = "/profiles/attacks"


class ApplicationProfile(Profile):
    def __init__(self):
        self.uri = "/profiles/apps"


class MalwareProfile(Profile):
    def __init__(self):
        self.uri = "/profiles/malware"
