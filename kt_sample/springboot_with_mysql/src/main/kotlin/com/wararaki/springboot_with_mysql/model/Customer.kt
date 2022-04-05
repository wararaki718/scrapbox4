package com.wararaki.springboot_with_mysql.model

import javax.persistence.*

@Entity
@Table(name = "customer")
class Customer (
    @Column(name = "first_name")
    val firstName: String,
    @Column(name = "last_name")
    val lastName: String,
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    val id: Long = -1) {
    private constructor(): this("", "")
}
