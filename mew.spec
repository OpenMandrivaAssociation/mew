# TODO:
# - See how debian and fedora package things
# - Break helpers binaries out into seperate package and make main package
#   noarch
# - Remove .elc files so it works with both emacs and xemacs (policy?)
# - Fix stripping binaries (rpmlint)

%define name mew
%define version 5.2
%define release %mkrel 1

Summary: Messaging in the Emacs World
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Source1: %{name}.el
License: BSD-like
Group: Networking/Mail
Url: http://www.Mew.org/

BuildRequires: emacs
Requires: emacs

%description
Mew (Messaging in the Emacs World) is a user interface for text messages,
multimedia messages (MIME), news articles and security functionality 
including PGP, SSH and SSL. 

The features of Mew are as follows: 

 - POP, SMTP, NNTP, and IMAP are supported.
 - You can easily display a very complicated structured message.
 - You can start to read messages before they are all fully listed.
 - For refiling, default folders are neatly suggested.
 - You can complete field names, e-mail addresses, receiver's names,
   domain names, and folder names.
 - Thread, a mechanism to display the flow of messages, is supported.

%prep
%setup -q

%build
%configure 
%make elispdir=%{_datadir}/emacs/site-lisp/%{name} etcdir=%{_datadir}/pixmaps/mew

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall elispdir=$RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp/%{name} etcdir=$RPM_BUILD_ROOT%{_datadir}/pixmaps/mew INSTALLINFO=/sbin/install-info

%__install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/emacs/site-start.d
%__install -pm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/emacs/site-start.d

%clean
rm -rf $RPM_BUILD_ROOT

%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info

%files
%defattr(-,root,root,0755)
%doc 00copyright 00readme 00diff 00changes* 00roadmap
%attr(0755,root,root) %{_bindir}/*
%{_datadir}/emacs/site-lisp/%{name}/*
%{_datadir}/pixmaps/mew/*
%{_infodir}/*
%{_mandir}/*
%config(noreplace) %{_sysconfdir}/emacs/site-start.d/%{name}.el
