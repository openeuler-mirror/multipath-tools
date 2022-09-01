#needsrootforbuild
Name:    multipath-tools
Version: 0.8.7
Release: 3
Summary: Tools to manage multipath devices with the device-mapper
License: GPL-2.0-or-later and LGPL-2.0-only
URL:     http://christophe.varoqui.free.fr/

# curl https://github.com/opensvc/multipath-tools/archive/0.8.7.tar.gz -o multipath-tools-0.8.7.tgz
Source0: multipath-tools-0.8.7.tgz
Source1: multipath.conf
Patch1:  0001-change-order-of-multipath.rules.patch
Patch2:  0002-RH-add-mpathconf.patch
Patch3:  0003-RH-Remove-the-property-blacklist-exception-builtin.patch
Patch4:  0004-fix-syntax-error.patch
Patch5:  0005-fix-multipathd-resize-when-not-all-paths-size-are-eq.patch
Patch6:  0006-avoid-handling-paths-repeatedly-in-coalesce-paths.patch
Patch7:  0007-fix-lun-expansion-failure-when-there-is-offline-path.patch
Patch8:  0008-fix-bugs-backported-from-next-branch.patch
Patch9:  0009-fix-change-reservation-key-to-uint8-for-memcmp.patch
Patch10: 0010-bugfix-flush-and-sync-before-reboot.patch
Patch11: 0011-change-log-level-to-info-if-alua-is-not-support-by-s.patch
Patch12: 0012-device-mapper-multipath-fix-find-multipath-failure.patch
Patch13: 0013-kpartx-change-kpartx-file-and-default-bindir.patch
Patch14: 0014-remove-local-disk-from-pathvec.patch
Patch15: 0015-clear-mpp-path-reference-when-path-is-freed-otherwis.patch
Patch16: 0016-multipath-return-failure-on-an-invalid-remove-cmd.patch

BuildRequires:    multipath-tools, libcmocka, libcmocka-devel
BuildRequires:    gcc, libaio-devel, userspace-rcu-devel, device-mapper-devel >= 1.02.89
BuildRequires:    libselinux-devel, libsepol-devel, readline-devel, ncurses-devel, 
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
%autosetup -n multipath-tools-0.8.7 -p1
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

%check
make test

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
%doc README.md README.alua multipath.conf
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
	/usr/%{_lib}/libmpathvalid.so
	/usr/%{_lib}/libmpathvalid.so.*
%dir    /etc/multipath
%dir    /usr/%{_lib}/multipath
        /usr/%{_lib}/multipath/*
%config /usr/lib/udev/rules.d/62-multipath.rules
%config /usr/lib/udev/rules.d/11-dm-mpath.rules


%files devel
%doc README.md
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
%doc README.md
/usr/sbin/kpartx
/usr/lib/udev/kpartx_id
%config /usr/lib/udev/rules.d/11-dm-parts.rules
%config /usr/lib/udev/rules.d/66-kpartx.rules
%config /usr/lib/udev/rules.d/68-del-part-nodes.rules


%changelog
* Wed Aug 31 2022 xueyamao<xueyamao@kylinos.cn> - 0.8.7-3
- fix multipath return failure on an invalid remove command

* Tue Mar 8 2022 lixiaokeng<lixiaokeng@huawei.com> - 0.8.7-2
- don't create nvme multipath device when enable remove_local_path

* Tue Nov 23 2021 lixiaokeng<lixiaokeng@huawei.com> - 0.8.7-1
- upgrade to 0.8.7

* Fri Sep 24 2021 lixiaokeng<lixiaokeng@huawei.com> - 0.8.5-7
- Type:codeclean
- ID:NA
- SUG:NA
- DESC:use upstream patch instead huawei patch

* Thu Sep 23 2021 lixiaokeng<lixiaokeng@huawei.com> - 0.8.5-6
- Type:testcode
- ID:NA
- SUG:NA
- DESC:add needsrootforbuild for make test

* Thu Aug 12 2021 lixiaokeng<lixiaokeng@huawei.com> - 0.8.5-5
- Type:testcode
- ID:NA
- SUG:NA
- DESC:add make test

* Wed Aug 11 2021 lixiaokeng<lixiaokeng@huawei.com> - 0.8.5-4
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix compile error

* Fri Jul 30 2021 chenyanpanHW <chenyanpan@huawei.com> - 0.8.5-3
- DESC: delete -Sgit from %autosetup, and delete BuildRequires git

* Tue Jul 20 2021 lixiaokeng<lixiaokeng@huawei.com> - 0.8.5-2
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:add check remove_local_disk before transport in pathinfo

* Thu Jan 30 2020 lixiaokeng<lixiaokeng@huawei.com> - 0.8.5-1
- update to 0.8.5

* Fri Oct 16 2020 lixiaokeng<lixiaokeng@huawei.com> - 0.8.4-4
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:remove patch that has been fix in 0.8.4

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

* Thu Jul 16 2020 lixiaokeng <lixiaokeng@huawei.com> - 0.8.4-1
- update to 0.8.4-1

* Sun Jul 5 2020 Zhiqiang Liu <lzhq28@mail.ustc.edu.cn> - 0.7.7-20
- remove useless readme files.

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
