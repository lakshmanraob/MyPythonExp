# <script src="https://www.gstatic.com/firebasejs/3.6.7/firebase.js"></script>
# <script>
#  // Initialize Firebase
#  var config = {
#    apiKey: "AIzaSyAPjtYSivTfIVEti8nZxcqAH-ykwWWzps0",
#    authDomain: "fbauthentication-9b3a2.firebaseapp.com",
#    databaseURL: "https://fbauthentication-9b3a2.firebaseio.com",
#    storageBucket: "fbauthentication-9b3a2.appspot.com",
#    messagingSenderId: "364929843096"
#  };
#  firebase.initializeApp(config);
# </script>

# {'registered': True, 'kind': 'identitytoolkit#VerifyPasswordResponse', 'refreshToken': 'ADDl5SFd4uUer9iA9z4IWEOcWbY3chayhTY7lGy_-akoyj86g8uswxaxAdgPMNtrbOH1ohUnkyRVM4Rvvr7Qpl5_BXy6pYYvenwaFj1KyFqBmxeV6AVD_zrv_S513RRFsXX8ZeJKmtZ91x34dQLt9s7P2v4ylpMus6ft-bN6JW8fCTThku9flqOTDhvZ14oAVh-BzZHFr_XrY-IRlpIA-4bMt4qPpou8dw', 'email': 'lak@z1.com', 'expiresIn': '3600', 'idToken': 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjJhZmU0YmFlYTcyY2UxZWE4N2Y4ZjUwMDliM2QxNDQ3NmYwODkxMGYifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vZmJhdXRoZW50aWNhdGlvbi05YjNhMiIsImF1ZCI6ImZiYXV0aGVudGljYXRpb24tOWIzYTIiLCJhdXRoX3RpbWUiOjE0ODU4NTM1NTcsInVzZXJfaWQiOiJUN0NqQjIwemcxWWUxT1FlWE5zZWI4OTlkSTIzIiwic3ViIjoiVDdDakIyMHpnMVllMU9RZVhOc2ViODk5ZEkyMyIsImlhdCI6MTQ4NTg1MzU1NywiZXhwIjoxNDg1ODU3MTU3LCJlbWFpbCI6Imxha0B6MS5jb20iLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZW1haWwiOlsibGFrQHoxLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.kV35za_0eV1mnVlfReY7HniEbKicVCW77WNPkqLuSZZleKeV1QK-Y9N7vfGACI0t7FGYQ-I9IB2zXl6ySll8mR0GXQCMA-ZvuYL2duQUTshQEzhC-sI3U_HJ-qoVB5zI3syXsJDuWSibokND7YyhgDy4Ug1lrd1taARBWsaUiyBn39JxWxLTXxaIbpipdPILCvLQZ9xtmTweBNBYhyxqWGyH_bUTvCOIAD17V6vq3hfGnidAsbxnaO-TbKVUudUX_47r6dn_RebyDNjjUiOTHXJ6CD07YfxqgnUB2Vu7rwleexq58n1mPaoz2tmjbZe785w14r1hwkq4xZY_OZkNIw', 'displayName': '', 'localId': 'T7CjB20zg1Ye1OQeXNseb899dI23'}

import pyrebase


class samplebase(object):
    def __init__(self, config):
        self.config = config
        config = {
            "apiKey": "AIzaSyAPjtYSivTfIVEti8nZxcqAH-ykwWWzps0",
            "authDomain": "fbauthentication-9b3a2.firebaseapp.com",
            "databaseURL": "https://fbauthentication-9b3a2.firebaseio.com",
            "storageBucket": "fbauthentication-9b3a2.appspot.com",
        };


    @classmethod
    def getStatus(samplename):
        print("firebase", samplename)

        firebase = pyrebase.initialize_app(config)

        auth = firebase.auth()

        user = auth.sign_in_with_email_and_password("lak@z1.com", "Dev12345")

        print(user)

        db = firebase.database()

        # parsed_json = json.loads(db.child('sampleList').get(user['idToken']).val()[])

        samplelist = db.child('sampleList').get(user['idToken']).val()

        for sample in samplelist:
            if sample['modelString'] == samplename:
                if sample['status'] == 'available':
                    print(sample['modelString'], " is available")
                else:
                    print(sample['modelString'], " is enagaged")
            else:
                print(samplename, " is not available")
