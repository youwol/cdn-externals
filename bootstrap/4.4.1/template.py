from pathlib import Path

from youwol.pipelines.pipeline_typescript_weback_npm import PackageType, Dependencies, Template, RunTimeDeps
from youwol.pipelines.pipeline_typescript_weback_npm.external import generate_template

template = Template(
    path=Path(__file__).parent,
    type=PackageType.Library,
    name="bootstrap",
    exportedSymbol="bootstrap",
    version="4.4.1",
    author="greinisch@youwol.com",
    dependencies=Dependencies(
        runTime=RunTimeDeps(
            load={
                "jquery": "^3.6.1",
                "popper.js": "^1.16.1"
            }
        )
    )
)

generate_template(template)
