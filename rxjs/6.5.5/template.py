from pathlib import Path

from youwol.pipelines.pipeline_typescript_weback_npm import PackageType, Dependencies, Template, RunTimeDeps
from youwol.pipelines.pipeline_typescript_weback_npm.external import generate_template

template = Template(
    path=Path(__file__).parent,
    type=PackageType.Library,
    name="rxjs",
    exportedSymbol="rxjs",
    version="6.5.5",
    author="greinisch@youwol.com"
)

generate_template(template)
