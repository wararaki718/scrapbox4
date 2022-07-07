package com.wararaki.sample_schemaspy.repo

import com.wararaki.sample_schemaspy.model.Customer
import org.springframework.data.repository.CrudRepository
import org.springframework.stereotype.Repository

@Repository
interface CustomerRepository : CrudRepository<Customer, Long> {
    fun findByLastName(lastName: String): Iterator<Customer>
}
