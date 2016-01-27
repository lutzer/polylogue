var exec = require('child_process').exec;

var message = "TESTTESTTEST space+#98301";

var process = exec('python2 polylogue.py -m "'+message+'"',
	(error, stdout, stderr) => {
		console.log(stdout);	
		if (error !== null) {
      		console.log(`exec error: ${error}`);
    	}
	}
);