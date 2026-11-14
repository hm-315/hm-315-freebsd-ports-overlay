PORTNAME=	keychain
DISTVERSION=	3.0.8
CATEGORIES=	security

MAINTAINER=	garga@FreeBSD.org
COMMENT=	User-friendly front-end to ssh-agent(1) and gpg-agent(1)
WWW=		https://www.funtoo.org/Keychain

LICENSE=	GPLv3
LICENSE_FILE=	${WRKSRC}/LICENSE

.if !exists(${LOCALBASE}/bin/ssh-agent) && !exists(/usr/bin/ssh-agent)
RUN_DEPENDS+=	ssh-agent:security/openssh-portable
.endif

USES=		gmake python:3.9+

USE_GITHUB=	yes
GH_ACCOUNT=	funtoo

CONFLICTS_INSTALL=	py*-pycoin # bin/keychain

MAKE_ARGS=	PYTHON=${PYTHON_CMD} PREFIX=${PREFIX}
ALL_TARGET=	keychain-precompiled.pyz keychain.1

PLIST_FILES=	bin/${PORTNAME} \
		share/man/man1/keychain.1.gz
PORTDOCS=	ChangeLog.md README.md

OPTIONS_DEFINE=	DOCS

do-install:
	${INSTALL_SCRIPT} ${WRKSRC}/keychain-precompiled.pyz ${STAGEDIR}${PREFIX}/bin/${PORTNAME}
	${INSTALL_MAN} ${WRKSRC}/keychain.1 ${STAGEDIR}${PREFIX}/share/man/man1
	@${MKDIR} ${STAGEDIR}${DOCSDIR}
	${INSTALL_DATA} ${PORTDOCS:S|^|${WRKSRC}/|} ${STAGEDIR}${DOCSDIR}

.include <bsd.port.mk>
