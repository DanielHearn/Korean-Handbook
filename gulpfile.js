var gulp = require('gulp');
var sass = require('gulp-sass');
var useref = require('gulp-useref');
var runSequence = require('run-sequence');
var cache = require('gulp-cache');
var del = require('del');
var imagemin = require('gulp-imagemin');
var uglify = require('gulp-uglify');
var cssnano = require('gulp-cssnano');
var gulpIf = require('gulp-if');
var pug = require('gulp-pug');
var browserSync = require('browser-sync').create();
var ghpages = require('gh-pages');
var path = require('path');

const scssSource = 'src/scss/*.scss';
const cssDest = 'src/css';

gulp.task('browserSync', function() {
  browserSync.init({
    server: {
      baseDir: 'src'
    },
  })
});

gulp.task('sass', function() {
  return gulp.src(scssSource)
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest(cssDest))
    .pipe(browserSync.stream())
    .pipe(cssnano({zindex: false}))
})

gulp.task('useref', function(){
  return gulp.src('src/*.html')
    .pipe(useref())
    //.pipe(gulpIf('src/js/*.js', gulp.dest('dist')))
    //.pipe(gulpIf('*.css', cssnano({zindex: false})))
    .pipe(gulp.dest('dist'))
});

gulp.task('js', function(){
  return gulp.src('src/js/*.js')
    .pipe(gulp.dest('dist/js'))
});

gulp.task('css', function(){
  return gulp.src('src/css/*.css')
    .pipe(gulp.dest('dist/css'))
});

gulp.task('images', function(){
  return gulp.src('src/img/*.+(png|jpg|jpeg|gif|svg)')
    .pipe(cache(imagemin()))
    .pipe(gulp.dest('dist/img'))
});

gulp.task('favicons', function(){
  return gulp.src('src/favicons/*.+(png|jpg|jpeg|gif|svg|ico|xml|json)')
  .pipe(gulpIf('*.+(png|jpg|jpeg|gif|svg)', cache(imagemin())))
  .pipe(gulp.dest('dist/favicons'))
});

gulp.task('pug', function buildHTML() {
  return gulp.src('src/pug/*.pug')
    .pipe(pug())
    .pipe(gulp.dest("src/"))
});

gulp.task('clean:dist', function() {
  return del.sync(['dist/**/*']);
});

gulp.task('watch', ['browserSync', 'pug', 'sass'], function (callback){
  gulp.watch('src/pug/*.pug', ['pug']);
  gulp.watch(scssSource, ['sass']);
  gulp.watch('src/*.html').on('change', browserSync.reload)
  gulp.watch('src/js/*.js', browserSync.reload)
})

gulp.task('build', function (callback) {
  runSequence('clean:dist',
    ['pug', 'sass', 'images', 'favicons', 'js', 'css'], 'useref',
    callback
  )
})

gulp.task('default', function(callback) {
  runSequence(['sass', 'pug', 'browserSync'], 'watch',
    callback
  )
})

gulp.task('deploytopages', function() {
  ghpages.publish('dist', function(err) {});
});

gulp.task('deploy', function(callback) {
  runSequence(['build'], 'deploytopages',
    callback
  )
});
