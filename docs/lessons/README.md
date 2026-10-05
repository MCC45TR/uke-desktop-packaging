# Engineering lessons

| ID | Date | Finding | Validation |
|---|---|---|---|
| UKE-INITIAL-001 | 2026-10-04 | Initial source/packaging scope established from the Nabu COPR inventory | Manifest checks only; package and physical validation open |

## UKE-INITIAL-001

- Date: 2026-10-04.
- Environment: project-owned Git repository; no tablet execution.
- Evidence: component manifest, source policy and acceptance roadmap.
- Finding: Nabu package roles can organize Uke work; their hardware assumptions
  cannot establish Uke behavior.
- Consequence: package admission requires Uke sources and isolated payload tests.
- Uncertainty: no functional package exists at this initial scaffold stage.
- Next validation: complete the manifest's component-specific gates.

| UKE-PACKAGE-002 | 2026-10-05 | Implemented real source/RPM rules from independently scoped Uke inputs | Source validation; target and native results recorded separately |

## UKE-PACKAGE-002

- Date: 2026-10-05.
- Environment: official Fedora host source tools; no tablet execution.
- Evidence: package specs, Make source factory and explicit Uke readiness records.
- Finding: the Nabu package roles are reusable, while firmware, panel, services
  and boot integration require their own Uke evidence. Shared Fedora software
  remains upstream; package data and dependency selections have explicit scope.
- Consequence: only real source families enter automatic COPR compilation.
- Uncertainty: source-generation checks do not establish target closure, native
  binary acceptance, graphical rendering or physical operation.
- Next validation: collect native COPR and signed target transaction results in
  distinct reports, then separately qualify hardware.

## UKE-DESKTOP-003 — COPR locates its source factory at repository root

- Date: 2026-10-05.
- Environment: COPR source-generation mock with two configured subdirectories.
- Evidence: failed source jobs 11075047/11075048 and repeated 11075049/11075050;
  their native source command selected the repository-root `.copr/Makefile` while
  setting its working directory to `packaging/PACKAGE`.
- Finding: a `.copr/Makefile` placed inside each package directory was not selected.
  The ordinary source generation passed locally, but the remote factory stopped
  before an SRPM was collected.
- Consequence: one root factory now validates the working-directory package name,
  dispatches to the ordinary root Makefile, and exports only its mode-0644 SRPM.
  The ineffective nested factory files were removed.
- Uncertainty: the corrected factory still requires its own remote collection
  and binary build results; local source success is not substituted for them.
- Next validation: collect replacement source jobs and audit signed target packages.

## UKE-DESKTOP-004 — current KF6 exports require explicit Qt QML imports

- Date: 2026-10-05.
- Environment: published upstream stable source and native Rawhide AArch64 COPR.
- Evidence: binary build 11075055 stopped in CMake generation because
  `KF6::I18nQml` referenced the undefined `Qt6::QmlIntegration` target.
- Finding: the stable project's Qt Widgets/DBus declaration did not create the
  QML targets exported by the current KF6 I18n toolchain.
- Consequence: an attributed small CMake patch explicitly imports Qt Qml and
  QmlIntegration; the spec adds official qt6-qtdeclarative-devel and increments
  its release. The SRPM retains the patch as an inspectable separate source.
- Uncertainty: successful source preparation alone does not establish the
  corrected C++ binary build, plugin load, dependency closure or rendering.
- Next validation: build the corrected native RPM, inspect its ELF/plugins and
  validate its signed target package transaction.
- Correction evidence: the first local patch trial had an incorrect unified-diff
  hunk count and was rejected by RPM preparation. Correcting the count allowed
  zero-fuzz application. An EOF blank context line then failed publication's
  whitespace check; narrowing the context removed it. Original failed logs and
  the corrected preparation are retained separately.
