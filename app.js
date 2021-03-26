var express = require('express');
var path = require('path');
var routes = require('./routes/routes.js');
var app = express();
app.use(express.urlencoded());

var http = require("http").createServer(app);
app.use(express.static(path.join(__dirname, "public")));

app.get('/', routes.gethomepage);
app.post('/', routes.gethomepage);
http.listen(8080);
console.log('Server running on port 8080');