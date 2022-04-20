package com.wararaki.sample_thymeleaf_web_form

import javax.validation.constraints.Min
import javax.validation.constraints.NotNull
import javax.validation.constraints.Size

data class PersonForm (@NotNull @Size(min=2, max=30) val name: String?, @NotNull @Min(18) val age: String?) {
    override fun toString(): String {
        return "Person(Name: %s, Age: %d)".format(this.name, this.age)
    }
}
