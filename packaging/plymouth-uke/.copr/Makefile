SHELL := /bin/bash
.SHELLFLAGS := -Eeuo pipefail -c
.ONESHELL:
.PHONY: srpm
srpm:
	dnf -y --setopt=install_weak_deps=False install make curl jq xz tar rpm-build coreutils
	$(MAKE) -C ../.. srpm PACKAGE=plymouth-uke outdir="$(CURDIR)/build/copr-source"
	mkdir -p "$(outdir)"
	install -m644 build/copr-source/*.src.rpm "$(outdir)/"
