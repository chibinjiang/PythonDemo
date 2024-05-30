import asyncio
from metagpt.roles.di.data_interpreter import DataInterpreter

async def main():
    di = DataInterpreter()
    await di.run("Tell me a joke about boys and girls")

asyncio.run(main())  # or await main() in a jupyter notebook setting

