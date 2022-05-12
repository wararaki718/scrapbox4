package com.wararaki.jms_messaging

import com.fasterxml.jackson.annotation.JsonProperty

data class Email(
    @JsonProperty("to") val to: String,
    @JsonProperty("body") val body: String
    )
{
    override fun toString(): String {
        return "Email{to=%s, body=%s}".format(this.to, this.body)
    }
}
