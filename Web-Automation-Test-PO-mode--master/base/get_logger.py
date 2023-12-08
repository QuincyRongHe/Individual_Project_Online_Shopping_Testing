import logging.handlers


class GetLogger:
    logger = None

    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            cls.logger = logging.getLogger()
            cls.logger.setLevel(logging.INFO)
            sh = logging.StreamHandler()
            th = logging.handlers.TimedRotatingFileHandler(filename="./log/tradingsystem.log",
                                                           when="midnight",
                                                           interval=1,
                                                           backupCount=30,
                                                           encoding="utf-8")
            fm = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            fmt = logging.Formatter(fm)
            sh.setFormatter(fmt)
            th.setFormatter(fmt)
            cls.logger.addHandler(sh)
            cls.logger.addHandler(th)
        return cls.logger
