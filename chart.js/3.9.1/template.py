from pathlib import Path

from youwol.pipelines.pipeline_typescript_weback_npm import PackageType, Dependencies, Template, RunTimeDeps, Bundles, \
    MainModule
from youwol.pipelines.pipeline_typescript_weback_npm.external import generate_template


template = Template(
    path=Path(__file__).parent,
    type=PackageType.Library,
    name="chart.js",
    exportedSymbol="Chart",
    version="3.9.1",
    author="greinisch@youwol.com",
    bundles=Bundles(
        mainModule=MainModule(
            entryFile="index.ts",
        )
    )
)

generate_template(template)
