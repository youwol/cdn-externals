from pathlib import Path

from youwol.pipelines.pipeline_typescript_weback_npm import PackageType, Dependencies, Template, RunTimeDeps
from youwol.pipelines.pipeline_typescript_weback_npm.external import generate_template

template = Template(
    path=Path(__file__).parent,
    type=PackageType.Library,
    name="js-beautify",
    exportedSymbol="js_beautify",
    version="1.14.6",
    author="greinisch@youwol.com"
)

generate_template(template)
