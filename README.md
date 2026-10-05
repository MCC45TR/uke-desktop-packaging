# Uke desktop package sources

This repository owns two real source families for Fedora Rawhide AArch64:

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
that family's complete SRPM. Each `packaging/NAME/.copr/Makefile` exports only its
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
