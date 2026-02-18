def test_sales_dashboard_exists(tableau_client):
    workbooks, _ = tableau_client.workbooks.get()
    names = [wb.name for wb in workbooks]

    assert "Sales Dashboard" in names
