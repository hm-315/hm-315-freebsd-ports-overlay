PORTNAME=	dspy
DISTVERSION=	3.3.1
CATEGORIES=	lang python
MASTER_SITES=	PYPI
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	hajime.murai@gmail.com
COMMENT=	Framework for programming--rather than prompting--language models
WWW=		https://github.com/stanfordnlp/dspy

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

BUILD_DEPENDS=	${PY_SETUPTOOLS}
RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}openai>=1.66.2:misc/py-openai@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}regex>=2023.10.3:textproc/py-regex@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}orjson>=3.9.0:devel/py-orjson@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}tqdm>=4.66.1:misc/py-tqdm@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}requests>=2.31.0:www/py-requests@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}pydantic2>=2.0:devel/py-pydantic2@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}litellm>=1.65.8:misc/py-litellm@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}diskcache>=5.6.0:devel/py-diskcache@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}json-repair>=0.54.2:textproc/py-json-repair@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}tenacity>=8.2.3:devel/py-tenacity@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}anyio>0:devel/py-anyio@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}cachetools>=5.5.0:devel/py-cachetools@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}cloudpickle>=3.1.2:devel/py-cloudpickle@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}gepa>=0.1.4<0.1.5:devel/py-gepa@${PY_FLAVOR}

USES=		python:3.10-3.14
USE_PYTHON=	autoplist pep517

NO_ARCH=	yes

.include <bsd.port.mk>
