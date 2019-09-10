console.log("Detected script.js");
var app = (function () {
	
	var start = function() {
		getHeadlines();
	}
	
	var getHeadlines = function () {
		var headlines = [
			'Follow us on Twitter @KeatonSample @daydreamjesse',
			'Missed an episode? Catch up on Keaton\'s YT Channel'
			];
		
		for(var i = 0; i < headlines.length; i++) {
			var concatHeadlines = headlines.join(" - ");
			$("#marquee").text(concatHeadlines);
		}
	}
	
	return {
		start: start
	}
)} ();

app.start();
