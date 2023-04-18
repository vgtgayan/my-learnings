import logging

log = logging.getLogger(__name__)

msg = "Hello world"
log.info(f"{msg} info")
log.warning(f"{msg} warning")
log.error(f"{msg} error")
