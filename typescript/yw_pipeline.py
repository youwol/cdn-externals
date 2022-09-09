from youwol.environment.models_project import Pipeline, Flow
from youwol.pipelines.pipeline_typescript_weback_npm import BuildStep
from youwol.pipelines.pipeline_typescript_weback_npm.external import PipelineConfig, pipeline

from youwol_utils.context import Context


class PatchInitStep(BuildStep):
    id: str = "init_patched"
    run: str = f"yarn && cp -r ./node_modules/typescript/lib ./lib"


async def pipeline_typescript(ctx: Context) -> Pipeline:
    base_pipeline = await pipeline(PipelineConfig(), ctx)
    base_pipeline.steps.append(PatchInitStep())
    base_pipeline.flows = [
        Flow(
            name="prod",
            dag=[
                "init_patched > build > publish-local > publish-remote "
            ]
        )
    ]
    return base_pipeline
