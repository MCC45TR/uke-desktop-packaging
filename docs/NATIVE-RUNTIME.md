# Python-free Fedora native runtime variants

The first complete Plasma dependency transaction pulled Python through optional
GI bindings, installed documentation utilities and configuration migrations.
An extracted official-RPM inventory also found Dolphin migration scripts even
though they did not declare a Python dependency. That transaction failed the
project's target acceptance gate; it is not an accepted tablet environment.

`manifests/native-runtime.json` pins six complete official Fedora Koji source
RPMs by exact NEVRA and SHA-256. Sources remain under this component's ignored
`referances/fedora-srpms/`. The section-aware host adapter derives inspectable
specifications in `build/`; native C/C++ applications and libraries are actually
rebuilt from their upstream sources in COPR. No binary RPM is repackaged.
The original source RPMs retain their complete source, licensing and history.
The generated candidate changelog contains the Senemos change; original history
remains available in the pinned source archive.

Optional Python GI overrides are excluded from at-spi2-core and libaccounts-glib.
GStreamer's two installed host documentation scanners are excluded while its
native plugin scanner is retained. Libwacom's Python database updater and stylus
viewer are excluded; native device listings and the upstream database remain.
Plasma's calendar migration and Dolphin's two XML migrations have attributed
C++/Qt replacements. These preserve permissions and use atomic replacement;
fixtures test idempotence and malformed/symlink rejection. No panel geometry,
Uke touchscreen identification or physical support is inferred from these
changes. The calendar migration preserves unknown plugin IDs. The Dolphin
shortcut migration avoids duplicating an existing action on repeated execution.

The generated source disables debug subpackages, restricts AArch64, checks every
installed file for Python paths/shebangs and provides an explicit
`senemos-native-runtime(PACKAGE)` capability. The Plasma Uke selection requires
these capabilities. `uke-core-meta` conflicts with the Python ABI/interpreter
packages, so an ordinary dependency solver fails safely rather than silently
introducing Python when Fedora later changes its dependency graph.

## Unavoidable upstream host tools

Official upstream Meson and GObject-introspection are Python host build tools.
Replacing their build engines or introspection compiler is not a practical
native-runtime packaging change. Fedora RPM's upstream build helpers also use
Python. They execute only in source/binary build workers, never as target tools.
The inspected Rawhide host pins are:

| Tool | Pin | Purpose |
|---|---|---|
| python3 | 3.15.0~rc2-1.fc46 | Upstream build engine/runtime |
| meson | 1.12.1-2.fc46 | Mandatory upstream native build descriptions |
| gobject-introspection-devel | 1.86.0-12.fc46 | Generate native typelib metadata |

These pins are added to the appropriate generated BuildRequires. A missing pin
stops a build and requires an explicit reviewed host-tool update. COPR logs
retain the actual worker dependency NEVRAs. All binary subpackage payloads and
the complete selected runtime must independently pass the no-Python audit.
The Qt/KF6 source factory resolves Plasma's inherited minimum Breeze version to
the inspected 6.7.91 literal because the factory may lack KF6 macro packages
before dependency parsing; the binary build still requires official KF6 macros.

The candidate remains experimental until signed RPM payload, dependency,
fresh-install, upgrade and removal tests pass. Compilation does not demonstrate
an accessible session, plugin rendering or Uke hardware behavior.
