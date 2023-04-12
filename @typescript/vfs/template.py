import shutil
from pathlib import Path

from youwol.pipelines.pipeline_typescript_weback_npm import PackageType, Dependencies, Template, RunTimeDeps, Bundles, MainModule
from youwol.pipelines.pipeline_typescript_weback_npm.external import generate_template
from youwol_utils import parse_json, write_json
folder_path = Path(__file__).parent


template = Template(
    path=Path(__file__).parent,
    type=PackageType.Library,
    name="@typescript/vfs",
    exportedSymbol="tsvfs",
    version="1.4.0",
    author="greinisch@youwol.com",
    dependencies=Dependencies(
        runTime=RunTimeDeps(
            externals={
            },
            includedInBundle={
                "@typescript/vfs": "1.4.0"
            }
        ),
        devTime={
            "ts-node": "^10.9.1"
        }
    ),
    bundles=Bundles(
        mainModule=MainModule(
            entryFile="./index.ts",
            loadDependencies=[]
        )
    )
)

generate_template(template)
#  'webpack.config.ts' is not here: missing apiVersion
for file in ['README.md', '.gitignore', 'package.json', 'tsconfig.json']:
    shutil.copyfile(
        src=folder_path / '.template' / file,
        dst=folder_path / file
    )

# regarding exported symbol name: we should always have the library's name, additional aliases (e.g. 'tsvsf' here)
# should be supported
# package_json = parse_json(folder_path / 'package.json')
# package_json['exportedSymbol'] = template.exportedSymbol
# write_json(package_json, folder_path / 'package.json')

