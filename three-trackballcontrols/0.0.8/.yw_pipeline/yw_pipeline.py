from youwol.environment.forward_declaration import YouwolEnvironment
from youwol.environment.models import IPipelineFactory
from youwol.environment.models_project import JsBundle, Link, PipelineStep, FileListing, Flow, Pipeline
from youwol.pipelines.pipeline_typescript_weback_npm.external import PipelineConfig, pipeline

from youwol_utils.context import Context


class PatchInitStep(PipelineStep):
    id: str = 'init-patched'
    run: str = "(yarn && cp src/three-trackballcontrols.patched.js node_modules/three-trackballcontrols/index.js)"
    sources: FileListing = FileListing(
        include=["src/three-trackballcontrols.patched.js"],
    )


class PipelineFactory(IPipelineFactory):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    async def get(self, env: YouwolEnvironment, context: Context) -> Pipeline:

        config = PipelineConfig(
            customInitStep=PatchInitStep()
        )
        return await pipeline(config, context)
