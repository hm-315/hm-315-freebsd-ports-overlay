PORTNAME=	pytokens
PORTVERSION=	0.4.1
CATEGORIES=	devel python
MASTER_SITES=	PYPI
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	sunpoet@FreeBSD.org
COMMENT=	Fast, spec compliant Python 3.14+ tokenizer that runs on older Pythons
WWW=		https://github.com/tusharsadhwani/pytokens

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

# mypyc build disabled: py-mypy needs py-orjson, which does not support free-threaded Python (py314t)
BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}setuptools>=61:devel/py-setuptools@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}wheel>=0:devel/py-wheel@${PY_FLAVOR}

USES=		python
USE_PYTHON=	autoplist concurrent pep517

NO_ARCH=	yes
MAKE_ENV=	PYTOKENS_USE_MYPYC=0

post-install:
	${FIND} ${STAGEDIR}${PYTHON_SITELIBDIR} -name '*.so' -exec ${STRIP_CMD} {} +

.include <bsd.port.mk>
