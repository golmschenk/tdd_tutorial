var initialize = function (navigator, user, token, urls) {
    $('#id_login').on('click', function () {
        navigator.id.request();
    });
    navigator.id.watch({
        loggedInUser: user,
        onlogin: function (assertion) {
            var deferred = $.post(urls.login, $.param({assertion: assertion, csrfmiddlewaretoken: token}));
            deferred.done(function () { window.location.reload(); });
            deferred.fail(function () { navigator.id.logout(); });
        },
        onlogout: function () {}
    });
};

window.Superlists = {
    Accounts: {
        initialize: initialize
    }
};

