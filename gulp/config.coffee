path = require 'path'
babelify = require 'babelify'

module.exports =
	publicDir: 'dist/'
	files:
		coffee: ['*.coffee', 'test/**/*.coffee', 'gulp/**/*.coffee']
		js: ['render/**/*.js']
		jsx: ['render/**/*.jsx']
		html: ['render/**/*.html']
		mocha: ['test/**/*.coffee']
	livereload:
		port: 32759
