import kfp


create_step_get_lines = kfp.components.load_component_from_file(
    "components.yaml"
)

def pipeline():
    get_line_step = create_step_get_lines()


if __name__ == "__main__":
    kfp.compiler.Compiler().compile(pipeline, "sample_pipeline.yaml")
