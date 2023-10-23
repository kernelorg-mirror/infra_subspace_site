Mailing list etiquette
======================

.. note::
   This page is the adapted version of ``Notes about netiquette
   <https://people.kernel.org/tglx/notes-about-netiquette>`` by Thomas
   Gleixner.

Send "plain text" mail only
---------------------------
The most common problem experienced by new mailing list participants is
that their mail was rejected because it contained HTML. Generally, HTML
mail is not accepted for the following reasons:

- HTML is a very rich standard that requires complex parsing/rendering
  engines to properly display message contents. These rendering engines
  have very large attack surfaces that allow bad actors to perform
  actions like deliver harmful payloads, track the recipients' location,
  leak private details about their work environment, etc.
- HTML mail is very commonly used by spammers to defeat anti-spam
  tooling (e.g. by hiding large parts of the message with invisible
  fonts, using hidden elements, etc).
- Many kernel developers prefer using terminal-based email tools that
  better integrate with their workflows. Reading HTML messages in such
  tools is often not supported.
- Messages that send both plain text and HTML parts are often seen as
  unnecessary bloat that just consumes resources.

For these reasons almost all kernel mailing lists will reject HTML
email.

How to send plain text email?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Almost all email clients, whether they are browser-based or standalone
applications, support sending "plain text" email. Please check
documentation for your app or provider and make sure that it is
configured to send outgoing mail only in plain text, without the HTML
part.

.. note::
   A lot of mobile phone apps do not have any way to disable sending
   HTML mail, so please use a regular desktop or browser app.

Use a succinct but descriptive subject line
-------------------------------------------
The subject line is what the list users will see first, and they will
decide whether to read your message or skip it based on whether they
think your email is relevant.

Bad example::

    Subject: help

Good example::

    Subject: backporting frobbledev to kernel 5.15

Bad example::

    Subject: bug

Good example::

    Subject: frobbledev data corruption with kernel 6.5

Do not include "confidentiality disclaimers"
--------------------------------------------
When posting to public mailing lists the boilerplate confidentiality
disclaimers are not only meaningless, they are absolutely wrong for
obvious reasons.

If that disclaimer is automatically inserted by your corporate e-mail
infrastructure, talk to your manager, IT department or consider using a
different e-mail address which is not affected by this policy. Many IT
companies have dedicated e-mail infrastructure for kernel developers to
specifically avoid this situation.

Always "reply to all"
---------------------
If you received a reply to your message on the list, always reply-all
when composing a response, unless you have a good reason for doing so
(e.g. discussing a private matter). Replying only to the sender of the
e-mail immediately excludes all other list recipients and defeats the
purpose of mailing lists by turning a public discussion into a private
conversation.

Do not "top-post" when replying
-------------------------------
Top-posting is the preferred style in corporate communication, but
kernel mailing list discussions commonly require proper context for
maximum clarity. For this reason, kernel mailing lists exclusively
require that all replies are sent as interleaved quoted replies.

For example::

    On Mon, Oct 23, 2023 at 08:55:56AM -1000, Rando Reviewer wrote:
    > How do you intend to handle these cases:
    >
    > - your device is frobbled

    In the case of frobbling, we reinitialize the device after a
    5-second sleep in firmware.

    > - your device is blimpoxed

    This is not currently supported by the manufacturer, so we pretend
    that blimpoxing never happens.

This style allows the person reviewing your submission to quickly
establish proper context for all your replies. Please also see below.

Trim your quotes when replying
------------------------------
Maintainer time is extremely precious, so they will greatly appreciate
if you trim the quoted text in your reply and only leave that
information which is crucial to establish the context of your reply.

For example, this is quoting too much::

    On Mon, Oct 23, 2023 at 08:55:56AM -1000, Rando Reviewer wrote:
    > Hello:
    > 
    > Thank you very much for following up with replies! I have
    > re-reviewed the patches you sent, but I still have concerns.
    > 
    > As you may know, the frobble subsystem is currently being
    > deprecated in favor of using systemd-flargle. While we still
    > accept device drivers written to the older spec, we need
    > to ensure that there will be dedicated resources at your
    > company that can convert to systemd-flargle when it becomes
    > the one and only true way of doing things.
    > 
    > Are there resources allocated at your company to make sure
    > the driver is properly rewritten to use systemd-flargle?
    
    Yes, we have dedicated a bajillion dollars to these efforts.
    
    -- 
    Dev Eloper
    Frobbledev Inc
    
    > Otherwise, I will queue up your submission when the merge
    > window opens up in a couple of weeks.
    >
    > Thanks!
    > 
    > -- 
    > Rando Reviewer
    > Reviewing-is-our.biz

This is much better because it leaves just enough context for the
reviewer to understand your reply and removes the bottom of the message
that is completely irrelevant::

    On Mon, Oct 23, 2023 at 08:55:56AM -1000, Rando Reviewer wrote:
    > Are there resources allocated at your company to make sure
    > the driver is properly rewritten to use systemd-flargle?

    Yes, we have dedicated a bajillion dollars to these efforts.

    -- 
    Dev Eloper
    Frobbledev Inc

Do not quote large chunks of code
---------------------------------
If you want to refer to code or a particular function, mentioning the
file and function name is usually sufficient. Maintainers and developers
generally don't need a link to a web interface with the code to be able
to understand the proper context.

If you do decide to quote some code to illustrate your message, try to
include only those lines that are relevant to the problem and ``[skip]``
the code that is unnecessary to understand your point.
