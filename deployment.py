from ex_rates_task import ex_rates_to_postgresql
from prefect.deployments import Deployment
from prefect.filesystems import GitHub

github_block = GitHub.load("githubdj")


deployment = Deployment.build_from_flow(
    flow=ex_rates_to_postgresql,
    name="log-simple",
    work_queue_name="test",
    storage=github_block,
)

if __name__ == "__main__":
    deployment.apply()
