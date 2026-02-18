import tableauserverclient as TSC


class BaseTableauClient:

    def __init__(self, server_url, token_name, token_value, site_id):
        self.auth = TSC.PersonalAccessTokenAuth(
            token_name,
            token_value,
            site_id
        )
        self.server = TSC.Server(server_url, use_server_version=True)

    def sign_in(self):
        self.server.auth.sign_in(self.auth)

    def sign_out(self):
        self.server.auth.sign_out()