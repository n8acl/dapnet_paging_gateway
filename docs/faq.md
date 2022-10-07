# Frequently Asked Questions (FAQ)

## How does this work?

!!! note ""
    There is alot of technical mumbo jumbo I can get into, but simply just know that there is alot of Python and Asterisk Magic going on in the background. There is alot of data being pulled, messaged and loaded from various sources to make it all work.

## Why DMR ID for dialing a person instead of RIC or some other extension?

!!! note ""
    DMR ID is a universal number that any ham can have. That is why this was chosen. There is not a way to cross reference Pager RICS to Callsigns from DAPNET. Plus DAPNET uses a modified version of a persons DMR ID as the Pager RIC, if they do not provide one from the pager they have. So using this method, a user can send a page to any DAPNET Subscriber. The script that is used will convert the DMR ID to a callsign to send the page to them via the DAPNET API.

## How do I know or how do I find out if the person I want to page is a DAPNET Subscriber?

!!! note ""
    Yeah. This is a tricky question as there really is no straight answer. There are some ways to do this:

      * First off, the easiest way is to ask the person you are wanting to send pages to.
      * If you are a DAPNET Subscriber yourself, you can login to the DAPNET website and do a search for the person. If they come up, they are a subscriber. However, they need to have everything setup and configured for it to go through.

    Otherwise, there really isn't a straight forward way

## So how do I find a person's DMR ID?

!!! note ""
    Once you know if a person is a DAPNET subscriber, you can go to [RadioID.Net](https://radioid.net) and use the online database search to get their DMR ID. And of course, you can always ask the person you want to page for their DMR ID.

### What if they don't have a DMR ID?

!!! note ""
    Then you are not able to use this system to page them. Sorry. There is nothing I can do about that.

### How do I know if the page went through?

!!! note ""
    Just like in the old days, the only way you know it went through and if they got it is if they call you back. You just have to cross your fingers and hope for the best.

### What happens if I try to page someone who is not a DAPNET subscriber?

!!! note ""
    Absolutly nothing. No message will go through to anyone. As the old saying goes, it will just drift in CyberSpace for all eternity. Unfortunatly, just like the old days, there will also be no prompt on the phone either. You just have to cross your fingers and hope for the best.
