from requests.packages.urllib3.exceptions import InsecureRequestWarning
import requests
import json
import pickle
import logging
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class CfClient:

    def __init__(self, userName, userPassword, controllerAddress):
        self.userName = userName
        self.userPassword = userPassword
        self.controllerAddress = "https://" + controllerAddress + "/api/v2"
        self.__bearerToken = ""
        self.__isLogged = False
        self.__session = requests.session()
        self.__session.verify = False

        # logging.basicConfig()
        # logging.getLogger().setLevel(logging.DEBUG)
        ## requests_log = logging.getLogger("requests.packages.urllib3")
        # requests_log.setLevel(logging.DEBUG)
        ## requests_log.propagate = True

    def generateToken(self):
        response = self.__session.post(self.controllerAddress + '/token',
                                       data={'email': self.userName,
                                             'password': self.userPassword})
        if response.status_code == 201:
            self.__bearerToken = json.loads(response.text)['token']
            self.__session.headers.update(
                {'Authorization': 'Bearer {0}'.format(self.__bearerToken)})
            self.__isLogged = True
            return self.__bearerToken

    def invalidateToken(self):
        return self.__session.delete(
            self.controllerAddress + '/token'
        )

    def isLogged(self):
        return self.__isLogged

    def getFile(self, fileId):
        return self.__session.get(
            self.controllerAddress + '/files/' + fileId
        )

    def downloadFile(self, fileId):
        return self.__session.get(
            self.controllerAddress + '/files/' + fileId + '/download'
        )

    def getFiles(self):
        return self.__session.get(
            self.controllerAddress + '/files'
        )

    def uploadFileMultipart(self, filePath):
        files = {'file': open(filePath, "rb")}
        response = self.__session.post(
            self.controllerAddress + '/files?type=multipart',
            files=files
        )
        return response

    def deleteFile(self, fileId):
        return self.__session.delete(
            self.controllerAddress + '/files' + fileId
        )

    def listAttackProfiles(self):
        return self.__session.get(
            self.controllerAddress + '/profiles/attacks'
        )

    def createAttackProfile(self, name, description, scenarioIds):
        response = self.__session.post(
            self.controllerAddress + '/profiles/attacks',
            json={
                'name': name,
                'description': description,
                'scenarios': scenarioIds,
                'scenarioTypes': ['attack']
            }
        )
        return response

    def createApplicationProfile(self, name, description, scenarioIds):
        response = self.__session.post(
            self.controllerAddress + '/profiles/apps',
            json={
                'name': name,
                'description': description,
                'category': 'Miscellaneous',
                'scenarios': scenarioIds,
                'scenarioTypes': ['app']
            }
        )
        return response

    def createMalwareProfile(self, name, description, scenarioIds):
        response = self.__session.post(
            self.controllerAddress + '/profiles/malware',
            json={
                'name': name,
                'description': description,
                'scenarios': scenarioIds,
                'scenarioTypes': ['malware'],
                'contentType': 'malware'
            }
        )
        return response

    def listMalwareProfiles(self):
        return self.__session.get(
            self.controllerAddress + '/profiles/malware'
        )

    def listApplicationProfiles(self):
        return self.__session.get(
            self.controllerAddress + '/profiles/apps'
        )

    def createAttackScenario(self, fileId, name, description):
        response = self.__session.post(
            self.controllerAddress + '/scenarios/attacks',
            json={
                'fileId': fileId,
                'name': name,
                'description': description
            }
        )
        return response

    def createApplicationScenario(self, fileId, name, description):
        response = self.__session.post(
            self.controllerAddress + '/scenarios/apps',
            json={'fileId': fileId,
                  'name': name,
                  'description': description,
                  'category': 'Miscellaneous'
                  }
        )
        return response

    def createMalwareScenario(self, fileId, name, description):
        response = self.__session.post(
            self.controllerAddress + '/scenarios/malware',
            json={'fileId': fileId,
                  'name': name,
                  'description': description,
                  'category': 'Miscellaneous'
                  }
        )
        return response

    def getAttackProfile(self, profileId):
        return self.__session.get(
            self.controllerAddress + "/profiles/attacks/" + profileId
        )

    def getCyberSecurityAssessmentTest(self, csaTestId):
        return self.__session.get(
            self.controllerAddress + "/tests/cyber_security_assessment/" + csaTestId
        )

    def getHttpThroughputTest(self, testId):
        return self.__session.get(
            self.controllerAddress + "//tests/http_throughput/" + testId
        )

    def updateCyberSecurityAssessmentTest(self, csaTest, csaTestId):
        return self.__session.put(
            self.controllerAddress +
            "/tests/cyber_security_assessment/" + csaTestId,
            json=csaTest
        )

    def startTest(self, testId):
        return self.__session.put(
            self.controllerAddress + "/tests/" + testId + "/start"
        )

    def getTestRun(self, testRunId):
        return self.__session.get(
            self.controllerAddress + "/test_runs/" + testRunId
        )

    def fetchTestRunTimelineStatistics(self, testRunId):
        return self.__session.get(
            self.controllerAddress + "/test_runs/" + testRunId + "/timeline"
        )
