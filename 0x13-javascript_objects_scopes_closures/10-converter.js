#!/usr/bin/nod

exports.converter = function (base) {
	return (num) => {
		return num.toString(base);
	};
};
