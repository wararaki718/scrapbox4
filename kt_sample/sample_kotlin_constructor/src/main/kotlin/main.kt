fun main(args: Array<String>) {
    // primary constructors
    val person = Person("test", 1)
    val person2 = OriginPerson("sample", 2)
    val person3 = Person()
    val person4 = ChildPerson("aaaa", 3)
    val person5 = PersonObject.create("object", 5)

    println("${person.name}: ${person.age}")
    println("${person2.name}: ${person2.age}")
    println("${person3.name}: ${person3.age}")
    println("${person4.name}: ${person4.age}")
    println("${person5.name}: ${person5.age}")
    println("")

    // secondary constructors
    val view = View("text")
    val view2 = View("text", "color")
    val view3 = MyView("text")
    val view4 = MyView("text", "color")
    val view5 = YourView("text")
    println(view)
    println(view2)
    println(view3)
    println(view4)
    println(view5)
    println("DONE")
}