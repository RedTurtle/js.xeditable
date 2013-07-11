from fanstatic import Library, Resource, Group
from js.bootstrap import bootstrap
from js.jquery import jquery

library = Library('x-editable', 'resources')

bootstrap_editable = Group([
                        Resource(library, 
                              'bootstrap-editable/js/bootstrap-editable.js',
                              minified='bootstrap-editable/js/bootstrap-editable.min.js',
                              depends=[bootstrap]),
                        Resource(library, 
                              'bootstrap-editable/css/bootstrap-editable.css'),
                        ])

jquery_editable = Group([
                        Resource(library, 
                              'jquery-editable/js/jquery-editable-poshytip.js',
                              minified='jquery-editable/js/jquery-editable-poshytip.min.js',
                              depends=[jquery]),
                        Resource(library, 
                              'jquery-editable/css/jquery-editable.css'),
                        ])

jqueryui_editable = Group([
                        Resource(library, 
                              'jqueryui-editable/js/jqueryui-editable.js',
                              minified='jqueryui-editable/js/jqueryui-editable.min.js',
                              depends=[jquery]),
                        Resource(library, 
                              'jqueryui-editable/css/jqueryui-editable.css'),
                        ])
