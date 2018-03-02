const path = require('path');

// noinspection WebpackConfigHighlighting
module.exports = {
    entry: './templates/insurance/risks/risks.js',
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, 'dist')
    },
    mode: 'development'
};