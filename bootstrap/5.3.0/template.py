from pathlib import Path

from youwol.pipelines.pipeline_typescript_weback_npm import (
    PackageType,
    Dependencies,
    Template,
    RunTimeDeps,
    Bundles,
    MainModule,
)
from youwol.pipelines.pipeline_typescript_weback_npm.external import generate_template

template = Template(
    path=Path(__file__).parent,
    type=PackageType.Library,
    name="bootstrap",
    exportedSymbol="bootstrap",
    version="5.3.0",
    author="greinisch@youwol.com",
    dependencies=Dependencies(
        runTime=RunTimeDeps(externals={"@popperjs/core": "^2.11.8"})
    ),
    bundles=Bundles(mainModule=MainModule(entryFile="./src/index.ts")),
)

generate_template(template)
