Summary:	Player for Commodore 64 music
Summary(pl.UTF-8):	Odtwarzacz muzyki z Commodore 64
Name:		sidplayfp
Version:	1.4.3
Release:	1
License:	GPL v2+
Group:		Applications/Sound
Source0:	http://downloads.sourceforge.net/sidplay-residfp/%{name}-%{version}.tar.gz
# Source0-md5:	be020b5927c80c4269273895400a8120
URL:		http://sourceforge.net/projects/sidplay-residfp/
BuildRequires:	alsa-lib-devel >= 1.0
BuildRequires:	libsidplayfp-devel >= 1.8.7
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel >= 1.0
Requires:	alsa-lib >= 1.0
Requires:	libsidplayfp >= 1.8.7
Requires:	pulseaudio-libs >= 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libsidplayfp (and its console frontend sidplayfp) is a fork of
sidplay2 born with the aim to improve the quality of emulating the
6581, 8580 chips and the surrounding C64 system in order to play SID
music better.

%description -l pl.UTF-8
Libsidplayfp (i jego konsolowy interfejs sidplayfp) to odgałęzienie
sidplay2 mające na celu poprawienie jakości emulacji układów 6581 i 8580
wraz z systemem C64, aby lepiej odtwarzać muzykę SID.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/sidplayfp
%attr(755,root,root) %{_bindir}/stilview
%{_mandir}/man1/sidplayfp.1*
%{_mandir}/man1/stilview.1*
%{_mandir}/man5/sidplayfp.ini.5*
