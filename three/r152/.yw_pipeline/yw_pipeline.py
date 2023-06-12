from typing import List

from youwol.app.environment import IPipelineFactory, YouwolEnvironment
from youwol.app.environment.models_project import Pipeline
from youwol.app.routers.projects import Artifact, Link
from youwol.pipelines.pipeline_typescript_weback_npm.external import PipelineConfig, pipeline, BuildStep
from youwol.utils import FileListing

from youwol.utils.context import Context

class PatchBuildStep(BuildStep):
    id: str = "build_patch"

    artifacts: List[Artifact] = [
        Artifact(
            id="dist",
            files=FileListing(
                include=["*", "**"],
                ignore=[".yw_pipeline/**", "cdn.zip", "node_modules", ".template/**"],
            ),
            links=[Link(name="bundle-analysis", url="./dist/bundle-analysis.html")],
        )
    ]


class PipelineFactory(IPipelineFactory):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    async def get(self, _env: YouwolEnvironment, ctx: Context) -> Pipeline:
        config = PipelineConfig(
            customBuildStep=PatchBuildStep()
        )
        return await pipeline(config, ctx)
