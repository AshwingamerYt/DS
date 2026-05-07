const http = require('http');

http.createServer(function(req, res)
{
    res.write("<h1>Welcome to Node.js Website</h1>");

    res.end();

}).listen(3000);

console.log("Server running at http://localhost:3000"); 