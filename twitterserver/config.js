/* CONFIG FILE */

var Config = {
	
	databaseFile : __dirname + "/data", //chmod this path 777

	settingsFile : __dirname + "/data/settings.json",

	baseUrl : '/app/', // with trailing /
	servePublicDir : true,
	hostname : false, // 127.0.0.1 = private, false = public
	port : '8081',

	tags : '#ZDFroll', // see https://dev.twitter.com/rest/public/search for how to setup the search query

	consumer_key: 'Du57s8tX7GazSMv2ri3u0vI3j',
  	consumer_secret: 'nkd3DXo6EiXhURKVRfdQ4dmnCkBpJqf0uJxOFE61xLHckBwjcg',
  	access_token_key: '855059771736641537-DkvMwItqbsCeM4KMMWwraDb1lpxwxx6',
  	access_token_secret: 'KVvmfX7rLCh5jdJveyPqmM0K8vEk8eCJpdXtkox7snlgW'

	/*
		#love OR #hate : one or the other
		#love #hate : contains both tags
	*/

};

module.exports = Config;