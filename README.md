# Custom Fedora

This is a opinionate fedora distribution with the help of image builder.

## Image Builder

Image builder is a command line tool, which is part of the tools in [osbuild](https://osbuild.org).

List all types

    image-builder list --filter distro:fedora-43

## Preinstall

The blueprint file is generated from the template and predefined configuration files in 'config' directory for lots of packages.

Generate the blueprint file by running

    python3 preinstall.py

## Customization

The image-builder will generate a minimal-installer

    sudo image-builder build image-installer --distro fedora-43 --blueprint custom_fedora.toml


## Postinstall

After successfully install the OS, change the default shell to nushell by using the command

    sudo chsh -s /usr/bin/nu <USER>

where <USER> is the custom user name.
