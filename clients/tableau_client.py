from clients.base_client import BaseTableauClient


class TableauClient(BaseTableauClient):
    def get_workbooks(self):
        return self.server.workbooks.get()

    def get_datasources(self):
        return self.server.datasources.get()

    def get_jobs(self):
        return self.server.jobs.get()

    def get_users(self):
        return self.server.users.get()

    def get_groups(self):
        return self.server.groups.get()