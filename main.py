import asyncio

from temporal.workflows.hello import HelloWorkflow
from temporalio.client import Client


async def start_workflow():
    client = await Client.connect("localhost:7233")
    result = await client.execute_workflow(
        HelloWorkflow.run,
        "World",
        id="hello-workflow-id",
        task_queue="hello-task-queue",
    )
    print(f"Result: {result}")


async def main():
    await start_workflow()


if __name__ == '__main__':
    asyncio.run(main())
