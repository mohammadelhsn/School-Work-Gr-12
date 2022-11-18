const hours = document.getElementsByClassName('ellipsis hours_played');

let total = 0;

function getHours() {
	total = 0;

	for (game of hours) {
		const hour = parseFloat(game.innerHTML.split(' ')[0].replace(',', ''));

		if (isNaN(hour)) {
			return console.log(`Total hours: ${Math.round(total)} hour(s)`);
		}

		total += hour;
	}
}
