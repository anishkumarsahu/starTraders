self.addEventListener('install', function(event){

	console.log('installed');
	event.waitUntil(
	    caches.open('static')
        .then(function (cache) {
            cache.addAll([
                '/static/logo/logo.png',
                '/static/cssMain/semantic.min.css',
                '/static/cssMain/dataTables.semanticui.min.css',
                '/static/cssMain/tableCss/dataTables.semanticui.min.css',
                '/static/cssMain/tableCss/buttons.semanticui.min.css',
                '/static/cssMain/jquery-confirm.min.css',
                '/static/jsMain/jquery.min.js',
                '/static/jsMain/semantic.min.js',
                '/static/jsMain/jquery.dataTables.min.js',
                '/static/jsMain/dataTables.semanticui.min.js',
                '/static/jsMain/jquery-confirm.min.js',
                '/static/jsMain/tablesort.js',
                '/static/table/dataTables.buttons.min.js',
                '/static/table/buttons.semanticui.min.js',
                '/static/table/jszip.min.js',
                '/static/table/pdfmake.min.js',
                '/static/table/vfs_fonts.js',
                '/static/table/buttons.html5.min.js',
                '/static/table/buttons.print.min.js',
                '/static/table/buttons.colVis.min.js',
            ]);

        })
    );

});

self.addEventListener('activate', function(event){
    console.log('activated');
});

self.addEventListener('fetch', function(event){
  event.respondWith(
      caches.match(event.request).then(function (res) {
          if (res){
              return res;
          }
          else {
              return fetch(event.request);
          }
      })
  )
  // return something for each interception
});/**
 * Created by anish on 15/7/19.
 */
