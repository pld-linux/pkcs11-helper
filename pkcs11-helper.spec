Summary:	Helper library for the use with smart cards and the PKCS#11 API
Summary(pl.UTF-8):	Biblioteka pomocnicza do używania z kartami procesorowymi i API PKCS#11
Name:		pkcs11-helper
Version:	1.09
Release:	1
License:	GPL v2 or BSD
Group:		Libraries
Source0:	http://www.opensc-project.org/files/pkcs11-helper/%{name}-%{version}.tar.bz2
# Source0-md5:	88ca59143f1b1d36283cab406f33a3fa
URL:		http://www.opensc-project.org/
# for macros
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	gnutls-devel >= 1.4
BuildRequires:	nss-devel >= 3.11
BuildRequires:	openssl-devel >= 0.9.7a
BuildRequires:	pkgconfig
Requires:	openssl >= 0.9.7a
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx

%description
pkcs11-helper provides a simple API to access PKCS#11 tokens.

%description -l pl.UTF-8
pkcs11-helper udostępnia proste API do dostępu do tokenów PKCS#11.

%package devel
Summary:	Header files for pkcs11-helper library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki pkcs11-helper
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for pkcs11-helper library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki pkcs11-helper.

%package static
Summary:	Static pkcs11-helper library
Summary(pl.UTF-8):	Statyczna biblioteka pkcs11-helper
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static pkcs11-helper library.

%description static -l pl.UTF-8
Statyczna biblioteka pkcs11-helper.

%prep
%setup -q

%build
%configure \
	--enable-doc

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING COPYING.BSD ChangeLog README THANKS
%attr(755,root,root) %{_libdir}/libpkcs11-helper.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpkcs11-helper.so.1
%{_mandir}/man8/pkcs11-helper-1.8*

%files devel
%defattr(644,root,root,755)
%doc doc/api/api.out/html/*
%attr(755,root,root) %{_libdir}/libpkcs11-helper.so
%{_libdir}/libpkcs11-helper.la
%{_includedir}/pkcs11-helper-1.0
%{_pkgconfigdir}/libpkcs11-helper-1.pc
%{_aclocaldir}/pkcs11-helper-1.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libpkcs11-helper.a
