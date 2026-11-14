PORTNAME=	pyqt
DISTVERSION=	${PYQT_VERSION}
PORTREVISION=	2
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITES_PYQT}
PKGNAMEPREFIX=	${PYQT_PY_RELNAME}-
DISTNAME=	${PYQT_DISTNAME}

MAINTAINER=	kde@FreeBSD.org
COMMENT=	Python bindings for the Qt5 toolkit, QtCore module
WWW=		https://riverbankcomputing.com/software/pyqt

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}dbus>1:devel/py-dbus@${PY_FLAVOR}
LIB_DEPENDS=	libdbus-1.so:devel/dbus
RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}dbus>1:devel/py-dbus@${PY_FLAVOR}

USES=		gl pkgconfig python pyqt:5,dist qt:5
USE_GL=		gl
USE_PYQT=	pysip qtbuilder:build sip:build
USE_PYTHON=	concurrent flavors
USE_QT=		connectivity core dbus declarative designer gui help imageformats location \
		multimedia network opengl printsupport quick3d remoteobjects \
		sensors serialport speech sql svg testlib webchannel websockets \
		widgets x11extras xml xmlpatterns \
		buildtools:build qmake:build

SIP_ARGS=	--confirm-license \
		--disable Enginio \
		--disable QAxContainer \
		--disable QtWebKit \
		--disable QtWebKitWidgets \
		--disable QtWinExtras \
		--disable Qt

PORTSCOUT?=	limit:^${_QT_VERSION:R}

post-extract:
	${RM} -r ${WRKSRC}/pyuic/uic/port_v2

post-patch:
	${REINPLACE_CMD} \
		-e 's|%%PYQT_DESIGNERDIR%%|${PYQT_DESIGNERDIR}|' \
		-e 's|%%PYQT_QMLDIR%%|${PYQT_QMLDIR}|' \
		${WRKSRC}/project.py
	${REINPLACE_CMD} -e "s|uses_limited_api=True|uses_limited_api=False|" ${WRKSRC}/project.py
	${FIND} ${WRKSRC} -name '*.sip' -exec ${REINPLACE_CMD} -e "s|use_limited_api=True|use_limited_api=False|" {} +

pre-install:
	${FIND} ${WRKSRC}/build -name "Makefile*" -exec ${REINPLACE_CMD} -e "s|sip-distinfo-${PYTHON_BASEVER} |sip-distinfo |" {} +

post-install:
	${PYTHON_CMD} ${PYTHON_LIBDIR}/compileall.py \
		-f -d ${PYTHONPREFIX_SITELIBDIR}/PyQt5 \
		${STAGEDIR}${PYTHONPREFIX_SITELIBDIR}/PyQt5
	${PYTHON_CMD} -O ${PYTHON_LIBDIR}/compileall.py \
		-f -d ${PYTHONPREFIX_SITELIBDIR}/PyQt5 \
		${STAGEDIR}${PYTHONPREFIX_SITELIBDIR}/PyQt5
	@${FIND} ${STAGEDIR}${PYTHONPREFIX_SITELIBDIR}/PyQt5 \
		-name '*.so*' -exec ${STRIP_CMD} {} +
	@${FIND} ${STAGEDIR}${PYTHONPREFIX_SITELIBDIR}/dbus/mainloop \
		-name '*.so*' -exec ${STRIP_CMD} {} +

.include <bsd.port.mk>
