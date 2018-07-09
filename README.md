


## Starting the project ##
    * virtualenv env
    * python manage.py
    * webpack (in new terminal window)

This starts the dev server as well as a webpack instance that watches our static assets for changes and compiles them. These compiled assets are then loaded in the browser.

#### Alternate way to start the project ####
    * npm start

This will start the dev server and webpack in a single window.. this is currently a little janky, god speed.


## Setting up new content types ##
    * Write plugin code in `styleguide/cms_plugin.py`
    * Add model code in `styleguide/models.py`
    * Add template to `styleguide/templates/*`
    * `npm run make-migrations`
    * 'npm run migrate`

    Ensure you add your migrations from `styleguide/migrations` to the git repo so that we can reproduce the site's database schema between tiers.

## Adding new scss or js ##
    * create your `*.scss` or `*.js`
    * add an import for your new file in the `main.scss` or `main.js`.


### Authors ###
Brandon Blanchard, Felix Lee, Tim Dolbear