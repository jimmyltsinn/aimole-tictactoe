gulp = require 'gulp'
plugins = require('gulp-load-plugins')()

config = require './config'

gulp.task 'watch-lint', () ->
	plugins.watch [].concat.apply(config.files.coffee, config.files.js), () -> gulp.start 'lint'

gulp.task 'watch-mocha', () ->
	plugins.watch config.files.mocha, () -> gulp.start 'mocha'

gulp.task 'watch-jsx', () ->
	plugins.watch config.files.jsx, () -> gulp.start 'browserify'

gulp.task 'watch-html', () ->
	plugins.watch config.files.html, () -> gulp.start 'html'

gulp.task 'livereload-start', () ->
	plugins.livereload.listen config.livereload.port

gulp.task 'watch', ['livereload-start', 'watch-html', 'watch-jsx', 'watch-mocha', 'watch-lint']
