var Twitter = require('twitter');
var _ = require('underscore');

var config = r_require('/config.js');
var appEvents = r_require('/utils/appEvents.js');

var client = new Twitter({
  consumer_key: 'xZvXusMhegnEKZyrSDf32JbMb',
  consumer_secret: 'I5zxJwtWVZWwMWfWiVuR3OzYOZydAClfQIqIrIzXequTKrXh5G',
  access_token_key: '855059771736641537-z5DrxaKVe4KaEXwSRgPSHQWApPrgQku',
  access_token_secret: 'ammqgew75XZ8NUmD8GuRFKukckJtwbVxjjrOLwvn550Ds'
});

module.exports = {

	run : function(intervall) {
		this.lastId = 0;
		setInterval(() => {
			this.loop.call(this);
		}, intervall);
	},

	loop : function() {
	
		client.get('search/tweets', {q: config.tags+' -filter:retweets', count: 3, since_id: this.lastId, result_type: 'recent'}, (err, tweets, response) => {
			  if(err) {
			  	console.log(err);
			  	return
			  }

			  if (!_.has(tweets,'statuses'))
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
			});
	}
}