from pathlib import Path

from youwol.pipelines.pipeline_typescript_weback_npm import PackageType, Dependencies, Template, RunTimeDeps
from youwol.pipelines.pipeline_typescript_weback_npm.external import generate_template

template = Template(
    path=Path(__file__).parent,
    type=PackageType.Library,
    name="uuid",
    exportedSymbol="uuid",
    version="8.3.2",
    author="greinisch@youwol.com"
)

generate_template(template)
