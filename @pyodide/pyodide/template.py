import shutil
from pathlib import Path

from youwol.pipelines.pipeline_typescript_weback_npm import PackageType, Dependencies, Template, Bundles, MainModule
from youwol.pipelines.pipeline_typescript_weback_npm.external import generate_template

folder_path = Path(__file__).parent


template = Template(
    path=Path(__file__).parent,
    type=PackageType.Library,
    name="pyodide",
    exportedSymbol="pyodide",
    version="0.21.3",
    author="greinisch@youwol.com",
    dependencies=Dependencies(
        devTime={"ts-node": "^10.9.1"}
    ),
    bundles=Bundles(
        mainModule=MainModule(
            entryFile="./index.ts"
        )
    )
)

generate_template(template)


for file in ['README.md', '.gitignore', 'tsconfig.json']:
    shutil.copyfile(
        src=folder_path / '.template' / file,
        dst=folder_path / file
    )
