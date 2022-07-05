package sample;

public class Main {
    public static void main(String[] args) {
        var pizzaNormal = Pizza.GetPizza();
        var pizzaLarge = Pizza.GetLargePizza();
        var pizzaSmall = Pizza.GetSmallPizza();

        System.out.println(pizzaNormal);
        System.out.println(pizzaLarge);
        System.out.println(pizzaSmall);
        System.out.println();

        var impl = StaticFactoryMethod.getStaticFactoryMethod(63);
        System.out.println(impl.getName());
        System.out.println("DONE");
    }
}
