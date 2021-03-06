var socketio = require('socket.io');
var submissions = r_require('/models/submissions');

var appEvents = r_require('/utils/appEvents');

module.exports = function (http) {

	var io = socketio(http);

	io.on('connection', function(socket){

	    console.log('Socket: User connected');

	    // Server event handlers

	    function submissionAddedHandler(doc) {
	    	console.log('socket emit:<submission:new>');
		    socket.emit('submission:new',{data: doc}); // this will send the data to the python printserver
	    }
		appEvents.on('submission:new', submissionAddedHandler);

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