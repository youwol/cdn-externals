import shutil
from pathlib import Path

from youwol.pipelines.pipeline_typescript_weback_npm import PackageType, Dependencies, Template, Bundles, MainModule, \
    RunTimeDeps
from youwol.pipelines.pipeline_typescript_weback_npm.external import generate_template
from youwol.utils import parse_json

folder_path = Path(__file__).parent

pkg_json = parse_json(folder_path / 'package.json')

template = Template(
    path=Path(__file__).parent,
    type=PackageType.Library,
    name=pkg_json['name'],
    version=pkg_json['version'],
    exportedSymbol=pkg_json['exportedSymbol'],
    author="greinisch@youwol.com",
    dependencies=Dependencies(
        runTime=RunTimeDeps(
            externals={
                "jquery": "^3.6.1",
                "proj4": "^2.8.0",
                "@tweenjs/tween.js": "^18.6.4"
            }
        ),
        devTime={
            "ts-node": "^10.9.1"
        }
    ),
    bundles=Bundles(
        mainModule=MainModule(
            entryFile="./index.ts",
            loadDependencies=["jquery", "proj4"]
        )
    )
)

generate_template(template)


for file in ['README.md', '.gitignore', 'tsconfig.json']:
    shutil.copyfile(
        src=folder_path / '.template' / file,
        dst=folder_path / file
    )
