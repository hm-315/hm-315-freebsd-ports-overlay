PORTNAME=	zfp
DISTVERSION=	1.0.1
PORTREVISION=	2
CATEGORIES=	devel science
MASTER_SITES=	https://github.com/LLNL/${PORTNAME}/releases/download/${DISTVERSION}/
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	yuri@FreeBSD.org
COMMENT=	High throughput library for compressed floating-point arrays
WWW=		https://computing.llnl.gov/projects/zfp \
		https://github.com/LLNL/zfp

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/scikit-build-cmake/LICENSE

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}numpy>=1.16:math/py-numpy@${PY_FLAVOR} \
		${PY_SETUPTOOLS}
LIB_DEPENDS=	libzfp.so:devel/zfp
RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}numpy>=1.16:math/py-numpy@${PY_FLAVOR}

USES=		cmake localbase:ldflags python
USE_PYTHON=	cython flavors pytest

WRKSRC_SUBDIR=	python

TEST_WRKSRC=	${WRKSRC}/../tests/python
TEST_ENV=	${MAKE_ENV} PYTHONPATH=${STAGEDIR}${PYTHONPREFIX_SITELIBDIR}

PLIST_FILES=	${PYTHON_SITELIBDIR}/zfpy${PYTHON_SOABI}.so

# tests fail to run, see https://github.com/LLNL/zfp/issues/251


post-install:
	${MKDIR} ${STAGEDIR}${PYTHONPREFIX_SITELIBDIR}
	${MV} ${STAGEDIR}${PREFIX}/lib/python${PYTHON_BASEVER}/site-packages/zfpy*.so ${STAGEDIR}${PYTHONPREFIX_SITELIBDIR}/
	-@${RMDIR} ${STAGEDIR}${PREFIX}/lib/python${PYTHON_BASEVER}/site-packages ${STAGEDIR}${PREFIX}/lib/python${PYTHON_BASEVER}

.include <bsd.port.mk>
