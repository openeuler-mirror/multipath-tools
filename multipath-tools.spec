Name:    multipath-tools
Version: 0.8.4
Release: 4
Summary: Tools to manage multipath devices with the device-mapper
License: GPLv2-or-later and LGPLv2+
URL:     http://christophe.varoqui.free.fr/

# curl "https://git.opensvc.com/gitweb.cgi?p=multipath-tools/.git;a=snapshot;h=d4915917655b3d205aa0e339ca13080ed8182d0d;sf=tgz" -o multipath-tools-d491591.tgz
Source0: multipath-tools-d491591.tgz
Source1: multipath.conf
Patch1: 0001-change-order-of-multipath.rules.patch
Patch2: 0002-libmpathpersist-depend-on-libmultipath.patch
Patch3: 0003-libmultipath-assign-variable-to-make-gcc-happy.patch
Patch4: 0004-RH-add-mpathconf.patch
Patch5: 0005-RH-Remove-the-property-blacklist-exception-builtin.patch
Patch6: 0006-fix-syntax-error.patch
Patch7: 0007-fix-multipathd-resize-when-not-all-paths-size-are-equal.patch
Patch8: 0008-multipathd-disable-queueing-for-recreated-map-in-uev.patch
Patch9: 0009-avoid-handling-paths-repeatedly-in-coalesce-paths.patch
Patch10: 0010-fix-bugs-backported-from-next-branch.patch
Patch11: 0011-bugfix-fix-change-reservation-key-to-uint8-for-memcmp.patch
Patch12: 0012-bugfix-ignore-for-clear-mismatch-key.patch
Patch13: 0013-bugfix-flush-and-sync-before-reboot.patch
Patch14: 0014-bugfix-RH-remove-local-disk-from-pathvec.patch
Patch15: 0015-bugfix-lun-expansion-failure-when-there-is-offline-path.patch
Patch16: 0016-bugfix-change-log-level-to-info-if-alua-is-not-support-by-s.patch
Patch17: 0017-bugfix-clear-mpp-path-reference-when-path-is-freed-otherwis.patch
Patch18: 0018-bugfix-libmultipath-fix-memory-leak-in-disassemble_map.patch
Patch19: 0019-fix-find-multipath-failure.patch
Patch20: 0020-change-kpartx-file-and-default-bindir.patch
Patch21: 0021-master-libmultipath-fix-use-after-free-when-iscsi-lo.patch
Patch22: 0022-libmultipath-warn-if-freeing-path-that-holds-mpp-hwe.patch
Patch23: 0023-libmultipath-warn-about-NULL-value-of-mpp-hwe.patch
Patch24: 0024-libmultipath-fix-mpp-hwe-handling-in-sync_paths.patch
Patch25: 0025-fix-boolean-value-with-json-c-0.14.patch

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
%autosetup -Sgit -n multipath-tools-d491591
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
* Tue Oct 27 2020 lixiaokeng<lixiaokeng@huawei.com> - 0.8.4-4
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:remove patch that has be fixed in 0.8.4

* Fri Sep 25 2020 lixiaokeng<lixiaokeng@huawei.com> - 0.8.4-3
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix boolean value for TRUE deleted

* Tue Sep 01 2020 lixiaokeng<lixiaokeng@huawei.com> - 0.8.4-2
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix use after free in select_pgfailback

* Tue Aug 26 2020 lixiaokeng<lixiaokeng@huawei.com> - 0.8.4-1
- upgrade to 0.8.4

* Tue Aug 18 2020 smileknife<jackshan2010@aliyun.com> - 0.7.7-18
- update release for rebuilding

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
