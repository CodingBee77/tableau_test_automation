from clients.workbook_client import WorkbookClient


def test_workbook_exists(config):
    client = WorkbookClient(
        config.server_url, config.token_name, config.token_value, config.site_id
    )
    client.sign_in()

    try:
        workbook = client.get_workbook_by_name("Sales Dashboard")
        assert workbook is not None
    finally:
        client.sign_out()
