# Notify about order

## Overview

This solution contains a class called `Order`, a codebox that would send notification to slack with data passed
and trigger that connects data event - creation of new order - with running a codebox.

# How it works

Someone creates new order, for example with one of libraries or making a POST api call and then you get notified
on slack.

# Custom configuration

To use this solution with your slack account, configure your slack integration and 

in codebox config set:

- `'hook_url'`
- `'username'`
- and `'channel'`


