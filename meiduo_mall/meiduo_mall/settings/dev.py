"""
Django settings for meiduo_mall project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys
import datetime
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# 内层`meiduo_mall`目录

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 将`apps`添加到项目的搜索包目录列表
# sys.path.insert(0, '/Users/smart/Desktop/code/meiduo/meiduo_mall/meiduo_mall/apps')

# print(sys.path)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x4rn*q#yf8q4)d!@v8jj8_g%y^8+*f3p#(%jq+^9w^6o3yl$n+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',

    'django_crontab',  # 定时任务
    'haystack',

    'users.apps.UsersConfig',
    'verifications.apps.VerificationsConfig',
    'oauth.apps.OauthConfig',
    'areas.apps.AreasConfig',
    'contents.apps.ContentsConfig',
    'goods.apps.GoodsConfig',
    'cart.apps.CartConfig',
    'orders.apps.OrdersConfig',
    'payment.apps.PaymentConfig',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'meiduo_mall.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 指定模板文件目录
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'meiduo_mall.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '192.168.19.131',  # 数据库主机
        'PORT': 3306,  # 数据库端口
        'USER': 'root',  # 数据库用户名
        'PASSWORD': 'mysql',  # 数据库用户密码
        'NAME': 'meiduo_db'  # 数据库名字
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'


# Django框架的缓存设置，默认Django框架的缓存为服务器的内存，此处将Django框架的缓存改为了redis
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://192.168.19.131:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "session": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://192.168.19.131:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    # 存储短信验证码内容
    "verify_codes": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://192.168.19.131:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    # 存储浏览记录
    "histories": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://192.168.19.131:6379/4",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    # 存储购物车记录
    "cart": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://192.168.19.131:6379/5",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
}
# 设置将session信息存储到缓存中，上面已经将缓存改为了redis，所有session会存放到redis中
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# 指定session存储到缓存空间的名称
SESSION_CACHE_ALIAS = "session"

# Django日志存储设置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # 是否禁用已经存在的日志器
    'formatters': {  # 日志信息显示的格式
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        },
    },
    'filters': {  # 对日志进行过滤
        'require_debug_true': {  # django在debug模式下才输出日志
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {  # 日志处理方法
        'console': {  # 向终端中输出日志
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {  # 向文件中输出日志
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(os.path.dirname(BASE_DIR), "logs/meiduo.log"),  # 日志文件的位置
            'maxBytes': 300 * 1024 * 1024,
            'backupCount': 10,
            'formatter': 'verbose'
        },
    },
    'loggers': {  # 日志器
        'django': {  # 定义了一个名为django的日志器
            'handlers': ['console', 'file'],  # 可以同时向终端与文件中输出日志
            'propagate': True,  # 是否继续传递日志信息
            'level': 'INFO',  # 日志器接收的最低日志级别
        },
    }
}

# 输出日志
# 1. 获取日志器
# import logging
# logger = logging.getLogger('django')

# 2. 输出日志
# logger.debug('Debug Message')
# logger.info('Info Message')
# logger.warning('Warn Message')
# logger.error('Error Message')
# logger.critical('Critical Message')

# DRF框架设置
REST_FRAMEWORK = {
    # 指定DRF框架的异常处理函数
    'EXCEPTION_HANDLER': 'meiduo_mall.utils.exceptions.exception_handler',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 引入JWT认证机制，将来客户端传递了jwt token给服务器之后，此认证机制会校验jwt token数据的有效性
        # 如果认证失败，会直接给客户端返回401(未认证)
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    # 指定DRF框架的全局分页类
    'DEFAULT_PAGINATION_CLASS': 'meiduo_mall.utils.pagination.StandardResultPagination'
}

# JWT扩展设置
JWT_AUTH = {
    # 设置JWT的有效时间
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'users.utils.jwt_response_payload_handler'
}

# 指定Django认证系统所使用的用户模型类
# AUTH_USER_MODEL = '子应用.模型类'
AUTH_USER_MODEL = 'users.User'

# CORS设置
CORS_ORIGIN_WHITELIST = (
    'http://127.0.0.1:8080',
    'http://www.meiduo.site:8080',
    'http://www.meiduo.site',
)
CORS_ALLOW_CREDENTIALS = True  # 允许携带cookie

# 指定Django的认证后端类
AUTHENTICATION_BACKENDS = ['users.utils.UserNameMobileBackend']

# QQ登录配置
QQ_CLIENT_ID = '101474184' # 开发者应用APPID
QQ_CLIENT_SECRET = 'c6ce949e04e12ecc909ae6a8b09b637c' # 开发者应用APPKEY
QQ_REDIRECT_URI = 'http://www.meiduo.site:8080/oauth_callback.html' # 回调网址

# 邮件发送的配置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# SMTP服务器地址
EMAIL_HOST = 'smtp.163.com'
# SMTP服务端口
EMAIL_PORT = 25
# 发送邮件的邮箱
EMAIL_HOST_USER = 'smartli_it@163.com'
# 在邮箱中设置的客户端授权密码
EMAIL_HOST_PASSWORD = 'smart123'
# 收件人看到的发件人
EMAIL_FROM = '美多商城<smartli_it@163.com>'


# DRF扩展
REST_FRAMEWORK_EXTENSIONS = {
    # 缓存时间
    'DEFAULT_CACHE_RESPONSE_TIMEOUT': 60 * 60,
    # 缓存存储
    'DEFAULT_USE_CACHE': 'default',
}

# 指定FDFS客户端配置文件路径
FDFS_CLIENT_CONF = os.path.join(BASE_DIR, 'utils/fastdfs/client.conf')
# 指定FDFS系统中Nginx地址
FDFS_NGINX_URL = 'http://192.168.19.131:8888/'

# 指定Django系统的文件存储类
DEFAULT_FILE_STORAGE = 'meiduo_mall.utils.fastdfs.storage.FDFSStorage'

# 生成的静态html文件保存目录
GENERATED_STATIC_HTML_FILES_DIR = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), 'front_page')

# 定时任务配置
CRONJOBS = [
    # 每1分钟执行一次生成主页静态文件
    ('*/1 * * * *', 'contents.crons.generate_static_index_html', '>> ' + os.path.dirname(BASE_DIR) + '/logs/crontab.log')
]

# 解决crontab中文问题
CRONTAB_COMMAND_PREFIX = 'LANG_ALL=zh_cn.UTF-8'

# Haystack全文检索框架配置
HAYSTACK_CONNECTIONS = {
    'default': {
        # 指明所使用的搜索引擎的类型
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        # 指明搜索引擎服务器的ip和port
        'URL': 'http://192.168.19.131:9200/',
        # 指定elasticsearch建立的索引库的名称
        'INDEX_NAME': 'meiduo_index',
    },
}

# 当添加、修改、删除数据时，自动生成索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'


# 支付宝开发配置
ALIPAY_APPID = "2016090800464054" # 开发者应用APP
ALIPAY_URL = "https://openapi.alipaydev.com/gateway.do" # 网关地址
ALIPAY_DEBUG = True # 是否使用沙箱环境

# 指定收集静态文件的保存目录
# STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), 'front_page/static')
