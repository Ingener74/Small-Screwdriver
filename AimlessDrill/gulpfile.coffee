gulp = require 'gulp'
clean = require 'gulp-rimraf'
browserify = require 'gulp-browserify'
source = require 'vinyl-source-stream'
concat = require 'gulp-concat'

gulp.task 'clean', (cb)->
  clean ['./build/static', './build/templates'], cb

gulp.task 'clean-all', (cb)->
  clean './build', cb

gulp.task 'html', ->
  gulp.src './app/templates/*.html'
  .pipe gulp.dest './build/templates'

gulp.task 'css', ->
  gulp.src './app/static/css/*.css'
  .pipe gulp.dest './build/static/css'

###
  http://stackoverflow.com/questions/24656898/gulp-browserify-shim-and-jquery-depended
  https://www.npmjs.com/package/gulp-browserify
###
gulp.task 'cjsx', ->
  gulp.src './app/static/scripts/App.cjsx',
    read: false
  .pipe browserify
    transform: ['coffee-reactify']
    externsions: ['.cjsx']
    shim:
      react:
        path: 'bower_components/react/react.min.js'
        exports: 'react'
      bootstrap:
        path: 'bower_components/bootstrap/dist/js/bootstrap.min.js'
        exports: 'bootstrap'
  .pipe concat 'bundle.js'
  .pipe gulp.dest './build/static/js/'

gulp.task 'build', ['html', 'css', 'cjsx']

gulp.task 'build-all'

gulp.task 'default', ['clean', 'build']

