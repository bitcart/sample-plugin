# Bitcart Sample Plugin

This plugin serves as an example of how Bitcart plugins can extend various parts of the app.

When creating your own plugin, please don't copy-paste this template, instead use [Bitcart CLI](https://github.com/bitcart/bitcart-cli):

```bash
bitcart-cli plugin init directory
```

An interactive wizard will help you to create your first plugin, properly configuring the development environment too.

You can then use `bitcart-cli plugin validate directory` to ensure it's correct and `bitcart-cli plugin package directory` to create the plugin archive.

This repository's plugin validity is checked by our bitcart circleci orb, which in turn runs `bitcart-cli plugin validate`
