package com.wararaki.sample_react_springdata_web

import javax.persistence.Entity
import javax.persistence.GeneratedValue
import javax.persistence.Id

@Entity
data class Employee (
    val firstName: String,
    val lastName: String,
    val description: String,
    @Id @GeneratedValue val id: Long = -1
){
    override fun equals(other: Any?): Boolean {
        if(this == other) {
            return true
        }
        if (other == null || this.javaClass != other.javaClass) {
            return false
        }
        val employee = other as Employee
        return (this.id == employee.id) &&
                (this.firstName == employee.firstName) &&
                (this.lastName == employee.lastName) &&
                (this.description == employee.description)
    }

    override fun toString(): String {
        return "Employee{id=%d, firstName='%s', lastName='%s', description='%s'}".format(
            this.id,
            this.firstName,
            this.lastName,
            this.description
        )
    }
}
