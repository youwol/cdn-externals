from pathlib import Path

from youwol.pipelines.pipeline_typescript_weback_npm import PackageType, Dependencies, Template, RunTimeDeps, Bundles, MainModule
from youwol.pipelines.pipeline_typescript_weback_npm.external import generate_template

template = Template(
    path=Path(__file__).parent,
    type=PackageType.Library,
    name="stats.js",
    exportedSymbol="stats.js",
    version="0.17.0",
    author="greinisch@youwol.com",
    dependencies=Dependencies(
        runTime=RunTimeDeps(
            externals={
            },
            includedInBundle={
                'stats.js': '0.17.0'
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
