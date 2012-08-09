%define modname		transliteration
%define drupal_version	7
%define module_version	3.1
%define version		%{drupal_version}.x.%{module_version}
%define tarname		%{modname}-%{drupal_version}.x-%{module_version}

Name:		drupal-%{modname}
Summary:	Transliteration module for Drupal
Version:	%{version}
Release:	1
License:	GPLv2+
Group:		Networking/WWW
URL:		https://drupal.org/project/%{modname}
Source0:	http://ftp.drupal.org/files/projects/%{tarname}.tar.gz
BuildArch:	noarch
Requires:	drupal >= %{drupal_version}
Requires:	drupal < %{lua: print(rpm.expand("%{drupal_version}")+1)}

%description
Provides one-way string transliteration (romanization) and cleans file names
during upload by replacing unwanted characters.

Generally spoken, it takes Unicode text and tries to represent it in US-ASCII
characters (universally displayable, unaccented characters) by attempting
to transliterate the pronunciation expressed by the text in some other writing
system to Roman letters.

According to Unidecode, from which most of the transliteration data has been
derived, "Russian and Greek seem to work passably. But it works quite bad
on Japanese and Thai."

%prep
%setup -q -n %{modname}

%build

%install
%__install -d -m 0755 %{buildroot}%{_var}/www/drupal/modules/
cp -a . %{buildroot}%{_var}/www/drupal/modules/%{modname}
rm -f %{buildroot}%{_var}/www/drupal/modules/%{modname}/*.txt

%files
%{_var}/www/drupal/modules/%{modname}
%doc README.txt
