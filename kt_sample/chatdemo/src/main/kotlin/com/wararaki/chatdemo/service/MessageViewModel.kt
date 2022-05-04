package com.wararaki.chatdemo.service

import java.time.Instant

data class MessageViewModel(val content: String, val user: UserViewModel, val sent: Instant, val id: String? = null)
