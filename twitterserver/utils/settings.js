var fs = require("fs");

module.exports = {

	values : {},

	path : "",

	read : function(path) {

		this.path = path;
		
		// read file if it exists
		try {
			var string = fs.readFileSync(this.path, 'utf8');
			this.values = JSON.parse(string);
		} catch (err) {
			this.values = {};
		}
	},

	write : function() {

		// open file
		var file = fs.openSync(this.path,"w+");

		// write file
		var string = JSON.stringify(this.values);
		fs.writeSync(file, string, 0, 'utf8');

		fs.closeSync(file);

	}
}