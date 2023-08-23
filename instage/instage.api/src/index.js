"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var express_1 = require("express");
var app = (0, express_1.default)();
var PORT = 3000;
app.get("/", function (req, res) {
    res.send("Hello World!");
});
app.get("/x", function (req, res) {
    throw new Error("This is an example exception.");
});
app.listen(PORT, function () {
    console.log("Server listening on port ${PORT}");
});
