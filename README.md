zulu-12-compat-srpm
===============================

This is a plugin to allow the Zulu published 12.0.1 JDK to satisfy
dependencies for other RHEL packages, and to block installation of
openjdk or the distinct Oracle jdk package.  This plugin should be
installed along with the Zulu RPM, documented at
http://www.azul.com/.other conflicts.

The Zulu RPM does provide /etc/alternatives handling: this meta package prevents later requirements for java components to incidentally pull in openjdk and accidentally reset the default Java.

Setting the PATH or setting JAVA_HOME to enforce the use of the
expected Java is an exercise for the user. That need is usually
handled by providing a valid /etc/profile.d/jdk.sh, but I've not
attempted to provide one here.

The "make" command will do these steps.

make build	# Build the package on the local OS
make all	# Use "mock" to build the packages with the designated
		# local mock configurations

Nico Kadel-Garcia <nkadel@gmail.com>