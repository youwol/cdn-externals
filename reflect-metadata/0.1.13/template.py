from pathlib import Path

from youwol.pipelines.pipeline_typescript_weback_npm import PackageType, Dependencies, Template, RunTimeDeps
from youwol.pipelines.pipeline_typescript_weback_npm.external import generate_template

# The source file 'index.ts' should be:
# import "reflect-metadata";
# window["Reflect_APIv01"] = Reflect;
#
# Seems like reflect-metadata is used through the global variable 'Reflect'

template = Template(
    path=Path(__file__).parent,
    type=PackageType.Library,
    name="reflect-metadata",
    exportedSymbol="Reflect",
    version="0.1.13",
    author="greinisch@youwol.com"
)

generate_template(template)
