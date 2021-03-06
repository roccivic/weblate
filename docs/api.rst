.. _api:

Weblate's Web API
=================

.. _hooks:

Notification hooks
------------------

Notification hooks allow external applications to notify weblate that Git
repository has been updated.

.. describe:: GET /hooks/update/(string:project)/(string:subproject)/

   Triggers update of a subproject (pulling from Git and scanning for
   translation changes).

.. describe:: GET /hooks/update/(string:project)/

   Triggers update of all subprojects in a project (pulling from Git and
   scanning for translation changes).

.. describe:: POST /hooks/github/

    Special hook for handling Github notifications and automatically updating
    matching subprojects.

    .. note::

        The GitHub notification relies on Git repository urls you use to be in form
        ``git:/github.com/owner/repo.git``, otherwise automatic detection of used
        repository will fail.

    .. seealso:: http://help.github.com/post-receive-hooks/

Exports
-------

Weblate provides various exports to allow you further process the data.

.. describe:: GET /exports/stats/(string:project)/(string:subproject)/

    Retrieves statistics for given subproject in JSON format.

    Example response::

        [
            {
                "code": "cs", 
                "fuzzy": 0, 
                "fuzzy_percent": 0.0, 
                "last_author": "Michal \u010ciha\u0159",
                "last_change": "2012-03-28T15:07:38+00:00",
                "name": "Czech", 
                "total": 436, 
                "translated": 436, 
                "translated_percent": 100.0, 
                "url": "http:/l10n.cihar.com/projects/weblate/master/cs/"
            }, 
            {
                "code": "nl", 
                "fuzzy": 11, 
                "fuzzy_percent": 2.5, 
                "last_author": null,
                "last_change": null,
                "name": "Dutch", 
                "total": 436, 
                "translated": 319, 
                "translated_percent": 73.2, 
                "url": "http:/l10n.cihar.com/projects/weblate/master/nl/"
            }, 
            {
                "code": "el", 
                "fuzzy": 21, 
                "fuzzy_percent": 4.8, 
                "last_author": null,
                "last_change": null,
                "name": "Greek", 
                "total": 436, 
                "translated": 312, 
                "translated_percent": 71.6, 
                "url": "http:/l10n.cihar.com/projects/weblate/master/el/"
            }, 
        ]
