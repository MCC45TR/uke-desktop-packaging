# Uke desktop package sources

This repository owns decoration, theme and native runtime sources for Fedora Rawhide AArch64:

- `material-decoration`: optional upstream C++20/Qt6 KWin decoration and KCM.
  Source is pinned to the published upstream release in
  `manifests/material-decoration.json`, with archive SHA-256 verification both
  before SRPM generation and during RPM preparation. Its GPL/LGPL source license
  is retained. The small KPlugin metadata correction is attributed to the Nabu
  reference specification at `152980fa9a4fd2d71a2825efe10411c5a8a74da7`.
- `plymouth-uke`: an original MIT-licensed optional text theme using the current
  renderer dimensions. It does not assume a Uke panel DPI, enable itself,
  regenerate an initramfs, select a boot entry or copy Nabu geometry/artwork.

`make validate` checks the source contracts. `make srpm PACKAGE=NAME` creates
that family's complete SRPM. The repository-root `.copr/Makefile`, invoked from each package subdirectory, exports only its
source RPM; source work stays outside COPR's unprivileged collection directory.
COPR builds binaries without network access. Main-branch push hooks rebuild both
families. The Material stable tracker fetches published upstream releases, pins
commit/archive identities and requests a new native build; failed compilation
does not establish package acceptance. New findings and native transaction
results have distinct `docs/lessons/` and `reports/` records.

Fedora's shared `powerdevil` and `plymouth` engines are dependencies. No measured
Uke issue currently justifies replacing them with Nabu-patched generic RPMs.
The source catalog retains those reference families for later Uke-specific work.
No Python enters target payloads or the accepted dependency closure. Official
Fedora RPM policy and upstream build dependencies may use host tools only.
Neither decoration compilation nor theme installation proves Uke graphics or boot.

[Uke package hub](https://github.com/MCC45TR/uke-linux/blob/main/docs/PACKAGE-HUB.md)
· [Development COPR](https://copr.fedorainfracloud.org/coprs/mcc45tr/uke-linux-test/)

Seven [native runtime source variants](docs/NATIVE-RUNTIME.md) are also owned here:
`at-spi2-core`, `gstreamer1`, `libaccounts-glib`, `libwacom`, `plasma-workspace`
and `dolphin`, plus `libstdcxx-uke-runtime` producing native `libstdc++`.
The reviewed complete Fedora sources retain their native APIs;
optional Python bindings/host utilities are excluded and required configuration
migrations have C++ equivalents. Their target acceptance remains separate from
source registration. A GitHub Actions workflow explicitly requests all seven
builds after shared adapter/manifest changes, because a package-subdirectory
push hook alone may not observe repository-root source changes. The hook value
is held only in an encrypted repository secret. Healthy COPR jobs are preserved.
These sources use reviewed Fedora pins; automatic builds do not silently admit
arbitrary new Fedora source recipes or assert physical hardware support.

The [package testing procedure](docs/PACKAGE-TESTING.md) requires both the
selected RPM closure and the complete installed root. The original 603-input
transaction passed its input audit and lifecycle fixtures, but its base image
contained optional Python GDB helpers in libstdc++; complete-root acceptance
was rejected. The seventh native source addresses that independent base-image
gate. Current accepted and failed results are recorded by the builder.
