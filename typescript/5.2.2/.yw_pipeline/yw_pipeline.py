# Youwol application
from typing import List

from youwol.app.environment import YouwolEnvironment
from youwol.app.routers.projects import IPipelineFactory, Pipeline, Artifact, PipelineStep, Link, FileListing
from youwol.pipelines.pipeline_typescript_weback_npm import Paths

# Youwol utilities
from youwol.utils.context import Context

# Youwol pipelines
from youwol.pipelines.pipeline_typescript_weback_npm.external import (
    PipelineConfig,
    pipeline,
    BuildStep
)

class PatchInitStep(BuildStep):
    id: str = "init_patched"
    run: str = f"yarn && cp -r ./node_modules/typescript/lib ./lib"
    artifacts: List[Artifact] = []


class BuildCustomStep(PipelineStep):
    id: str = "build-custom"
    run: str = "yarn build:prod"
    sources: FileListing = FileListing(
        include=[Paths.package_json_file, "webpack.config.js", "src/app",
                 "src/index.ts", "src/tests"],
        ignore=[Paths.auto_generated_file, "**/.*/*", '.template/**']
    )

    artifacts: List[Artifact] = [
        Artifact(
            id='dist',
            files=FileListing(
                include=["*", "dist", "lib/*.d.ts"],
                ignore=['.yw_pipeline/**', 'cdn.zip', 'node_modules', '.template/**', 'lib/*/**', 'lib/*.js',
                        'lib/*.json']
            ),
            links=[
                Link(
                    name='bundle-analysis',
                    url='dist/bundle-analysis.html'
                )
            ]
        )
    ]


class PipelineFactory(IPipelineFactory):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    async def get(self, _env: YouwolEnvironment, ctx: Context) -> Pipeline:
        config = PipelineConfig(
            customInitStep=PatchInitStep(),
            customBuildStep=BuildCustomStep()
        )
        return await pipeline(config, ctx)
