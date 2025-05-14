from datetime import timedelta

from temporalio import workflow
from temporal.activities.hello import say_hello


@workflow.defn
class HelloWorkflow:
    @workflow.run
    async def run(self, name: str) -> str:
        return await workflow.execute_activity(
            say_hello,
            name,
            schedule_to_close_timeout=timedelta(seconds=5),
        )