import kfp


def _metrics_op() -> kfp.dsl.ContainerOp:
    metrics_op = kfp.components.load_component_from_file(
        "components/evaluator/component.yaml"
    )
    return (metrics_op().set_image_pull_policy("Never"))

def pipeline():
    metrics = _metrics_op()


if __name__ == "__main__":
    kfp.compiler.Compiler().compile(
        pipeline,
        "metrics_pipeline.yaml"
    )
