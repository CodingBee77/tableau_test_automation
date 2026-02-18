from clients import WorkbookClient


def test_workbook_can_refresh(workbook_client: WorkbookClient):

    workbook = workbook_client.get_workbook_by_name("Sales Dashboard")

    workbook_client.server.workbooks.refresh(workbook)

    assert True
