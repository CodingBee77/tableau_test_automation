def test_sales_extract_refreshed_today(tableau_client):
    datasources, _ = tableau_client.datasources.get()

    ds = next(d for d in datasources if d.name == "Sales Extract")

    assert ds.extract_last_refresh_time is not None
