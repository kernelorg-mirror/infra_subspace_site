Subscribing to lists
====================

.. note::

   Most lists do not require subscribing in order to post a message, so
   you only need to subscribe if you are interested in receiving a copy
   of all mail messages sent to the list.

Subscribing for email delivery
------------------------------
The mailing lists are managed by `mlmmj <https://codeberg.org/mlmmj/mlmmj>`_,
so in order to subscribe to receive messages via email you will need to
send a message to a special subscription address of the list.

For example, if you want to subscribe to ``test@lists.linux.dev``:

- to receive an **individual copy of every message sent to the list**,
  send an email to::

    test+subscribe@lists.linux.dev

- to receive a **daily digest of all messages sent to the list**,
  send an email to::

    test+subscribe-digest@lists.linux.dev

The subject or body of the message do not make a difference and can be
left blank.

.. warning:: If you use Gmail

   If you are a Gmail user, please do not subscribe to high-volume
   lists, because this will almost certainly push you over Gmail's
   delivery quotas (60 messages per second, specifically). This may
   cause you to miss important mail.

Unsubscribing to stop receiving list mail
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To stop receiving mail from any list, send a message to the unsubscribe
address of the list. For example, to unsubscribe from either the full or
digest version of the test list, send a message to::

    test+unsubscribe@lists.linux.dev

Subscribing via NNTP
--------------------
NNTP is an old but still popular mechanism for exchanging usenet forum
messages. If a mailing list is configured to provide a message archive,
you can subscribe to it via NNTP.

In your usenet-capable client, provide the following NNTP server to use:

- ``nntp://nntp.lore.kernel.org``

Once the connection is established, you can retrieve the list of groups
and subscribe to the list you need.

The group names are usually the list-id of the list in reverse order.
For example, if the list address is ``patches@lists.linux.dev``, then
the NNTP group will be ``dev.linux.lists.patches``.
