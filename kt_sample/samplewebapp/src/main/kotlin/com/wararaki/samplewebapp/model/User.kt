package com.wararaki.samplewebapp.model

import javax.persistence.Entity
import javax.persistence.GeneratedValue
import javax.persistence.GenerationType
import javax.persistence.Id

@Entity
class User (
    val name: String,
    val email: String,
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    val id: Long = -1){
    private constructor(): this("", "")
}
