PORTNAME=	pykep
DISTVERSIONPREFIX=	v
#DISTVERSION=	2.6.4
DISTVERSION=	3.0.0
#PORTREVISION=	7
CATEGORIES=	astro python
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	yuri@FreeBSD.org
COMMENT=	Python binding for pykep, library for astrodynamics research
WWW=		https://github.com/esa/pykep

LICENSE=	GPLv3
#LICENSE_FILE=	${WRKSRC}/LICENSE.txt

BUILD_DEPENDS=	pybind11>0:devel/pybind11 \
		xtensor>0:math/xtensor \
		xtensor-blas>0:math/xtensor-blas
LIB_DEPENDS=	libboost_serialization.so:devel/boost-libs \
		libkep3.so:astro/pykep
RUN_DEPENDS=	${PYNUMPY} \
		${PYTHON_PKGNAMEPREFIX}matplotlib>0:math/py-matplotlib@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}pygmo2>0:science/py-pygmo2@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}scipy>0:science/py-scipy@${PY_FLAVOR}

USES=		cmake compiler:c++20-lang python
USE_PYTHON=	flavors

CMAKE_ON=	kep3_BUILD_PYTHON_BINDINGS
CMAKE_OFF=	kep3_BUILD_TESTS kep3_BUILD_BENCHMARKS

USE_GITHUB=	yes
GH_ACCOUNT=	esa

# the C++ library itself is packaged by astro/pykep
post-install:
	${RM} -r ${STAGEDIR}${PREFIX}/include/kep3 ${STAGEDIR}${PREFIX}/lib/cmake/kep3
	${RM} ${STAGEDIR}${PREFIX}/lib/libkep3.so*

.include <bsd.port.mk>
