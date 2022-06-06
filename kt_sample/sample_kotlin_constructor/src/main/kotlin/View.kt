// secondary constructor

open class View {
    val text: String
    constructor(text: String) {
        this.text = text
    }
    constructor(text: String, color: String) {
        this.text = "$text $color"
    }

    override fun toString(): String {
        return "${this.text} view"
    }
}

class MyView: View {
    constructor(text: String): super(text)
    constructor(text: String, color: String): super(text, color)

    override fun toString(): String {
        return "${this.text} myview"
    }
}

class YourView: View {
    constructor(text: String): this(text, "default_color")
    constructor(text: String, color: String): super(text, color)

    override fun toString(): String {
        return "${this.text} yourview"
    }
}
