// companion object
class SampleCompanionObject {
    companion object {
        fun create(): SampleCompanionObject = SampleCompanionObject()
    }

    fun get(): String {
        return "companion"
    }
}
