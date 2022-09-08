from youwol.environment.forward_declaration import YouwolEnvironment
from youwol.environment.models import IPipelineFactory
from youwol.environment.models_project import Pipeline, Flow
from youwol.pipelines.pipeline_typescript_weback_npm.external import PipelineConfig, pipeline, BuildStep

from youwol_utils.context import Context

to_replace = [
    [
    'https:\/\/cdnjs.cloudflare.com\/ajax\/libs\/font-awesome\/4.7.0\/css\/font-awesome.min.css',
    '\/api\/assets-gateway\/raw\/package\/Zm9udGF3ZXNvbWU=\/5.12.1\/css\/all.min.css'
    ],
    ["fa fa-trash-o", "fas fa-trash"],
    ["fa fa-arrows", "fas fa-arrows-alt"]
]


class PatchBuildStep(BuildStep):
    id: str = "build_patch"
    run: str = f"yarn build:prod && sed -i 's/{to_replace[0][0]}/{to_replace[0][1]}/g'  ./dist/grapesjs.js && " \
               f"sed -i 's/{to_replace[1][0]}/{to_replace[1][1]}/g'  ./dist/grapesjs.js &&" \
               f" sed -i 's/{to_replace[2][0]}/{to_replace[2][1]}/g'  ./dist/grapesjs.js"


class PipelineFactory(IPipelineFactory):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    async def get(self, _env: YouwolEnvironment, ctx: Context) -> Pipeline:

        base_pipeline = await pipeline(PipelineConfig(), ctx)
        base_pipeline.steps.append(PatchBuildStep())
        base_pipeline.flows = [
            Flow(
                name="prod",
                dag=[
                    "init > build_patch > publish-local > publish-remote "
                ]
            )
        ]
        return base_pipeline
