var homepage = function(req, res) {
    res.render('main.ejs');
}

var routes = {
    gethomepage: homepage,
};

module.exports = routes;