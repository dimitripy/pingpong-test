import asyncio
from aiohttp import web
import subprocess
import os

async def execute_script(project_path, script_name):
    script_path = os.path.join(project_path, script_name)
    process = await asyncio.create_subprocess_exec('python3', script_path, stdout=asyncio.subprocess.PIPE)
    stdout, _ = await process.communicate()
    return stdout.decode()

async def handle_request(request):
    data = await request.json()
    script_name = data.get('script')
    project_path = '/path/to/coworker_scripts'  # Pfad zu den Coworker-Skripten
    result = await execute_script(project_path, script_name)
    return web.Response(text=result)

app = web.Application()
app.router.add_post('/trigger', handle_request)

web.run_app(app, port=4041)
