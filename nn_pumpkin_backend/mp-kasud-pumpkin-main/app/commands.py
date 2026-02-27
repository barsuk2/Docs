from asyncio import run as aiorun

import typer
import uvicorn

from app.fixtures.db import init_fixtures

app = typer.Typer()


@app.command()
def webserver(hostname: str, port: int, mode: str):
    async def _start():
        config = uvicorn.Config("app.main:app", port=port, host=hostname, log_level="debug" if mode == "dev" else "info")
        server = uvicorn.Server(config)
        await server.serve()

    aiorun(_start())

@app.command()
def restore_demo_users():
    init_fixtures(force=True)
