import logging as log

log.basicConfig(
    level=log.DEBUG,
    format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
    datefmt='%I:%M:%S %p',
    handlers=[
        log.FileHandler('dataAccess.log'),
        log.StreamHandler()
    ]
)

if __name__ == '__main__':
    log.debug('DEBUG message level')
    log.info('INFO message level')
    log.warning('WARNING message level')
    log.error('ERROR message level')
    log.critical('CRITICAL message level')
