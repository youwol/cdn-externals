import asyncio
import shutil
from pathlib import Path
from typing import Dict, Any

import aiohttp

from youwol_utils import write_json

version = "0.21.3"

natives_packages_folder = Path(__file__).parent / 'pyodide-native-packages'
packages_folder = Path(__file__).parent / 'auto-generated'

for folder in [natives_packages_folder, packages_folder]:
    if folder.exists():
        shutil.rmtree(folder)
    folder.mkdir()


def patch_version(version_str: str):
    parts = [''.join([c for c in part if c.isdigit()]) for part in version_str.split('.')]
    return f"{parts[0]}.{parts[1] if len(parts)>1 else 0}.{parts[2]if len(parts)>2 else 0}"


async def create_native_packages(session: aiohttp.ClientSession, natives_packages: Dict[str, Any]):

    for name, package in natives_packages.items():

        print(f"Native package: {package['name']}")
        url = f"https://cdn.jsdelivr.net/pyodide/v0.21.3/full/{package['file_name']}"
        async with await session.get(url=url) as resp:
            if resp.status == 200:
                file = open(natives_packages_folder / package['file_name'], 'wb')
                file.write(await resp.read())
                file.close()


async def create_packages(session, filtered_packages, all_packages):

    for name, package in all_packages.items():

        print(f"Process package {package['name']}")
        root = packages_folder / package['name']
        root.mkdir(exist_ok=True)
        (root / 'dist').mkdir(exist_ok=True)

        dependencies = [all_packages[d] for d in package['depends']]
        package_json = {
            "name": f"@pyodide/{package['name']}",
            "version": patch_version(package['version']),
            "main": f"dist/{package['file_name']}",
            "youwol": {
                "cdnDependencies": dict({f"@pyodide/{d['name']}": f"^{patch_version(d['version'])}"
                                         for d in dependencies})
            }
        }
        write_json(data=package_json, path=root / 'package.json')
        shutil.copytree(src='./template_yw_pipeline_package', dst=root / '.yw_pipeline', dirs_exist_ok=True)
        url = f"https://cdn.jsdelivr.net/pyodide/v0.21.3/full/{package['file_name']}"
        async with await session.get(url=url) as resp:
            if resp.status == 200:
                file = open(root / 'dist' / package['file_name'], 'wb')
                file.write(await resp.read())
                file.close()


async def execute():

    session = aiohttp.ClientSession()

    async with await session.get(url=f"https://cdn.jsdelivr.net/pyodide/v{version}/full/repodata.json") as resp:
        if resp.status == 200:
            repo_data = await resp.json()

    filtered_packages = {n: p for n, p in repo_data['packages'].items()
                         if p['file_name'].endswith('.whl')
                         }

    natives_packages = {n: p for n, p in repo_data['packages'].items()
                        if not p['file_name'].endswith('.whl') and 'test' not in n}

    await create_packages(session=session,
                          filtered_packages=filtered_packages,
                          all_packages=repo_data['packages'])

    await create_native_packages(session=session,
                                 natives_packages=natives_packages)

    await session.close()

    write_json(data=natives_packages, path=natives_packages_folder / 'native-packages.json')

loop = asyncio.get_event_loop()

asyncio.new_event_loop()
asyncio.run(execute())
