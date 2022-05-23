package com.wararaki.async_method_demo

data class User (val name: String, val blog: String) {
    override fun toString(): String {
        return "User [name=%s, blog=%s]".format(name, blog)
    }
}
