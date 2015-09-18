gulp = require 'gulp'
del = require 'del'
browserify = require 'gulp-browserify'
source = require 'vinyl-source-stream'
concat = require 'gulp-concat'
minifyCss = require 'gulp-minify-css'
runSequence = require 'run-sequence'
browserSync = require 'browser-sync'
exec = require('child_process').exec;

gulp.task 'clean', ->
  del ['./build/static', './build/templates']

gulp.task 'clean-all', ->
  del ['./build']

gulp.task 'html', ->
  gulp.src './app/templates/*.html'
  .pipe gulp.dest './build/templates/'

gulp.task 'css', ->
  gulp.src [
    './app/static/css/*.css',
    './bower_components/bootstrap/dist/css/*.min.css'
  ]
  .pipe minifyCss()
  .pipe concat 'style.css'
  .pipe gulp.dest './build/static/css/'

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

gulp.task 'py', ->
  gulp.src ['./app/*.py']
  .pipe gulp.dest './build/'

gulp.task 'build', ['html', 'css', 'cjsx', 'py']

gulp.task 'runserver', ->
  exec 'cd build && python AimlessDrill.py', (err, stdout, stderr)->
    console.log stdout
    console.log stderr

###
  https://github.com/pebreo/gulp-browsersync-flask/blob/master/gulpfile.js
###
gulp.task 'browser-sync', ->
  browserSync
    notify: false
    proxy: "127.0.0.1:5003"

gulp.task 'default', (cb)->
  runSequence 'clean', ['build'], 'runserver', 'browser-sync', 'watch', cb

gulp.task 'watch', ->
  gulp.watch [
    'app/**/*'
  ], ['build', browserSync.reload]

gulp.task 'build-all'

###
  TODO
  * use ref
  * browser sync
  * start flask
  * deploy
  * watch
  * ...
###