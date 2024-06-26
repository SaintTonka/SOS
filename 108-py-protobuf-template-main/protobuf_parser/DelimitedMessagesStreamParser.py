from protobuf_parser.helpers import parseDelimited
from google.protobuf.internal.decoder import _DecodeVarint32
from typing import TypeVar, Type
 
T = TypeVar('T')
 
 
class DelimitedMessagesStreamParser:
    def __init__(self, cls: Type[T]) -> None:
        self.cls = cls
        self.buf = bytearray()
 
    def parse(self, data: bytes) -> list[Type[T]]:
        messages = []
        
        try:
            self.buf += data
        except TypeError:
            return []

        while self.buf:
            message, ind = parseDelimited(self.buf, self.cls)
            if message:
                messages.append(message)
            else:
                break
 
            self.buf = self.buf[ind:]
 
        return messages