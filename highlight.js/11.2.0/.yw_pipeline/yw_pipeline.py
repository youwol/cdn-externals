from youwol.environment.forward_declaration import YouwolEnvironment
from youwol.environment.models import IPipelineFactory
from youwol.environment.models_project import Pipeline, Flow
from youwol.pipelines.pipeline_typescript_weback_npm import BuildStep
from youwol.pipelines.pipeline_typescript_weback_npm.external import PipelineConfig, pipeline

from youwol_utils.context import Context


class PatchInitStep(BuildStep):
    id: str = "init_patched"
    run: str = f"yarn && cp -r ./node_modules/highlight.js/styles ./styles"


class PipelineFactory(IPipelineFactory):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    async def get(self, _env: YouwolEnvironment, ctx: Context) -> Pipeline:

        config = PipelineConfig(
            customInitStep=PatchInitStep()
        )
        return await pipeline(config, ctx)

