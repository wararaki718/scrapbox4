import kfp

_matrix_op = kfp.components.load_component_from_file(
    "component.yaml"
)

def pipeline():
    matrix_op = (_matrix_op().set_image_pull_policy("Never"))


if __name__ == "__main__":
    kfp.compiler.Compiler().compile(pipeline, "confusion-matrix-pipeline.yaml")
