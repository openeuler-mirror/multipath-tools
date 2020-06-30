Name:    multipath-tools
Version: 0.7.7
Release: 19
Summary: Tools to manage multipath devices with the device-mapper
License: GPLv2-or-later and LGPLv2+
URL:     http://christophe.varoqui.free.fr/

# curl "https://git.opensvc.com/?p=multipath-tools/.git;a=snapshot;h=ef6d98b;sf=tgz" -o multipath-tools-ef6d98b.tgz
Source0: multipath-tools-ef6d98b.tgz
Source1: multipath.conf
Patch0: 0000-libmultipath-remove-last-of-rbd-code.patch
Patch1: 0001-libmultipath-fix-detect-alua-corner-case.patch
Patch2: 0002-multipath-fix-setting-conf-version.patch
Patch3: 0003-mpathpersist-add-param-alltgpt-option.patch
Patch4: 0004-libmutipath-remove-unused-IDE-bus-type.patch
Patch5: 0005-multipathd-add-new-protocol-path-wildcard.patch
Patch6: 0006-libmultipath-add-protocol-blacklist-option.patch
Patch7: 0007-libmultipath-remove-_filter_-blacklist-functions.patch
Patch8: 0008-multipath-tests-change-to-work-with-old-make-version.patch
Patch9: 0009-multipath-tests-add-blacklist-tests.patch
Patch10: 0010-mpathpersist-add-missing-param-rk-usage-info.patch
Patch11: 0011-change-order-of-multipath.rules.patch
Patch12: 0012-RH-Remove-the-property-blacklist-exception-builtin.patch
Patch13: 0013-RH-add-mpathconf.patch
Patch14: 0014-fix-segfault-when-mount-or-umount-VIMS-with-reservation-conflict.patch
Patch15: 0015-fix-multipathd-resize-when-not-all-paths-size-are-equal.patch
Patch16: 0016-multipathd-disable-queueing-for-recreated-map-in-uev.patch
Patch17: 0017-avoid-handling-paths-repeatedly-in-coalesce-paths.patch
Patch18: 0018-fix-bugs-backported-from-next-branch.patch
Patch19: 0019-bugfix-fix-change-reservation-key-to-uint8-for-memcmp.patch
Patch20: 0020-bugfix-ignore-for-clear-mismatch-key.patch
Patch21: 0021-bugfix-flush-and-sync-before-reboot.patch
Patch22: 0022-bugfix-RH-remove-local-disk-from-pathvec.patch
Patch23: 0023-bugfix-lun-expansion-failure-when-there-is-offline-path.patch
Patch24: 0024-bugfix-some-memory-leaks-issues-in-libmpathpersist.patch
Patch25: 0025-libmultipath-fix-set_int-error-path.patch
Patch26: 0026-libmultipath-free-allocated-value-in-set_int.patch
Patch27: 0027-libmultipath-fix-memory-issue-in-path_latency-prio.patch
Patch28: 0028-libmultipath-fix-null-dereference-int-alloc_path_group.patch
Patch29: 0029-multipath-fix-max-array-size-in-print_cmd_valid.patch
Patch30: 0030-multipathd-minor-fixes.patch
Patch31: 0031-multipathd-fix-memory-leak-on-error-in-configure.patch
Patch32: 0032-multipathd-check-for-NULL-udevice-in-cli_add_path.patch
Patch33: 0033-kpartx-fix-apparent-out-of-bounds-access.patch
Patch34: 0034-libmultipath-fix-apparent-overflow.patch
Patch35: 0035-libmultipath-fix-int-overflow-in-sysfs_set_scsi_tmo.patch
Patch36: 0036-libmultipath-fix-enum-misuse-for-find_multipaths.patch
Patch37: 0037-libmultipath-fix-possible-NULL-dereference.patch
Patch38: 0038-fix-syntax-error.patch
Patch39: 0039-bugfix-change-log-level-to-info-if-alua-is-not-support-by-s.patch
Patch40: 0040-bugfix-clear-mpp-path-reference-when-path-is-freed-otherwis.patch
Patch41: 0041-bugfix-libmultipath-fix-memory-leaks-from-scandir-use.patch
Patch42: 0042-bugfix-libmultipath-fix-memory-leak-in-disassemble_map.patch
Patch43: 0043-multipathd-fix-mpp-hwe-handling-when-paths-are-freed.patch
Patch44: 0044-bugfix-check-close-return-value.patch
Patch45: 0045-fix-find-multipath-failure.patch
Patch46: 0046-change-kpartx-file-and-default-bindir.patch
Patch47: 0047-multipathd-ignore-failed-wwid-recheck.patch
Patch48: 0048-libmultipath-group_by_prio-fix-signedness-bug.patch
Patch49: 0049-multipathd-handle-NULL-return-from-genhelp_handler.patch
Patch50: 0050-libmultipath-fix-parsing-of-VPD-83-type-1-T10-vendor.patch
Patch51: 0051-libmultipath-Fix-buffer-overflow-in-parse_vpd_pg80.patch
Patch52: 0052-libmultipath-fix-another-WWID-overflow-in-parse_vpd_.patch
Patch53: 0053-libmultipath-fix-possible-WWID-overflow-in-parse_vpd.patch
Patch54: 0054-libmultipath-fix-parsing-of-SCSI-name-string-iqn-for.patch
Patch55: 0055-libmultipath-fix-double-free-in-pgpolicyfn-error-pat.patch
Patch56: 0056-libmultipath-fix-files-read-from-config_dir.patch
Patch57: 0057-libmultipath-fix-sgio_get_vpd-looping.patch


BuildRequires:    gcc, libaio-devel, userspace-rcu-devel, device-mapper-devel >= 1.02.89
BuildRequires:    libselinux-devel, libsepol-devel, readline-devel, ncurses-devel, git
BuildRequires:    systemd-units, systemd-devel, json-c-devel, perl-interpreter, pkgconfig
Requires:         userspace-rcu, json-c, device-mapper >= 1.02.96
Requires:         kpartx = %{version}-%{release}
Requires(post):   systemd-units
Requires(preun):  systemd-units
Requires(postun): systemd-units
Conflicts:        mdadm < 4.1-rc2.0.2
Conflicts:        udisks2 < 2.8.0-2
Provides:         device-mapper-multipath
Obsoletes:        device-mapper-multipath
Provides:         device-mapper-multipath-libs
Obsoletes:        device-mapper-multipath-libs
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

%package -n kpartx
Summary: Create device maps from partition tables.

%description -n kpartx
Reads partition tables and create device maps over partitions segments detected.

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
        /usr/sbin/multipath
        /usr/sbin/multipathd
        /usr/sbin/mpathconf
        /usr/sbin/mpathpersist
        /usr/%{_lib}/libmultipath.so
        /usr/%{_lib}/libmultipath.so.*
        /usr/%{_lib}/libmpathpersist.so.*
        /usr/%{_lib}/libmpathcmd.so.*
        /usr/%{_lib}/libdmmp.so.*
%dir    /etc/multipath
%dir    /usr/%{_lib}/multipath
        /usr/%{_lib}/multipath/*
%config /usr/lib/udev/rules.d/62-multipath.rules
%config /usr/lib/udev/rules.d/11-dm-mpath.rules


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

%files -n kpartx
%license LICENSES/GPL-2.0
%doc README
/usr/sbin/kpartx
/usr/lib/udev/kpartx_id
%config /usr/lib/udev/rules.d/11-dm-parts.rules
%config /usr/lib/udev/rules.d/66-kpartx.rules
%config /usr/lib/udev/rules.d/68-del-part-nodes.rules


%changelog
* Tue Jun 30 2020 volcanodragon <linfeilong@huawei.com> - 0.7.7-19
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:rename patches

* Sat May 28 2020 ethan848 <mingfangsen@huawei.com> - 0.7.7-18
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:backport bugfix from community

* Thu Mar 19 2020 hy-euler <eulerstoragemt@huawei.com> - 0.7.7-17
- Type:enhancement
- ID:NA
- SUG:NA
- DESC: disabled multipathd.service

* Mon Mar 09 2020 wangjufeng <wangjufeng@huawei.com> - 0.7.7-16
- Type:enhancement
- ID:NA
- SUG:NA
- DESC: separate kpartx from the main package

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
