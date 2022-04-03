package com.wararaki.crudweb.spring_boot_with_postgresql.repo

import com.wararaki.crudweb.spring_boot_with_postgresql.model.Customer
import org.springframework.data.repository.CrudRepository
import org.springframework.stereotype.Repository

@Repository
interface CustomerRepository : CrudRepository<Customer, Long> {
    fun findByLastName(lastName: String): Iterator<Customer>
}
