package sample;

class StaticFactoryMethodImplA implements IStaticFactoryMethod {
    @Override
    public String getName() {
        return "Impl A";
    }
}

class StaticFactoryMethodImplB implements IStaticFactoryMethod {
    @Override
    public String getName() {
        return "Impl B";
    }
}
