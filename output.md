usage: alembic [-h] [-c CONFIG] [-n NAME] [-x X] [--raiseerr]
               {branches,current,downgrade,edit,heads,history,init,list_templates,merge,revision,show,stamp,upgrade}
               ...

positional arguments:
  {branches,current,downgrade,edit,heads,history,init,list_templates,merge,revision,show,stamp,upgrade}
    branches            Show current branch points. :param config: a
                        :class:`.Config` instance. :param verbose: output in
                        verbose mode.
    current             Display the current revision for a database. :param
                        config: a :class:`.Config` instance. :param verbose:
                        output in verbose mode. :param head_only: deprecated;
                        use ``verbose`` for additional output.
    downgrade           Revert to a previous version. :param config: a
                        :class:`.Config` instance. :param revision: string
                        revision target or range for --sql mode :param sql: if
                        True, use ``--sql`` mode :param tag: an arbitrary
                        "tag" that can be intercepted by custom ``env.py``
                        scripts via the
                        :class:`.EnvironmentContext.get_tag_argument` method.
    edit                Edit revision script(s) using $EDITOR. :param config:
                        a :class:`.Config` instance. :param rev: target
                        revision.
    heads               Show current available heads in the script directory
                        :param config: a :class:`.Config` instance. :param
                        verbose: output in verbose mode. :param
                        resolve_dependencies: treat dependency version as down
                        revisions.
    history             List changeset scripts in chronological order. :param
                        config: a :class:`.Config` instance. :param rev_range:
                        string revision range :param verbose: output in
                        verbose mode.
    init                Initialize a new scripts directory. :param config: a
                        :class:`.Config` object. :param directory: string path
                        of the target directory :param template: string name
                        of the migration environment template to use.
    list_templates      List available templates :param config: a
                        :class:`.Config` object.
    merge               Merge two revisions together. Creates a new migration
                        file. .. versionadded:: 0.7.0 :param config: a
                        :class:`.Config` instance :param message: string
                        message to apply to the revision :param branch_label:
                        string label name to apply to the new revision :param
                        rev_id: hardcoded revision identifier instead of
                        generating a new one. .. seealso:: :ref:`branches`
    revision            Create a new revision file. :param config: a
                        :class:`.Config` object. :param message: string
                        message to apply to the revision; this is the ``-m``
                        option to ``alembic revision``. :param autogenerate:
                        whether or not to autogenerate the script from the
                        database; this is the ``--autogenerate`` option to
                        ``alembic revision``. :param sql: whether to dump the
                        script out as a SQL string; when specified, the script
                        is dumped to stdout. This is the ``--sql`` option to
                        ``alembic revision``. :param head: head revision to
                        build the new revision upon as a parent; this is the
                        ``--head`` option to ``alembic revision``. :param
                        splice: whether or not the new revision should be made
                        into a new head of its own; is required when the given
                        ``head`` is not itself a head. This is the
                        ``--splice`` option to ``alembic revision``. :param
                        branch_label: string label to apply to the branch;
                        this is the ``--branch-label`` option to ``alembic
                        revision``. :param version_path: string symbol
                        identifying a specific version path from the
                        configuration; this is the ``--version-path`` option
                        to ``alembic revision``. :param rev_id: optional
                        revision identifier to use instead of having one
                        generated; this is the ``--rev-id`` option to
                        ``alembic revision``. :param depends_on: optional list
                        of "depends on" identifiers; this is the ``--depends-
                        on`` option to ``alembic revision``. :param
                        process_revision_directives: this is a callable that
                        takes the same form as the callable described at :para
                        mref:`.EnvironmentContext.configure.process_revision_d
                        irectives`; will be applied to the structure generated
                        by the revision process where it can be altered
                        programmatically. Note that unlike all the other
                        parameters, this option is only available via
                        programmatic use of :func:`.command.revision` ..
                        versionadded:: 0.9.0
    show                Show the revision(s) denoted by the given symbol.
                        :param config: a :class:`.Config` instance. :param
                        revision: string revision target
    stamp               'stamp' the revision table with the given revision;
                        don't run any migrations. :param config: a
                        :class:`.Config` instance. :param revision: target
                        revision. :param sql: use ``--sql`` mode :param tag:
                        an arbitrary "tag" that can be intercepted by custom
                        ``env.py`` scripts via the
                        :class:`.EnvironmentContext.get_tag_argument` method.
    upgrade             Upgrade to a later version. :param config: a
                        :class:`.Config` instance. :param revision: string
                        revision target or range for --sql mode :param sql: if
                        True, use ``--sql`` mode :param tag: an arbitrary
                        "tag" that can be intercepted by custom ``env.py``
                        scripts via the
                        :class:`.EnvironmentContext.get_tag_argument` method.

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
                        Alternate config file
  -n NAME, --name NAME  Name of section in .ini file to use for Alembic config
  -x X                  Additional arguments consumed by custom env.py
                        scripts, e.g. -x setting1=somesetting -x
                        setting2=somesetting
  --raiseerr            Raise a full stack trace on error
