---
title: "[macOS] Enable/Disable .DS_STORE"
date: 2021-10-24 08:00:00 -0400
categories: macOS DS_STORE
---

.DS_STORE Files means Desktop Services Store. This files are created and maintained by the Finder application on every folder. Similar to desktop.ini in MS Windows. Also, this file is hidden.

.DS_Store is a file that stores custom attributes of its containing folder, such as the position of icons or the choice of a background image.

```sh
#OFF
defaults write com.apple.desktopservices DSDontWriteNetworkStores true
```

```sh
#ON
defaults write com.apple.desktopservices DSDontWriteNetworkStores false
```