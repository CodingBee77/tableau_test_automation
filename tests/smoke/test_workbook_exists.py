from clients.workbook_client import WorkbookClient


def test_workbook_exists(workbook_client: WorkbookClient):
    workbook = workbook_client.get_workbook_by_name("Sales Dashboard")
    assert workbook is not None
