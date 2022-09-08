from pathlib import Path

from youwol.pipelines.pipeline_typescript_weback_npm import PackageType, Dependencies, Template, RunTimeDeps
from youwol.pipelines.pipeline_typescript_weback_npm.external import generate_template


template = Template(
    path=Path(__file__).parent,
    type=PackageType.Library,
    name="lodash",
    exportedSymbol="_",
    version="4.17.15",
    author="greinisch@youwol.com"
)

generate_template(template)
