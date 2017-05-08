/* CONFIG FILE */

var Config = {
	
	databaseFile : __dirname + "/data", //chmod this path 777

	settingsFile : __dirname + "/data/settings.json",

	baseUrl : '/app/', // with trailing /
	servePublicDir : true,
	hostname : false, // 127.0.0.1 = private, false = public
	port : '8081',

	tags : '#ZDFroll', // see https://dev.twitter.com/rest/public/search for how to setup the search query

	consumer_key: '--',
  	consumer_secret: '--',
  	access_token_key: '--',
  	access_token_secret: '--'

	/*
		#love OR #hate : one or the other
		#love #hate : contains both tags
	*/

};

module.exports = Config;