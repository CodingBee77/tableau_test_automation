def test_no_failed_jobs(tableau_client):
    jobs, _ = tableau_client.jobs.get()

    failed_jobs = [job for job in jobs if job.finish_code == "Failed"]

    assert len(failed_jobs) == 0
