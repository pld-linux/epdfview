Summary:	A lightweight PDF viewer for GNOME
Summary(pl.UTF-8):	Lekka przeglądarka PDF-ów dla GNOME
Name:		epdfview
Version:	0.1.6
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://trac.emma-soft.com/epdfview/chrome/site/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	cce9edb41b4a8308e0ef0eea24b5a1ab
URL:		http://trac.emma-soft.com/epdfview/
BuildRequires:	cups-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2.6.0
BuildRequires:	intltool
BuildRequires:	poppler-glib-devel > 0.5.2
#Requires:
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

%build
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
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/epdfview.desktop
%{_datadir}/epdfview
