# Rawhide AArch64 desktop package acceptance

Package acceptance uses isolated AArch64 userspace under QEMU, with network
disabled during installation and lifecycle tests. It does not start Plasma,
boot the Uke kernel, activate Plymouth or execute a recovery installer.

## Required inputs

Use the exact native source jobs, package hashes and base-image identity in the
[builder acceptance report](https://github.com/MCC45TR/uke-fedora-builder/blob/main/reports/DESKTOP-RAWHIDE-2026-10-05.json)
and its [603-package runtime lock](https://github.com/MCC45TR/uke-fedora-builder/blob/main/manifests/DESKTOP-RUNTIME-LOCK-2026-10-05.json).
The public lock records NEVRA, architecture, license and SHA-256 for every
selected transaction input. Local caches and installed-root exports are test
artifacts, not distributed tablet images.

The observed COPR signing fingerprint is
`DAFC3C5A881FB49C7167EE2D6F772E3D487BD13E`; the official Fedora 46 primary key
fingerprint is `D924B10D3E810DABDD8B56B596E7E91491211FCE`. Verify each signature
against the appropriate isolated key database. Source archive hashes identify
the reviewed official Fedora inputs; they are not claims of Koji SRPM signatures.

## Acceptance sequence

1. Build each complete source family in native COPR. Inspect all binary
   subpackages for Python files, scripts, interpreter dependencies and ELF
   dependencies. Inspect admitted runtime packages for private content.
2. Resolve `kde-plasma-uke-meta`, `material-decoration`, `plymouth-uke` and
   `uke-orangefox-recovery` with weak dependencies disabled. Use DNF5's
   `--store` to retain the exact transaction before installation. Require the
   expected nonempty package count, signatures and complete hashes.
3. Extract every selected RPM on the host and scan its complete payload with
   `check-target-payload.sh` from the workspace. GNU readelf is mandatory;
   missing tools and unreadable ELF fail the gate. Metadata checks alone miss
   undeclared interpreter scripts.
4. Replay the stored signed transaction in a clean pinned AArch64 container
   with network disabled and local RPM signature verification enabled. Require
   core and desktop meta release 2, all six `senemos-native-runtime(NAME)`
   capabilities, no Python package names and successful `rpm -V` on admitted
   packages and native runtime binaries.
5. Execute the real AArch64 calendar migration and both Dolphin migrations on
   fixture configuration files. Host fixtures additionally check permissions,
   idempotence, unknown entries, malformed XML and symlink rejection.
6. Export the installed root and scan all installed `usr/` and `etc/` on the
   host, including the base image. Check the three replacement helpers' ELF
   architecture and dynamic dependencies. Inspecting only newly installed RPMs
   does not qualify the complete root.
7. Install the actual signed release-1 core and desktop metas as an upgrade
   fixture, require their old release, then upgrade all three to release 2.
   Repeat capability, package verification and no-Python checks.
8. Remove the admitted meta, kernel, recovery, decoration and theme packages.
   Require absent package records, profile/plugin/theme/recovery files and
   empty or absent kernel module payload/indexes. Keep each gate's exit status
   and distinguish failed trials from accepted corrections.

Never bypass the core's Python conflicts, use `--nodeps`, skip broken
dependencies or promote an empty extraction/query result. A changed dependency
graph requires a new complete acceptance record.

## Runtime scope and remaining validation

The native variants preserve upstream C/C++ APIs and normal UI translations.
Optional Python GI overrides, Wacom administration helpers, documentation
scanners and GDB conveniences are excluded. Required configuration migrations
have native C++ implementations. Optional Plasma HTML documentation is outside
the admitted tablet selection; the lean Dolphin runtime omits offline HTML
manuals while retaining complete upstream source and licensing.

This package gate establishes dependency and file lifecycle behavior. Plasma
startup, decoration rendering, accessibility/account consumers, audio/media,
input, suspend, display, firmware-specific boot and physical Uke support require
separate validation. Host-only upstream build tools and their exact reviewed
pins are documented in [native runtime rules](NATIVE-RUNTIME.md).
