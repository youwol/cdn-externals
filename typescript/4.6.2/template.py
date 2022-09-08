from pathlib import Path

from youwol.pipelines.pipeline_typescript_weback_npm import PackageType, Dependencies, Template, RunTimeDeps
from youwol.pipelines.pipeline_typescript_weback_npm.external import generate_template


#  In package.json => remove typescript from devDependencies
template = Template(
    path=Path(__file__).parent,
    type=PackageType.Library,
    name="typescript",
    exportedSymbol="ts",
    version="4.6.2",
    author="greinisch@youwol.com"
)

generate_template(template)
