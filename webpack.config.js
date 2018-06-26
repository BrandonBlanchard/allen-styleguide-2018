const path = require('path'),
    url = require('file-loader'),
    webpack = require('webpack'),
    glob = require('glob'),
    MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
    entry: [path.resolve(process.cwd(), 'styleguide', 'static', 'script', 'main.js'),
            path.resolve(process.cwd(), 'styleguide', 'static', 'style', 'main.scss') ],
    output: {
        filename: 'site.js',
        libraryTarget: 'umd',
        path: path.resolve(process.cwd(), 'styleguide', 'static', 'build'),
        publicPath: '/static/'
    },
    resolve: {
        modules: ['node_modules']
    },
    optimization: {
        splitChunks: {
            cacheGroups: {
                styles: {
                    name: 'site',
                    test: /\.css$/,
                    chunks: 'all',
                    enforce: true
                }
            }
        }
    },
    module: {
        rules: [
            {
                test: /\.(js?)$/,
                exclude: ['node_modules'],

                use: [{
                    loader: 'babel-loader',
                    options: {
                        presets: [
                            ["env", [
                                // http://browserl.ist/?q=last+5+versions
                                {"targets": {
                                  "browsers": ["last 5 versions"]
                                }}
                            ]],
                            "stage-0"
                        ]
                    }
                }]
            },
            {
                test: /\.scss$/i,
                use: [
                    {
                        loader: MiniCssExtractPlugin.loader,
                    },
                    {
                        loader: 'css-loader',

                        options: {
                            // modules: true,
                            // importLoaders: 1,
                            // localIdentName: '[name]__[local]--[hash:base64:5]'
                        }
                    },
                    {
                        loader: 'sass-loader',
                        options: {
                            includePaths: ['node_modules']
                                .map(d => path.join(__dirname, d))
                                .map(g => glob.sync(g))
                                .reduce((a, c) => a.concat(c), [])
                        }
                    }
                ]
                
            }
        ]
    },
    performance: {
        hints: "warning",
        maxEntrypointSize: 2000000,
        maxAssetSize: 2000000
    },
    watch: true,
    watchOptions: {
        poll: true
    },
    plugins: [
        new MiniCssExtractPlugin({
            filename: "site.css"
        })
    ]
};