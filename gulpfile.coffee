requireDir = require 'require-dir'
requireDir './gulp'

gulp = require 'gulp'

gulp.task 'travis', ['lint', 'test']
gulp.task 'update-client', ['browserify', 'html']
gulp.task 'default', ['watch', 'update-client']

gulp.task 'test', ['mocha']
gulp.task 'build', ['browserify', 'html']
