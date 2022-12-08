from ex_rates_task import ex_rates_to_postgresql
from prefect.deployments import Deployment
from prefect.blocks.core import Block
from prefect.filesystems import LocalFileSystem


deployment = Deployment.build_from_flow(
    flow=ex_rates_to_postgresql,
    name="log-simple",
    work_queue_name="test",
)

if __name__ == "__main__":
    deployment.apply()
