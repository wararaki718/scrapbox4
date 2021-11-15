import kfp


def _switch_op(sample_flag: str) -> kfp.dsl.ContainerOp:
    switch_op = kfp.components.load_component_from_file(
        "component.yaml"
    )
    return (switch_op().set_image_pull_policy("Never"))


def pipeline():
    test_op = _switch_op(sample_flag="test")
    sample_op = _switch_op(sample_flag="sample")


if __name__ == "__main__":
    kfp.compiler.Compiler().compile(
        pipeline,
        "switch_pipeline.yaml"
    )
