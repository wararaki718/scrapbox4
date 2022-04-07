package com.wararaki.samplewebapp.repo

import com.wararaki.samplewebapp.model.User
import org.springframework.data.repository.CrudRepository
import org.springframework.stereotype.Repository

@Repository
interface UserRepository : CrudRepository<User, Long> {
}
