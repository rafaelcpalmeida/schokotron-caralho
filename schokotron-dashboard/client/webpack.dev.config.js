var webpack = require('webpack');
var path = require('path');

var BUILD_DIR = path.resolve(__dirname, './build');
var APP_DIR = path.resolve(__dirname, './src');

const config = {
    entry: {
        main: APP_DIR + '/app.js'
    },
    output: {
        filename: 'bundle.js',
        path: BUILD_DIR,
        publicPath: '/'

    },
    module: {
        rules: [
            {
                test: /(\.css|.scss)$/,
                use: [{
                    loader: "style-loader"
                }, {
                    loader: "css-loader",
                    options: {
                        modules: true,
                    },
                }, {
                    loader: "sass-loader"
                }],

            },
            {
                test: /\.(jsx|js)?$/,
                use: [{
                    loader: "babel-loader",
                    options: {
                        cacheDirectory: true,
                        presets: ['react', 'es2015', 'stage-1']
                    }
                }]
            }
        ],
    },
    devServer: {
        contentBase: parentDir,
        historyApiFallback: true
    }
};

module.exports = config;