# CyberFlood Python Client
pip package to interact with the [CyberFlood](https://www.spirent.com/products/cyberflood) REST API.

Note that this is still a work in progress and not all actions of the API are implemented yet (far from it, in fact). If you need a missing action to be implemented, please [create a ticket](https://github.com/acastaner/cf-py-cfclient/issues) on the Github repository.

## Installation

From pip:

`pip install cyberfloodClient`

Or [download the files](https://pypi.org/project/cyberfloodClient/#files).

## Usage

```python
import cyberfloodClient

print("Checking for connectivity & credentials...", end=" ")
cfClient = cyberfloodClient.CfClient["userName", "password", "controllerAddress"]
cfClient.generateToken()
if cfClient.isLogged():
    print("success! [" + cfClient.userName + "]")
else:
    print("error! Please check your configuration.")
```
