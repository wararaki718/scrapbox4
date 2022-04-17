package com.wararaki.sample_webflux_application

data class Greeting(val message: String) {
    override fun toString(): String {
        return "Greeting {message='%s'}".format(this.message)
    }
}
