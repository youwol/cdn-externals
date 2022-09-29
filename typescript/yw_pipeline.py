from typing import List

from youwol.environment.models_project import Pipeline, PipelineStep, FileListing, Artifact, Link
from youwol.pipelines.pipeline_typescript_weback_npm import BuildStep, Paths
from youwol.pipelines.pipeline_typescript_weback_npm.external import PipelineConfig, pipeline

from youwol_utils.context import Context


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


async def pipeline_typescript(ctx: Context) -> Pipeline:
    config = PipelineConfig(
        customInitStep=PatchInitStep(),
        customBuildStep=BuildCustomStep()
    )
    return await pipeline(config, ctx)


