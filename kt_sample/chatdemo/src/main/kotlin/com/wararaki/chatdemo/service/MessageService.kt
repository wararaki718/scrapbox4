package com.wararaki.chatdemo.service

import kotlinx.coroutines.flow.Flow

interface MessageService {
    fun latest(): Flow<MessageViewModel>

    fun after(lastMessageId: String): Flow<MessageViewModel>

    fun stream(): Flow<MessageViewModel>

    suspend fun post(messages: Flow<MessageViewModel>)
}