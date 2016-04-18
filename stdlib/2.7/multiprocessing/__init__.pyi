# Stubs for multiprocessing (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from multiprocessing.process import Process as Process, current_process as current_process, active_children as active_children
from multiprocessing.util import SUBDEBUG as SUBDEBUG, SUBWARNING as SUBWARNING

class ProcessError(Exception): ...
class BufferTooShort(ProcessError): ...
class TimeoutError(ProcessError): ...
class AuthenticationError(ProcessError): ...

def Manager(): ...
def Pipe(duplex=True): ...
def cpu_count(): ...
def freeze_support(): ...
def get_logger(): ...
def log_to_stderr(level=None): ...
def allow_connection_pickling(): ...
def Lock(): ...
def RLock(): ...
def Condition(lock=None): ...
def Semaphore(value=1): ...
def BoundedSemaphore(value=1): ...
def Event(): ...
def Queue(maxsize=0): ...
def JoinableQueue(maxsize=0): ...
def Pool(processes=None, initializer=None, initargs=..., maxtasksperchild=None): ...
def RawValue(typecode_or_type, *args): ...
def RawArray(typecode_or_type, size_or_initializer): ...
def Value(typecode_or_type, *args, **kwds): ...
def Array(typecode_or_type, size_or_initializer, **kwds): ...
