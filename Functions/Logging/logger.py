import logging

swapper_logger = logging
swapper_logger.basicConfig(filemode="swapperlog.log", level=logging.DEBUG,
                           format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
