from ex_rates_task import ex_rates_to_postgresql
from prefect.deployments import Deployment
from prefect_github.repository import GitHubRepository

github_repository_block = GitHubRepository.load("git-repo")


deployment = Deployment.build_from_flow(
    flow=ex_rates_to_postgresql,
    name="git-dominik",
    work_queue_name="test",
    storage=github_repository_block,
)

if __name__ == "__main__":
    deployment.apply()
