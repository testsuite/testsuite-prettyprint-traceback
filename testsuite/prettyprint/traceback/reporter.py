from nose2.plugins.result import ResultReporter


class PrettyTracebackReporter(ResultReporter):
    commandLineSwitch = (
        None, 'pretty-print-traceback', 'Prettyprint Traceback on errors and failures')
    configSection = 'pretty-print'