package sample;

public class Pizza {
    private int SizeDiameterCM;

    public Pizza() {
        this.SizeDiameterCM = 25;
    }

    public Pizza(int size) {
        this.SizeDiameterCM = size;
    }

    public static Pizza GetPizza() {
        return new Pizza();
    }

    public static Pizza GetLargePizza() {
        return new Pizza(35);
    }

    public static Pizza GetSmallPizza() {
        return new Pizza(28);
    }

    @Override
    public String toString() {
        return String.format("A Pizza with a diameter of %d cm", this.SizeDiameterCM);
    }
}
