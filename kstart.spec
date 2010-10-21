#
# Conditional build:
%bcond_with	krb5		# build with MIT kerberos
#
Summary:	Obtain and optionally keep active a Kerberos v5 ticket
Name:		kstart
Version:	3.16
Release:	0.1
License:	MIT
Group:		Applications
Source0:	http://archives.eyrie.org/software/kerberos/%{name}-%{version}.tar.gz
# Source0-md5:	cff45f24afef93305633b7d2480cd418
URL:		http://www.eyrie.org/~eagle/software/kstart/
%if %{with krb5}
BuildRequires:	krb5-devel
%else
BuildRequires:	heimdal-devel
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
k5start and krenew are modified versions of kinit which add support
for running as a daemon to maintain a ticket cache, running a command
with credentials from a keytab and maintaining a ticket cache until
that command completes, obtaining AFS tokens (via an external aklog)
after obtaining tickets, and creating an AFS PAG for a command.
They are primarily useful in conjunction with long-running jobs; for
moving ticket handling code out of servers, cron jobs, or daemons; and
to obtain tickets and AFS tokens with a single command.

%prep
%setup -q

%build
%configure \
	--disable-k4start

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
