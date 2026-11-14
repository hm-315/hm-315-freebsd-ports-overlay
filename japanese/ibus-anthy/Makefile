PORTNAME=	ibus-anthy
DISTVERSION=	1.5.18
CATEGORIES=	japanese
MASTER_SITES=	https://github.com/ibus/ibus-anthy/releases/download/${DISTVERSION}/
PKGNAMEPREFIX=	ja-

MAINTAINER=	CQG00620@nifty.ne.jp
COMMENT=	Anthy engine for IBus
WWW=		https://github.com/ibus/ibus-anthy

LICENSE=	GPLv2
LICENSE_FILE=	${WRKSRC}/COPYING

LIB_DEPENDS=	libibus-1.0.so:textproc/ibus \
		libanthy-unicode.so:japanese/anthy-unicode

USES=		gettext gmake gnome libtool pkgconfig python shebangfix
USE_GNOME=	pygobject3
SHEBANG_FILES=	data/era.py data/zipcode-textdic.py
GLIB_SCHEMAS=	org.freedesktop.ibus.engine.anthy.gschema.xml

GNU_CONFIGURE=	yes
CONFIGURE_ARGS=	--with-layout=default
INSTALL_TARGET=	install-strip

.include <bsd.port.mk>
