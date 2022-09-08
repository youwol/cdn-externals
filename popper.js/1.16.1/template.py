from pathlib import Path

from youwol.pipelines.pipeline_typescript_weback_npm import PackageType, Dependencies, Template, RunTimeDeps
from youwol.pipelines.pipeline_typescript_weback_npm.external import generate_template

template = Template(
    path=Path(__file__).parent,
    type=PackageType.Library,
    name="popper.js",
    exportedSymbol="Popper",
    version="1.16.1",
    author="greinisch@youwol.com",
    dependencies=Dependencies(
        devTime={
        }
    )
)

generate_template(template)
