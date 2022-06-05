fun main(args: Array<String>) {
    // object expression
    val say = object {
        val hello = "Hello"
        val world = "World"

        override fun toString(): String {
            return "$hello, $world"
        }
    }
    println(say)

    println(SampleSingleton.get())

    val sample = SampleCompanionObject.create()
    println(sample.get())
}