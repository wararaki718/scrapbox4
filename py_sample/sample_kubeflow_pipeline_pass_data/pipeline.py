from types import FunctionType

import kfp


def load_component_yaml(target: str) -> FunctionType:
    filepath = f"components/{target}/component.yaml"
    return kfp.components.load_component_from_file(filepath)


def _generator_op() -> kfp.dsl.ContainerOp:
    generator_op = load_component_yaml("generator")
    return (generator_op().set_image_pull_policy("Never"))


def _preprocessor_op(generator_data_path: str) -> kfp.dsl.ContainerOp:
    preprocessor_op = load_component_yaml("preprocessor")
    return (preprocessor_op(generator_data_path=generator_data_path).set_image_pull_policy("Never"))


def _trainer_op(preprocessor_data_path: str) -> kfp.dsl.ContainerOp:
    trainer_op = load_component_yaml("trainer")
    return (trainer_op(preprocessor_data_path=preprocessor_data_path).set_image_pull_policy("Never"))


def _evaluator_op(trainer_data_path: str) -> kfp.dsl.ContainerOp:
    evaluator_op = load_component_yaml("evaluator")
    return (evaluator_op(trainer_data_path=trainer_data_path).set_image_pull_policy("Never"))


@kfp.dsl.pipeline(
    name="sample pipeline",
    description="test pipeline"
)
def pipeline():
    generator = _generator_op()
    preprocessor = _preprocessor_op(generator_data_path=generator.outputs["generator_data_path"])
    trainer = _trainer_op(preprocessor_data_path=preprocessor.outputs["preprocessor_data_path"])
    evaluator = _evaluator_op(trainer_data_path=trainer.outputs["trainer_data_path"])


if __name__ == "__main__":
    kfp.compiler.Compiler().compile(
        pipeline,
        "sample_pipeline.yaml"
    )
