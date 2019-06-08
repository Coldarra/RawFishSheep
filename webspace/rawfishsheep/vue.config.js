module.exports = {
    devServer: {
        proxy: {
            '/api': {
                target: 'http://0.0.0.0/',
                ws: true, 
                changeOrigin: true,
                pathRewrite: {
                    '^/api': '/api'
                }   
            },
        }
    }
};
