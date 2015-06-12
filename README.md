# get-polymer-imports
Simple python script to get all the polymer imports from a bower_components directory

# Usage

`./get_polymer_imports bower_components` outputs a 'acceptable' HTML imports.

Essentially, it excludes `demo`, `test`, and `src` directories.  It also ignores the `polymer` directory, and simply uses `../bower_components/polymer/polymer.html`.

If you want to change the initial prefix from `..`, simply add that as the second argument, i.e.:

`./get_polymer_imports bower_components ''` to use no prefix.

It will also work on a `components` directory, but nothing else, because who knows what hell will break lose otherwise.
