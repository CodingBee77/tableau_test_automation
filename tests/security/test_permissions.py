from clients import WorkbookClient


def test_workbook_permissions(workbook_client: WorkbookClient):

    workbook = workbook_client.get_workbook_by_name("Sales Dashboard")

    permissions = workbook_client.server.workbooks.populate_permissions(workbook)

    assert len(permissions.permissions) > 0
