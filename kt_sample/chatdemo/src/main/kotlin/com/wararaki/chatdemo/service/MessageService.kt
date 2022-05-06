package com.wararaki.chatdemo.service

interface MessageService {
    suspend fun latest(): List<MessageViewModel>

    suspend fun after(lastMessageId: String): List<MessageViewModel>

    suspend fun post(message: MessageViewModel)
}