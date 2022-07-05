package sample;

public class StaticFactoryMethod {
    private static StaticFactoryMethodImplA implA = new StaticFactoryMethodImplA();
    private static StaticFactoryMethodImplB implB = new StaticFactoryMethodImplB();

    public static IStaticFactoryMethod getStaticFactoryMethod(int num) {
        if (num <= 64) {
            return implA;
        } else {
            return  implB;
        }
    }

    @Override
    public String toString() {
        return "StaticFactoryMethod class";
    }
}
