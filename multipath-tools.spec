Name:    multipath-tools
Version: 0.7.7
Release: 15
Summary: Tools to manage multipath devices with the device-mapper
License: GPLv2-or-later and LGPLv2+
URL:     http://christophe.varoqui.free.fr/

# curl "https://git.opensvc.com/?p=multipath-tools/.git;a=snapshot;h=ef6d98b;sf=tgz" -o multipath-tools-ef6d98b.tgz
Source0: multipath-tools-ef6d98b.tgz
Source1: multipath.conf
Patch0000: 0000-libmultipath-remove-last-of-rbd-code.patch
Patch0001: 0001-libmultipath-fix-detect-alua-corner-case.patch
Patch0002: 0002-multipath-fix-setting-conf-version.patch
Patch0003: 0003-mpathpersist-add-param-alltgpt-option.patch
Patch0004: 0004-libmutipath-remove-unused-IDE-bus-type.patch
Patch0005: 0005-multipathd-add-new-protocol-path-wildcard.patch
Patch0006: 0006-libmultipath-add-protocol-blacklist-option.patch
Patch0007: 0007-libmultipath-remove-_filter_-blacklist-functions.patch
Patch0008: 0008-multipath-tests-change-to-work-with-old-make-version.patch
Patch0009: 0009-multipath-tests-add-blacklist-tests.patch
Patch0010: 0010-mpathpersist-add-missing-param-rk-usage-info.patch
Patch0011: 0011-change-order-of-multipath.rules.patch
Patch0012: 0012-RH-Remove-the-property-blacklist-exception-builtin.patch
Patch0013: 0013-RH-add-mpathconf.patch

Patch9000: 9000-fix-segfault-when-mount-or-umount-VIMS-with-reservation-conflict.patch
Patch9001: 9001-fix-multipathd-resize-when-not-all-paths-size-are-equal.patch
Patch9002: 9002-multipathd-disable-queueing-for-recreated-map-in-uev.patch
Patch9003: 9003-avoid-handling-paths-repeatedly-in-coalesce-paths.patch
Patch9004: 9004-fix-bugs-backported-from-next-branch.patch
Patch9005: 9005-bugfix-fix-change-reservation-key-to-uint8-for-memcmp.patch
Patch9006: 9006-bugfix-ignore-for-clear-mismatch-key.patch
Patch9007: 9007-bugfix-flush-and-sync-before-reboot.patch
Patch9008: 9008-bugfix-RH-remove-local-disk-from-pathvec.patch
Patch9009: 9009-bugfix-lun-expansion-failure-when-there-is-offline-path.patch
Patch9010: 9010-bugfix-some-memory-leaks-issues-in-libmpathpersist.patch

Patch6000: 6000-libmultipath-fix-set_int-error-path.patch
Patch6001: 6001-libmultipath-free-allocated-value-in-set_int.patch
Patch6002: 6002-libmultipath-fix-memory-issue-in-path_latency-prio.patch
Patch6003: 6003-libmultipath-fix-null-dereference-int-alloc_path_group.patch
Patch6004: 6004-multipath-fix-max-array-size-in-print_cmd_valid.patch
Patch6005: 6005-multipathd-minor-fixes.patch
Patch6006: 6006-multipathd-fix-memory-leak-on-error-in-configure.patch
Patch6007: 6007-multipathd-check-for-NULL-udevice-in-cli_add_path.patch
Patch6008: 6008-kpartx-fix-apparent-out-of-bounds-access.patch
Patch6009: 6009-libmultipath-fix-apparent-overflow.patch
Patch6010: 6010-libmultipath-fix-int-overflow-in-sysfs_set_scsi_tmo.patch
Patch6011: 6011-libmultipath-fix-enum-misuse-for-find_multipaths.patch
Patch6012: 6012-libmultipath-fix-possible-NULL-dereference.patch
Patch6014: 6014-fix-syntax-error.patch

Patch9011: 9011-bugfix-change-log-level-to-info-if-alua-is-not-support-by-s.patch
Patch9012: 9012-bugfix-clear-mpp-path-reference-when-path-is-freed-otherwis.patch
Patch9013: 9013-bugfix-libmultipath-fix-memory-leaks-from-scandir-use.patch
Patch9014: 9014-bugfix-libmultipath-fix-memory-leak-in-disassemble_map.patch
Patch6013: 6013-multipathd-fix-mpp-hwe-handling-when-paths-are-freed.patch
Patch9015: 9015-bugfix-check-close-return-value.patch
Patch9016: 9016-fix-find-multipath-failure.patch
Patch9017: 9017-change-kpartx-file-and-default-bindir.patch

Patch6020: 6020-multipathd-ignore-failed-wwid-recheck.patch
Patch6021: 6021-libmultipath-group_by_prio-fix-signedness-bug.patch
Patch6022: 6022-multipathd-handle-NULL-return-from-genhelp_handler.patch
Patch6023: 6023-libmultipath-fix-parsing-of-VPD-83-type-1-T10-vendor.patch
Patch6024: 6024-libmultipath-Fix-buffer-overflow-in-parse_vpd_pg80.patch
Patch6025: 6025-libmultipath-fix-another-WWID-overflow-in-parse_vpd_.patch
Patch6026: 6026-libmultipath-fix-possible-WWID-overflow-in-parse_vpd.patch
Patch6027: 6027-libmultipath-fix-parsing-of-SCSI-name-string-iqn-for.patch
Patch6028: 6028-libmultipath-fix-double-free-in-pgpolicyfn-error-pat.patch


BuildRequires:    gcc, libaio-devel, userspace-rcu-devel, device-mapper-devel >= 1.02.89
BuildRequires:    libselinux-devel, libsepol-devel, readline-devel, ncurses-devel, git
BuildRequires:    systemd-units, systemd-devel, json-c-devel, perl-interpreter, pkgconfig
Requires:         userspace-rcu, json-c, device-mapper >= 1.02.96
Requires(post):   systemd-units
Requires(preun):  systemd-units
Requires(postun): systemd-units
Conflicts:        mdadm < 4.1-rc2.0.2
Conflicts:        udisks2 < 2.8.0-2
Provides:         device-mapper-multipath
Obsoletes:        device-mapper-multipath
Provides:         device-mapper-multipath-libs
Obsoletes:        device-mapper-multipath-libs
Provides:         kpartx
Obsoletes:        kpartx
Provides:         libdmmp
Obsoletes:        libdmmp

%description
This package provides the multipath tool and the multipathd daemon
to manage dm-multipath devices. multipath can detect and set up
multipath maps. multipathd sets up multipath maps automatically,
monitors path devices for failure, removal, or addition, and applies
the necessary changes to the multipath maps to ensure continuous
availability of the map devices.

%package devel
Summary: Development libraries for %{name}
Requires:      %{name} = %{version}-%{release}
Obsoletes:     %{name}-libs < %{version}-%{release}
Provides:      libdmmp-devel
Obsoletes:     libdmmp-devel
Provides:      device-mapper-multipath-devel
Obsoletes:     device-mapper-multipath-devel
Requires:      pkgconfig
Obsoletes:     libdmmp

%description devel
This package contains the development libraries for %{name}
that are %{name}'s libbmpathpersist and libmpathcmd libraries.

%package help
Summary:   Including man files for multipath-tools.
Requires:  man
Provides:  device-mapper-multipath-help
Obsoletes: device-mapper-multipath-help
%description    help
This contains man files for the using of multipath-tools.

%prep
%autosetup -Sgit -n multipath-tools-ef6d98b
cp %{SOURCE1} .

%build
%make_build LIB=%{_lib}

%install
make install \
    DESTDIR=%{buildroot} \
    bindir=/usr/sbin \
    syslibdir=/usr/%{_lib} \
    usrlibdir=/usr/%{_lib} \
    libdir=/usr/%{_lib}/multipath \
    rcdir=%{_initrddir} \
    unitdir=%{_unitdir} \
    includedir=%{_includedir} \
    pkgconfdir=/usr/%{_lib}/pkgconfig

install -d %{buildroot}/etc/multipath
rm -rf %{buildroot}/%{_initrddir}

%post
/sbin/ldconfig
%systemd_post multipathd.service

%preun
%systemd_preun multipathd.service

%postun
/sbin/ldconfig
if [ $1 -ge 1 ] ; then
    /sbin/multipathd forcequeueing daemon > /dev/null 2>&1 || :
fi
%systemd_postun_with_restart multipathd.service

%triggerun -- %{name} < 0.4.9-37
/bin/systemctl --quiet is-enabled multipathd.service >/dev/null 2>&1 && /bin/systemctl reenable multipathd.service ||:


%files
%doc README README.alua multipath.conf
%license LICENSES/GPL-2.0 LICENSES/LGPL-2.0 LICENSES/GPL-3.0
%{_unitdir}/*
        /usr/sbin/*
        /usr/%{_lib}/libmultipath.so
        /usr/%{_lib}/libmultipath.so.*
        /usr/%{_lib}/libmpathpersist.so.*
        /usr/%{_lib}/libmpathcmd.so.*
        /usr/%{_lib}/libdmmp.so.*
%dir    /etc/multipath
%dir    /usr/%{_lib}/multipath
        /usr/%{_lib}/multipath/*
        /usr/lib/udev/kpartx_id
%config /usr/lib/udev/rules.d/*

%files devel
%doc README
        %{_includedir}/*.h
%dir    %{_includedir}/libdmmp
        %{_includedir}/libdmmp/*
        /usr/%{_lib}/libmpathpersist.so
        /usr/%{_lib}/libmpathcmd.so
        /usr/%{_lib}/libdmmp.so
        /usr/%{_lib}/pkgconfig/libdmmp.pc

%files help
%{_mandir}/man3/*
%{_mandir}/man5/*
%{_mandir}/man8/*


%changelog
* Thu Jan 16 2020 openEuler Buildteam <buildteam@openeuler.org> - 0.7.7-15
- Type:enhancement
- ID:NA
- SUG:NA
- DESC: add the script mpathconf

* Fri Jan 10 2020 wangjufeng <wangjufeng@huawei.com> - 0.7.7-14
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:rename the package

* Fri Jan 10 2020 wangjufeng <wangjufeng@huawei.com> - 0.7.7-13
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:rewrap the package

* Fri Jan 3 2020 openEuler Buildteam <buildteam@openeuler.org> - 0.7.7-12
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix find multipath failure

* Tue Dec 31 2019 openEuler Buildteam <buildteam@openeuler.org> - 0.7.7-11
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:package rewrap

* Thu Dec 25 2019 openEuler Buildteam <buildteam@openeuler.org> - 0.7.7-10
- reupload patches

* Wed Dec 25 2019 openEuler Buildteam <buildteam@openeuler.org> - 0.7.7-9
- revert patches

* Tue Dec 24 2019 openEuler Buildteam <buildteam@openeuler.org> - 0.7.7-8
- bugfix

* Fri Nov 01 2019 wangjufeng<wangjufeng@huawei.com> - 0.7.7-7
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix syntax error

* Tue Sep 17 2019 zoujing<zoujing13@huawei.com> - 0.7.7-6
- Package init
