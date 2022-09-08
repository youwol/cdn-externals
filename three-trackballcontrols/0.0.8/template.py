from pathlib import Path

from youwol.pipelines.pipeline_typescript_weback_npm import PackageType, Dependencies, Template, RunTimeDeps
from youwol.pipelines.pipeline_typescript_weback_npm.external import generate_template

#  three-trackballcontrols: some changes have been maid regarding catching event from the renderer
#  compare src/three-trackball-controls.patch.js with the original

template = Template(
    path=Path(__file__).parent,
    type=PackageType.Library,
    name="three-trackballcontrols",
    exportedSymbol="TrackballControls",
    version="0.0.8",
    author="greinisch@youwol.com",
    dependencies=Dependencies(
        runTime=RunTimeDeps(
            load={
                "three": "^0.128.0"
            }
        )
    ))

generate_template(template)
