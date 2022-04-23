package com.wararaki.sample_react_springdata_web

import org.springframework.data.repository.CrudRepository

interface EmployeeRepository: CrudRepository<Employee, Long> {
}