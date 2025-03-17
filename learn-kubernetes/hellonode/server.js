var http = require('http');

port = process.env.PORT;

var handleRequest = function (request, response) {
  console.log('Recieved request for URL: ' + request.url);
  response.writeHead(200);
  response.end('Hello World from Kubernetes!');
};
var www = http.createServer(handleRequest);
www.listen(port);
console.log("Listening on port " + port);
