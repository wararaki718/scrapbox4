package com.wararaki.chatdemo.service

interface MessageService {
    fun latest(): List<MessageViewModel>

    fun after(messageId: String): List<MessageViewModel>

    fun post(message: MessageViewModel)
}