bind = "0.0.0.0:80"
workers = 2
threads = 2
timeout = 180
errorlog = "-"
loglevel = "info"
accesslog = "-"
access_log_format = '%(L)s %(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'