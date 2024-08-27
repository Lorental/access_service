from .models import Log


def logsave(action, log, username):
    logmessage = Log()
    logmessage.action = action
    logmessage.log = log
    logmessage.created_by = username
    logmessage.save()
