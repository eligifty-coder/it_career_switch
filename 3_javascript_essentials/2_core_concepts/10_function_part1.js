let max =0
function findMax(a, b, c, d, e, f) {
	for (i = 0; i < arguments.length; i++) {
		if (arguments[i] > max) {
			max = arguments[i];
		}
	}
	return max;
}

x = findMax(1, 23, 500, 115, 44, 88);
