# importing the required libraries
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

# define the scope
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']


def create_keyfile_dict():
    variables_keys = {
        "type": "service_account",
        "project_id": "mobilede-hasznaltauto",
        "private_key_id": "6210f9863b36b8878c18f7026b27c1e81aed25ce",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCt9jRYW8qvNLEC\nZxkwDKM7WHIe340voG5mHYwvYmcFkm0cJTOu76YZ+Hni8L7MAvRYFukd9Tua7PAt\n83KHepsezyoySVNnpUY73J1BQZVn/6IzJMXFnXYxXuGQRjeNnICXu/0gPqavyThq\nfwPIsb0kiUlSYLyssGU8ezrPQ1L+Ryq30jOBDx2bWAcuh1UNAxyyCgGmMl6oO0sP\n1PiK83L+I+fUYbG+KWT/9CJFzBW08vNZf9ybpEQBAip7+b/UFKM4mSWlPAf49yDL\nL+rBE+DsT3TM/24mzGLQKjggqxXrh0T4HL1JnvHW/Hev2yR0WZd77isdw7R27k26\nqQUTLi1nAgMBAAECggEAJvmBMsal+2kHu20T1JMQQyyGrOoS/Lep5FD8ZmVahYIP\n1f1zvd7NTQZBcJnVdWm4CsBfTCn0R7qL+Q+Q+k96z4VEg+2vtQnvWVwNE2C5M4qv\ncVvsv2CO6XLDgIpqydxlZxlkFcRTnhCsBhgc5esEYFotxjoMK3h9xfYp7+O6hWNX\n253vtG8v7I5yo5sJpHsJzudZfXUGYUNpBsBHTGj7RHU2dPjGx7hYkUHcMDCwuaSl\nJAc1qhwpfARWRw+iEjSE+7NS6HS0f/lz8uPS7CpxbiMlGFs6u4TCmeydbEAi7/3K\nU89fWF4LvtjsCiW9pmKzvcBhpuWmpmVF2hwu1Gq2EQKBgQDUd68Z0Nce54VRSkGD\nufS9HijKguOZyNkuhAwlhlY2KnJMkve8JO7fZ73gQ3GC3hcWSqm4/5ZckrQ6iqJ2\nE5u2JXYdxUMZ+NetY0ApON5Hec3cxAMK/IU05Y48hMrmn9NIlZ/HfEz1rjsbsqGZ\naQ1tDGznZa3P3q65koWvVMnWjwKBgQDRmtIgQUNxjVZXou52niwYX6QvgTROK1Ef\n6H/JpLLc365HILgOPj/5WnMC8glhMhcljxVLZBcvxB+OAK95AP1OxwJ8d6otDS6+\nJPjguUP0n3YeFccRtm4ydH/+UE1XwqrudgVM171ZOtLrIV8jBiFuF+ihYDCTm5Ru\nYrgt/6RnqQKBgBnhZkvfu4SBMSUgxXA1Q5GRzeg1H2JJK+NVpGEhxvicHQYk1NZv\nLUW7Tk62CGqngOpvN9NYFsm5+Qg0gOufIdWDJKslrzHHtQXi1BrxWWoddS0SF0jM\nT7GM0NGgX1LOXx81UpwrEPjQO1T5YmPcfw0seUuKgCyU9HWYWn5r9pYTAoGAG4l9\nhaNNWwO4jjbnoUnSfTlDdsJAvuxN8iU3dKRgo0f3u3x+8dAX04igh4iI1u4fwF11\n7LuvmCTqCFvqsbkBjnHyz6tg/h43P9/Xmp58YQz6FaXCy37uJ07K6fxezOLUVhPH\nSnslcy2ZPC7cMtvBVJdrhpf+icXs0DvD+rcVQFECgYAm7XNc6eSYRnvRISHsHPhG\nZhIXjIvvfX+CxkPlS7Ym7D7RzEoD+YguwS2w6bGZMhzjEaor5ISR5YM1ohMVHu/n\nk5HBlvtzGGYKqHU0aysUzGZ0QJMa7pRtOW9Ibu28jb8dNTy1390lOM3YRPVelChN\nsNfOB0HAs7H3vpLRtyNzzg==\n-----END PRIVATE KEY-----\n",
        "client_email": "mobilede@mobilede-hasznaltauto.iam.gserviceaccount.com",
        "client_id": "115948495130456236131",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/mobilede%40mobilede-hasznaltauto.iam.gserviceaccount.com"
    }

    return variables_keys


class SpreadMobile:

    def __init__(self, credential_path="/Users/Krisztian_Urban/Desktop/mobile_de_hza/mobilede-hasznaltauto.json"
                 , scope=None, email=str()):
        if scope is None:
            scope = list()

        self.credential_path = credential_path
        self.scope = scope
        self.email = email

    def connect_to_spread(self, str_spread_name="mobile"):
        """Return a spreadsheet"""
        # add credentials to the account
        creds = ServiceAccountCredentials.from_json_keyfile_name(self.credential_path, scope)

        # authorize the client
        client = gspread.authorize(creds)

        sheet = client.open(str_spread_name)

        return sheet

    def share_spread_with_email(self, sheet, list_email=list()):
        # get the instance of the Spreadsheet
        for account in list_email:
            sheet.share(account, perm_type='user', role='writer')

    def df_from_worksheet(self, sh, ws=0):
        # get the first sheet of the Spreadsheet
        sheet_instance = sh.get_worksheet(ws)
        df_mobile = pd.DataFrame(sheet_instance.get_all_values())

        #  change header to frist row
        df_new_header = df_mobile.iloc[0]  # grab the first row for the header
        df_mobile = df_mobile[1:]  # take the data less the header row
        df_mobile.columns = df_new_header  # set the header row as the df header

        return df_mobile

    def get_links(self, df_mobile):
        """clear link colums from space and '\n', give only df_links"""
        df_links = df_mobile['link'].str.strip()
        df_links = df_links.str.replace("\n", "")

        return df_links


meine_mobile = SpreadMobile(scope=scope)
df_meine_mobile = meine_mobile.df_from_worksheet(meine_mobile.connect_to_spread())
df_meine_mobile.head(5)
df_meine_mobile.columns

df_links = meine_mobile.get_links(df_meine_mobile)
type(df_links)

link = df_links.iloc[0]
type(link)

#  https://suchen.mobile.de/fahrzeuge/details.html?id=333515156&damageUnrepaired=NO_DAMAGE_UNREPAIRED&isSearchRequest=true&makeModelVariant1.makeId=3500&makeModelVariant1.modelId=10&minFirstRegistrationDate=2014-01-01&pageNumber=1&scopeId=C&sfmr=false&searchId=eabbac38-e310-71b9-d913-18b1c460c5e8'
