import logging

from scrapinghub import ScrapinghubClient


class SpiderMonitor:
    def __init__(self, batches_sizes, api_key, project_id):
        self.logger = logging.getLogger(__name__)

        client = client = ScrapinghubClient(api_key)
        self.project = client.get_project(project_id)
        self.batches_sizes = batches_sizes

    def run_next_batch(self, spider_name, upper_bound, is_master=False, lower_bound=0):
        self.project.jobs.run(spider_name,
                              job_args={'lower_bound': upper_bound, "is_master": False, "parent": lower_bound})

    def jobs_summary(self):
        pending, running = self.project.jobs.summary("pending"), self.project.jobs.summary("running")
        self.logger.warning(f"Jobs summary  pending:{pending}, running : {running}")
        return pending["count"] + running["count"]
