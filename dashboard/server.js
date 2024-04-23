const http = require('http');

const hostname = '10.0.0.72'; // Listen on all network interfaces
const port = 5000; // Port for the server

const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello from my windows machine\n');
});

server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
});
