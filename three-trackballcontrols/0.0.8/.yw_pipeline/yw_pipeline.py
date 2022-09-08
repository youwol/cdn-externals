from youwol.environment.forward_declaration import YouwolEnvironment
from youwol.environment.models import IPipelineFactory
from youwol.environment.models_project import JsBundle, Link, PipelineStep, FileListing, Flow, Pipeline
from youwol.pipelines.pipeline_typescript_weback_npm.external import PipelineConfig, pipeline

from youwol_utils.context import Context


class PatchStep(PipelineStep):
    id: str = 'patch'
    run: str = "cp src/three-trackballcontrols.patched.js node_modules/three-trackballcontrols/index.js"
    sources: FileListing = FileListing(
        include=["src/three-trackballcontrols.patched.js"],
    )


class PipelineFactory(IPipelineFactory):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    async def get(self, env: YouwolEnvironment, context: Context) -> Pipeline:

        base_pipeline = await pipeline(PipelineConfig(), context)
        base_pipeline.steps.append(PatchStep())
        base_pipeline.flows = [
            Flow(
                name="prod",
                dag=[
                    "init > patch > build > publish-local > publish-remote "
                ]
            )
        ]
        return base_pipeline
