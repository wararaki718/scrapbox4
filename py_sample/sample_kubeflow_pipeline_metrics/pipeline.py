import kfp
from kfp.components import OutputPath, create_component_from_func


def produce_metrics(
    mlpipeline_metrics_path: OutputPath("Metrics")
):
    import json
    import random
    accuracy = random.random()
    precision = random.random()
    recall = random.random()
    
    metrics = {
        "metrics": [
            {"name": "accuracy-score", "numberValue": accuracy, "format": "PERCENTAGE"},
            {"name": "precision-score", "numberValue": precision, "format": "PERCENTAGE"},
            {"name": "recall-score", "numberValue": recall, "format": "PERCENTAGE"},
        ]
    }

    #return [json.dumps(metrics)]
    with open(mlpipeline_metrics_path, "w") as f:
        json.dump(metrics, f)

def get_metrics_op():
    produce_metrics_op = create_component_from_func(
        produce_metrics,
        base_image="python:3.8",
        packages_to_install=[]
        #output_component_file="component.yaml"
    )
    return produce_metrics_op()


def pipeline():
    metrics = get_metrics_op()


if __name__ == "__main__":
    kfp.compiler.Compiler().compile(
        pipeline,
        "sample_metrics_pipeline.yaml"
    )
