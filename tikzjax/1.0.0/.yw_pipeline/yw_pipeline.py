from youwol.environment.models_project import JsBundle

from typing import List

from youwol.environment.forward_declaration import YouwolEnvironment
from youwol.environment.models import IPipelineFactory
from youwol.environment.models_project import Artifact, Flow, Pipeline, PipelineStep, FileListing
from youwol.pipelines.pipeline_typescript_weback_npm import PublishCdnLocalStep, \
    create_sub_pipelines_publish, create_sub_pipelines_publish_cdn
from youwol_utils.context import Context
from youwol_utils.utils_paths import parse_json


class BuildStep(PipelineStep):
    id: str = "build"
    run: str = "echo 'Nothing to do'"
    sources: FileListing = FileListing(
        include=["dist"]
    )

    artifacts: List[Artifact] = [
        Artifact(
            id='dist',
            files=FileListing(
                include=["dist", "package.json"]
            )
        )
    ]


class PipelineFactory(IPipelineFactory):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    async def get(self, _env: YouwolEnvironment, ctx: Context):

        publish_remote_steps, dags = await create_sub_pipelines_publish_cdn(start_step="cdn-local", context=ctx)

        return Pipeline(
            target=JsBundle(),
            tags=["javascript", "library", "external"],
            projectName=lambda path: parse_json(path / "package.json")["name"],
            projectVersion=lambda path: parse_json(path / "package.json")["version"],
            steps=[
                      BuildStep(),
                      PublishCdnLocalStep(packagedArtifacts=['dist']),
                  ] + publish_remote_steps,
            flows=[
                Flow(
                    name="prod",
                    dag=[
                            "build > cdn-local",
                        ] + dags
                )
            ]
        )
