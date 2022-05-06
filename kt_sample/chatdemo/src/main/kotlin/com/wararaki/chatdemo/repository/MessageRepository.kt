package com.wararaki.chatdemo.repository

import com.wararaki.chatdemo.Model.Message
import org.springframework.data.r2dbc.repository.Query
import org.springframework.data.repository.kotlin.CoroutineCrudRepository
import org.springframework.data.repository.query.Param

interface MessageRepository: CoroutineCrudRepository<Message, String> {
    @Query("""
        SELECT * FROM (
            SELECT * FROM MESSAGES
            ORDER BY "SENT" DESC
            LIMIT 10
        ) ORDER BY "SENT"
    """)
    suspend fun findLatest(): List<Message>

    @Query("""
        SELECT * FROM (
            SELECT * FROM MESSAGES
            WHERE SENT > (SELECT SENT FROM MESSAGES WHERE ID = :id)
            ORDER BY "SENT" DESC
        ) ORDER BY "SENT"
    """)
    suspend fun findLatest(@Param("id") id: String): List<Message>
}