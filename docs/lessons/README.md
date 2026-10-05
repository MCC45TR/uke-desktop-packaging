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

## UKE-DESKTOP-005 — inspect payloads as well as dependency names

- Date: 2026-10-05.
- Environment: isolated Rawhide AArch64 dependency transaction and official RPM archive audit.
- Evidence: the complete Plasma selection resolved six Python packages; five
  native source families declared the immediate interpreter dependencies.
  An independent 600-RPM file-list audit found two additional Python scripts
  in Dolphin, despite their missing interpreter Requires.
- Consequence: six exact-pinned official source variants remove optional host
  utilities/bindings or replace required migrations with native C++ helpers.
  The core selection refuses the Python ABI and Plasma requires explicit native
  variant capabilities. Neither RPM metadata nor successful compilation alone
  is sufficient target evidence.
- Host evidence: calendar and Dolphin C++ fixtures passed transformations,
  preservation/idempotence and unsafe-input checks. These are host fixtures,
  separate from COPR binary builds and target transactions.
- Correction: inherited Plasma source metadata used a KF6 minimum-version macro
  unavailable in some source factories. Its inspected 6.7.91 value is explicit.
  An inherited nonchronological Fedora changelog is retained in the original
  archive, while the generated candidate records its own change.
- Uncertainty: native rebuilds and the complete corrected runtime transaction
  remain required. Optional Python accessibility/account consumers and Wacom
  helper users are deliberately outside this native-runtime selection.
- Next validation: audit every signed native binary payload and re-run complete
  fresh-install/upgrade/removal with the hard no-Python dependency gate.
- Additional source-factory gate: the minimal compiler image deliberately lacks
  KF6 RPM macros. The shared source factory now installs official kf6-rpm-macros
  before generating KDE source RPMs; this also resolves Dolphin's inherited
  versioned BuildRequires before mock's binary dependency solver runs.

## UKE-DESKTOP-006 — declare the native compiler in a minimal build root

- Date: 2026-10-05.
- Environment: native Rawhide AArch64 COPR binary job 11075173.
- Evidence: source collection passed, then Meson reported `gcc --version` could
  not execute because the compiler was absent. The inherited libwacom spec did
  not declare GCC; the project's minimal worker does not imply Fedora's full
  default build group.
- Consequence: the libwacom variant now explicitly requires GCC and increments
  its candidate release to `1.uke2`. A source/RPM collection result cannot prove
  native dependency closure or compilation.
- Next validation: replacement native compilation and signed runtime audit.
