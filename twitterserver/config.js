/* CONFIG FILE */

var Config = {
	
	databaseFile : __dirname + "/data", //chmod this path 777

	baseUrl : '/app/', // with trailing /
	servePublicDir : true,
	hostname : false, // 127.0.0.1 = private, false = public
	port : '8081',

	tags : '#rp17' // see https://dev.twitter.com/rest/public/search for how to setup the search query

	/*
		#love OR #hate : one or the other
		#love #hate : contains both tags
	*/

};

module.exports = Config;