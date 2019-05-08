module.exports = {

    publicPath: process.env.NODE_ENV === 'production'
        ? '/dist2/'
        : '/',
    
    devServer: {
        proxy: {
            '/api': {
                target: 'http://127.0.0.1/',
                // target: 'http://coldarra.cn:8848/',
                ws: true,
                changeOrigin: true,
                // pathRewrite: {
                //     '^/api': '/api'
                // }
            },
            '/static': {
                target: 'http://127.0.0.1/',
                // target: 'http://coldarra.cn:8848/',
                ws: true,
                changeOrigin: true,
                // pathRewrite: {
                //     '^/static': '/static'
                // }
            },
        }
    }
}
