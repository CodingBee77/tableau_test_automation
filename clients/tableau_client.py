import tableauserverclient as TSC

from config.config import Config


class TableauClient:
    def __init__(self):
        self.auth = TSC.PersonalAccessTokenAuth(
            Config.PAT_NAME, Config.PAT_VALUE, site_id=Config.SITE_ID
        )
        self.server = TSC.Server(Config.SERVER_URL, use_server_version=True)

    def sign_in(self):
        return self.server.auth.sign_in(self.auth)

    def get_workbooks(self):
        return self.server.workbooks.get()

    def get_datasources(self):
        return self.server.datasources.get()

    def get_jobs(self):
        return self.server.jobs.get()
