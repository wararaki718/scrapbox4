package com.wararaki.plugins

import com.wararaki.routes.customerRouting
import com.wararaki.routes.getOrderRoute
import com.wararaki.routes.listOrdersRoute
import com.wararaki.routes.totalizeOrderRoute
import io.ktor.server.routing.*
import io.ktor.http.*
import io.ktor.server.application.*
import io.ktor.server.response.*
import io.ktor.server.request.*

fun Application.configureRouting() {
    routing {
        customerRouting()
        listOrdersRoute()
        getOrderRoute()
        totalizeOrderRoute()
    }
}
