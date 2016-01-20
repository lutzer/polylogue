var socketio = require('socket.io');
var submissions = r_require('/models/submissions');

var appEvents = r_require('/utils/appEvents');

module.exports = function (http) {

	var io = socketio(http);

	io.on('connection', function(socket){

	    console.log('Socket: User connected');

	    // Server event handlers

	    function submissionAddedHandler(doc) {
	    	console.log('send submidssion:new');
		    socket.emit('submissions:new',{data: doc});
	    }
		appEvents.on('submission:added', submissionAddedHandler);

		socket.on('error', function(err) {
	    	console.log(err);
		});

	    // Clean up after disconnect

	    socket.on('disconnect', function(){
	        console.log('Socket: User disconnected');

	        //remove server events
	        appEvents.removeListener('submissions:new',submissionAddedHandler);
	    });

	});

};