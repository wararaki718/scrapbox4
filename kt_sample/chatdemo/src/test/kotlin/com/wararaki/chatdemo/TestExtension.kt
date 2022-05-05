package com.wararaki.chatdemo

import com.wararaki.chatdemo.Model.Message
import com.wararaki.chatdemo.service.MessageViewModel
import java.time.temporal.ChronoUnit.MILLIS

fun MessageViewModel.prepareForTesting() = copy(id = null, sent = sent.truncatedTo(MILLIS))

fun Message.prepareForTesting() = copy(id = null, sent = sent.truncatedTo(MILLIS))
