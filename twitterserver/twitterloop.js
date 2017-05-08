var Twitter = require('twitter');
var _ = require('underscore');

var config = r_require('/config.js');
var appEvents = r_require('/utils/appEvents.js');

var client = new Twitter({
  consumer_key: config.consumer_key,
  consumer_secret: config.consumer_secret,
  access_token_key: config.access_token_key,
  access_token_secret: config.access_token_secret
});

module.exports = {

	run : function(intervall) {

		if (_.has(settings.values, "lastId")) {
			this.lastId = settings.values.lastId;
		} else {
			this.lastId = 0;
		}

		setInterval(() => {
			this.loop.call(this);
		}, intervall);
	},

	loop : function() {
	
		client.get('search/tweets', {q: config.tags+' -filter:retweets', count: 3, since_id: this.lastId, result_type: 'recent'}, (err, tweets, response) => {
			  if(err) {
			  	console.log(err);
			  	return;
			  }

			  // client.get('application/rate_limit_status', {}, (err, tweets, response) => {
				 //  if(err) {
				 //  	console.log(err);
				 //  	return
				 //  }
				 //  console.log(tweets.resources.search);
			  // });

			  if (!_.has(tweets,'statuses'))
			  	return;

			  if (_.isEmpty(tweets.statuses))
			  	return;

			  _.forEach(tweets.statuses, (tweet) => {
			  		if (tweet.id != this.lastId) {
						console.log('Received: '+tweet.text+", id:"+tweet.id);

						var data = {
					        message : tweet.text
					    };
						appEvents.emit('submission:new', data);
			  		}
			  });

			  this.lastId = _.max(_.pluck(tweets.statuses,'id'));

			  settings.values = { lastId : this.lastId };
			  settings.write();
			
			});
	}
}