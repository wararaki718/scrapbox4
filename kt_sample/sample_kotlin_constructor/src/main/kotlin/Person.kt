// primary constructors
class Person (val name: String = "default", val age: Int = 0)

class OriginPerson constructor(name: String, age: Int) {
    val name: String
    val age: Int
    init {
        this.name = name
        this.age = age
    }
}

open class SuperPerson(val name: String)

class ChildPerson(name: String, val age: Int): SuperPerson(name)

class PersonObject private constructor(val name: String, val age: Int) {
    companion object {
        fun create(name: String, age: Int): PersonObject = PersonObject(name, age)
    }
}
