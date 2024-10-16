# TODO:
# - See how debian and fedora package things
# - Break helpers binaries out into seperate package and make main package
#   noarch
# - Remove .elc files so it works with both emacs and xemacs (policy?)
# - Fix stripping binaries (rpmlint)

%define name mew
%define version 6.5
%define release  3

Summary: Messaging in the Emacs World
Name: %{name}
Version: 6.8
Release: 1%{release}
Source0: http://www.mew.org/Release/%{name}-%{version}.tar.gz
Source1: %{name}.el
License: BSD-like
Group: Networking/Mail
Url: https://www.Mew.org/

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
%makeinstall elispdir=%{buildroot}%{_datadir}/emacs/site-lisp/%{name} etcdir=%{buildroot}%{_datadir}/pixmaps/mew INSTALLINFO=/sbin/install-info

%__install -dm 755 %{buildroot}%{_sysconfdir}/emacs/site-start.d
%__install -pm 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/emacs/site-start.d



%files
%defattr(-,root,root,0755)
%doc 00copyright 00readme 00diff 00changes*
%attr(0755,root,root) %{_bindir}/*
%{_datadir}/emacs/site-lisp/%{name}/*
%{_datadir}/pixmaps/mew/*
%{_infodir}/*
%{_mandir}/*
%config(noreplace) %{_sysconfdir}/emacs/site-start.d/%{name}.el
