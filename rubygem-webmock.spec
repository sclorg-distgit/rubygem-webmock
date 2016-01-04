%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from webmock-1.7.6.gem by gem2rpm -*- rpm-spec -*-
%global gem_name webmock

Summary: Library for stubbing HTTP requests in Ruby
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.17.1
Release: 3%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/bblimke/webmock
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(addressable) >= 2.2.7
Requires: %{?scl_prefix}rubygem(crack) >= 0.3.2
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ror}rubygem(rspec)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
WebMock allows stubbing HTTP requests and setting expectations on HTTP
requests.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - << \EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

pushd %{buildroot}%{gem_instdir}
sed -i s-/usr/bin/env\ rake-/usr/bin/rake- Rakefile
rm  .travis.yml .rspec-tm .gitignore .gemtest
popd

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/minitest
%doc %{gem_instdir}/LICENSE
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/test
%{gem_instdir}/spec

%changelog
* Thu Feb 19 2015 Josef Stribny <jstribny@redhat.com> - 1.17.1-3
- Add SCL macros

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 21 2014 Mo Morsi <mmorsi@redhat.com> - 1.17.1-1
- Update to version 1.17.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 11 2013 Vít Ondruch <vondruch@redhat.com> - 1.9.0-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 13 2012 Mo Morsi <mmorsi@redhat.com> - 1.9.0-1
- Updated to webmock 1.9.0

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 02 2012 Vít Ondruch <vondruch@redhat.com> - 1.8.7-1
- Updated to webmock 1.8.7.

* Mon Feb 13 2012 Mo Morsi <mmorsi@redhat.com> - 1.7.10-1
- Update to latest upstream release
- Build against ruby 1.9

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 03 2011 Mo Morsi <mmorsi@redhat.com> - 1.7.6-2
- Update to conform to guidelines

* Wed Sep 28 2011 Mo Morsi <mmorsi@redhat.com> - 1.7.6-1
- Initial package
