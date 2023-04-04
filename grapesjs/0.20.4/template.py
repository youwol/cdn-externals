from pathlib import Path

from youwol.pipelines.pipeline_typescript_weback_npm import PackageType, Dependencies, Template, RunTimeDeps, Bundles, MainModule
from youwol.pipelines.pipeline_typescript_weback_npm.external import generate_template

template = Template(
    path=Path(__file__).parent,
    type=PackageType.Library,
    name="grapesjs",
    exportedSymbol="grapesjs",
    version="0.20.4",
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
