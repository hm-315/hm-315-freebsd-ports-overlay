PORTNAME=	paramiko
PORTVERSION=	5.1.0
CATEGORIES=	security python
MASTER_SITES=	PYPI
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	sbz@FreeBSD.org
COMMENT=	Python SSH2 protocol library
WWW=		https://www.paramiko.org/

LICENSE=	LGPL21
LICENSE_FILE=	${WRKSRC}/LICENSE

BUILD_DEPENDS=	${PY_SETUPTOOLS}
RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}bcrypt>=3.2:security/py-bcrypt@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}invoke>=2.0:devel/py-invoke@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}PyNaCl>=1.5:security/py-pynacl@${PY_FLAVOR}
TEST_DEPENDS=	${PYTHON_PKGNAMEPREFIX}mock>=0:devel/py-mock@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}pytest-relaxed>=0:devel/py-pytest-relaxed@${PY_FLAVOR}

USES=		cpe python
USE_PYTHON=	autoplist cryptography pep517 pytest

NO_ARCH=	yes
TEST_ARGS=	-p no:relaxed

OPTIONS_DEFINE=		GSSAPI
GSSAPI_RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}gssapi>=1.4.1:security/py-gssapi@${PY_FLAVOR}

.include <bsd.port.mk>
