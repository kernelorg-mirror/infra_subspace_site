What is subspace running?
=========================

The subspace server is running:

- postfix_
- mlmmj_
- public-inbox_

Postfix and mlmmj are set up as the upstream docs recommend, so please
see the README.postfix_ file in the mlmmj repository for reference.

.. _postfix: https://www.postfix.org/
.. _mlmmj: https://codeberg.org/mlmmj/mlmmj
.. _public-inbox: https://public-inbox.org/
.. _README.postfix: https://codeberg.org/mlmmj/mlmmj/src/branch/master/README.postfix


Configuring public-inbox with mlmmj
-----------------------------------

public-inbox reads messages directly from the mlmmj archives. This way,
the archives get every message that the list accepted, even if delivery
to some subscribers has problems.

mlmmj keeps one file per message in its archive directory, which is the
same layout as an MH folder. public-inbox-watch can watch it as it is::

    watch = mh:/var/spool/mlmmj/test.lists.linux.dev/archive

This only does work when a new message arrives.


List headers
------------

mlmmj adds the standard ``List-*`` headers (RFC 2919 and RFC 2369) by
itself. We only add one more, because many people filter on it::

    X-Mailing-List: test@lists.linux.dev


DMARC compliance measures
-------------------------

To stay compatible with DMARC, mlmmj makes no changes to the body or to
the signed headers of each message. In particular, we do not set the
``prefix`` or ``footer`` tunables, because subject tags and footers
would break the author's DKIM signature.

We also:

- ARC-seal incoming posts, so receivers that trust our seal can accept
  them even if the author's DKIM signature does not survive the trip
- reject posts that fail DMARC when the author's domain has
  ``p=reject``, because the subscribers' servers would refuse them too

Note that if the original message has no DKIM signature, DMARC will
fail no matter what we do. But a domain that has a DMARC policy and does
not sign its mail is misconfigured anyway.
