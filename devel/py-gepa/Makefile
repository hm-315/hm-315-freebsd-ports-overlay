PORTNAME=	gepa
DISTVERSION=	0.1.4
CATEGORIES=	devel python
MASTER_SITES=	PYPI
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	hajime.murai@gmail.com
COMMENT=	Optimize text components of arbitrary systems using LLM reflection
WWW=		https://github.com/gepa-ai/gepa

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

BUILD_DEPENDS=	${PY_SETUPTOOLS} \
		${PYTHON_PKGNAMEPREFIX}wheel>=0:devel/py-wheel@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}build>=0:devel/py-build@${PY_FLAVOR}

USES=		python:3.10-3.14
USE_PYTHON=	autoplist pep517

NO_ARCH=	yes

.include <bsd.port.mk>
