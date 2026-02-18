from clients.base_client import BaseTableauClient


class WorkbookClient(BaseTableauClient):
    def get_workbook_by_name(self, workbook_name):
        workbooks, _ = self.server.workbooks.get()

        for wb in workbooks:
            if wb.name == workbook_name:
                return wb

        raise Exception(f"Workbook '{workbook_name}' not found")
