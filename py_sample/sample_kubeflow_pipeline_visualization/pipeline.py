from kfp.v2 import dsl, compiler
from kfp.v2.dsl import Output, ClassificationMetrics


@dsl.component(
    packages_to_install=["scikit-learn"],
    base_image="python:3.8"
)
def iris_sgdclassifier(
    test_sample_fraction: float,
    metrics: Output[ClassificationMetrics]
):
    from sklearn import datasets, model_selection
    from sklearn.linear_model import SGDClassifier
    from sklearn.metrics import confusion_matrix

    iris = datasets.load_iris()
    X_train, X_text, y_train, y_test = model_selection.train_test_split(
        iris["data"], iris["target"], test_size=test_sample_fraction
    )

    model = SGDClassifier()
    model.fit(X_train, y_train)

    y_preds = model_selection.cross_val_predict(model, X_train, y_train, cv=3)
    metrics.log_confusion_matrix(
        ["Setosa", "Versicolour", "Virginica"],
        confusion_matrix(y_train, y_preds)
    )


@dsl.pipeline(
    name="metrics-visualization-pipeline"
)
def pipeline():
    iris_op = iris_sgdclassifier(test_sample_fraction=0.3)


if __name__ == "__main__":
    compiler.Compiler().compile(
        pipeline,
        "sample_visualization_pipeline.json"
    )
