import kfp
from kfp.components import func_to_container_op

@func_to_container_op
def hello_world_1():
    print("step1")

@func_to_container_op
def hello_world_2():
    print("step2")

@func_to_container_op
def hello_world_3():
    print("step3")

def hello_world_4():
    hello_world_2()
    hello_world_3()
    print("step4")

def sample_pipelines():
    hello_world_1()
    hello_world_4()


if __name__ == "__main__":
    kfp.compiler.Compiler().compile(sample_pipelines, f"{__file__}.yaml")
