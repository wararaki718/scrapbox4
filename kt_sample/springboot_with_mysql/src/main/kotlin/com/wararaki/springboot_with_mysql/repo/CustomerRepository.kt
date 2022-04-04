package com.wararaki.springboot_with_mysql.repo

import com.wararaki.springboot_with_mysql.model.Customer
import org.springframework.data.repository.CrudRepository
import org.springframework.stereotype.Repository

@Repository
interface CustomerRepository : CrudRepository<Customer, Long> {
    fun findByLastName(lastName: String): Iterator<Customer>
}
