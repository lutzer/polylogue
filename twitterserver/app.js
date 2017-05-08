/* 
* @Author: Lutz Reiter, Design Research Lab, Universität der Künste Berlin
* @Date:   2016-01-25 11:08:47
* @Last Modified by:   lutz
* @Last Modified time: 2016-01-25 11:08:57
*/

/* use absolute paths for require */
global.r_require = function(name) {
    return require(__dirname + name);
}

var config = r_require('/config.js');

/* Load Settings */
global.settings = r_require('/utils/settings.js');
settings.read(config.settingsFile);

/*Define dependencies.*/
var express = require('express');
var app = express();
var http = require('http').Server(app);



/* Load Sockets */
var sockets = r_require('/sockets')(http);

/* setup router */
var router = express.Router();
router.get('/',function(req,res) {
    res.send("Twitter server running...");
});
app.use(router);


/* Error Handling */
app.use(function(err, req, res, next) {
    res.status(err.status || 500);
});

/* Run the http server */
http.listen(config.port,config.hostname,function(){
    console.log("Node Server listening on "+config.hostname+":"+config.port);
});

/* Run the twitter loop with 6s intervall */
r_require('/twitterloop.js').run(6000);