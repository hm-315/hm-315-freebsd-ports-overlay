PORTNAME=	blosc2
PORTVERSION=	4.12.0
CATEGORIES=	archivers python
MASTER_SITES=	PYPI
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	sunpoet@FreeBSD.org
COMMENT=	Fast and compressed ndarray library with a flexible compute engine
WWW=		https://www.blosc.org/python-blosc2/ \
		https://github.com/Blosc/python-blosc2

LICENSE=	BSD3CLAUSE
LICENSE_FILE=	${WRKSRC}/LICENSE.txt

BUILD_DEPENDS=	c-blosc2>=2.21.3:archivers/c-blosc2 \
		${PYTHON_PKGNAMEPREFIX}numpy>=0,1:math/py-numpy@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}scikit-build-core>=0:devel/py-scikit-build-core@${PY_FLAVOR}
LIB_DEPENDS=	libblosc2.so:archivers/c-blosc2
RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}msgpack>=0:devel/py-msgpack@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}ndindex>=0:math/py-ndindex@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}numexpr>=2.14.1:math/py-numexpr@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}numpy>=0,1:math/py-numpy@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}py-cpuinfo2>=0:sysutils/py-py-cpuinfo2@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}requests>=0:www/py-requests@${PY_FLAVOR}

USE_GITHUB=	nodefault
GH_TUPLE=	Blosc:miniexpr:f0b8c94771cd21d3c9029d6ccec204ab3a67584f:miniexpr/miniexpr-src \
		Blosc:minicc:695ad1e6b5c9a00875192ca1f3a9c4949dee4858:minicc/minicc-src \
		shibatch:sleef:7623d6cfa2712462880fa63a4d0f0b5f775d1a83:sleef/sleef-src
DISTFILES=	${DISTNAME}${EXTRACT_SUFX}

USES=		cmake:indirect pkgconfig python
USE_PYTHON=	autoplist concurrent cython pep517

MAKE_ENV=	USE_SYSTEM_BLOSC2=1 \
		CMAKE_ARGS=-C${WRKSRC}/fetchcontent-preload.cmake

post-patch:
	@${ECHO_CMD} 'set(FETCHCONTENT_SOURCE_DIR_MINIEXPR "${WRKSRC}/miniexpr-src" CACHE PATH "")' > ${WRKSRC}/fetchcontent-preload.cmake
	@${ECHO_CMD} 'set(FETCHCONTENT_SOURCE_DIR_SLEEF "${WRKSRC}/sleef-src" CACHE PATH "")' >> ${WRKSRC}/fetchcontent-preload.cmake
	@${ECHO_CMD} 'set(FETCHCONTENT_SOURCE_DIR_TINYCC "${WRKSRC}/minicc-src" CACHE PATH "")' >> ${WRKSRC}/fetchcontent-preload.cmake

post-install:
	${FIND} ${STAGEDIR}${PYTHON_SITELIBDIR} -name '*.so' -exec ${STRIP_CMD} {} +

.include <bsd.port.mk>
