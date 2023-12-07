What is subspace running?
=========================

The subspace server is running:

- postfix_
- mlmmj_
- public-inbox_

Postfix and mlmmj are configured exactly as recommended by the upstream
docs, so please refer to the README.postfix_ file in the upstream
repository for the reference.

.. _postfix: https://www.postfix.org/
.. _mlmmj: https://codeberg.org/mlmmj/mlmmj
.. _public-inbox: https://public-inbox.org/
.. _README.postfix: https://codeberg.org/mlmmj/mlmmj/src/branch/master/README.postfix


Configuring public-inbox with mlmmj
-----------------------------------

Our public-inbox instance is configured to read messages directly from
the mlmmj archives, with the goal to ensure that public-inbox feeds have
the latest messages regardless of any delivery problems that may happen
on the SMTP layer between us and subscribers.

To achieve this, our automation creates lists with the following
structure::

    /var/spool/mlmmj/test.lists.linux.dev/
        ...
        maildir-archive/
            new/
            cur/
            tmp/
        archive -> maildir-archive/new

This way mlmmj writes archives messages into the ``maildir-archive/new``
directory and the public-inbox-watch process monitors it for any new
arriving messages::

    watch=maildir:/var/spool/mlmmj/test.lists.linux.dev/maildir-archive/

This process is very IO-efficient and only runs when there are actual
new entries in the archives directory.

DMARC compliance measures
-------------------------

To be compliant with current DMARC policies, it is sufficient to
configure mlmmj to make no changes to the headers or body of each
processed message. Specifically, do not set the ``prefix`` or ``footer``
tunables.

We only add the following custom headers that are required for list
operation (using the test list for illustration purposes)::

    Precedence: bulk
    X-Mailing-List: test@lists.linux.dev
    List-Id: <test.lists.linux.dev>
    List-Subscribe: <mailto:test+subscribe@lists.linux.dev>
    List-Unsubscribe: <mailto:test+unsubscribe@lists.linux.dev>

Note, that if there is no DKIM signature on the originating message, the
DMARC verification will fail regardless of anything we do, but
situations where there's a DMARC policy configured for a domain without
a corresponding DKIM signature are invalid anyway.

As a final note, more work will be required in the near future to remain
DMARC-compliant. Once Replay-Resistant ARC becomes an accepted and
enforced standard, setting the ``Forwarded-to:`` header and ARC-signing
all recipients will become a required step. For more info, see:

* https://datatracker.ietf.org/doc/draft-chuang-replay-resistant-arc/

