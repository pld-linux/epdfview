Summary:	A lightweight PDF viewer for GNOME
Summary(pl.UTF-8):	Lekka przeglądarka PDF-ów dla GNOME
Name:		epdfview
Version:	0.1.8
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://trac.emma-soft.com/epdfview/chrome/site/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	e50285b01612169b2594fea375f53ae4
Patch0:		%{name}-locale.patch
Patch1:		%{name}-desktop.patch
URL:		http://trac.emma-soft.com/epdfview/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cups-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	intltool
BuildRequires:	pkgconfig
BuildRequires:	poppler-glib-devel > 0.5.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ePDFView is a free lightweight PDF document viewer using Poppler and
GTK+ libraries.

The aim of ePDFView is to make a simple PDF document viewer, in the
lines of Evince but without using the GNOME libraries.

%description -l pl.UTF-8
ePDFView to darmowa, lekka przeglądarka dokumentów PDF, używająca
bibliotek Poppler i GTK+.

Celem ePDFView jest zrobienie prostej przeglądarki dokumentów PDF w
stylu Evince, ale bez wykorzystywania bibliotek GNOME.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

# locales quick fix
%{__mv} po/pt_PT.gmo po/pt.gmo
%{__mv} po/pt_PT.po po/pt.po
%{__mv} po/he_IL.gmo po/he.gmo
%{__mv} po/he_IL.po po/he.po
%{__mv} po/nl_NL.gmo po/nl.gmo
%{__mv} po/nl_NL.po po/nl.po

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS
%attr(755,root,root) %{_bindir}/epdfview
%{_desktopdir}/epdfview.desktop
%{_datadir}/epdfview
%{_mandir}/man1/epdfview.1*
