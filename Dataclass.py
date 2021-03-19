from dataclasses import dataclass, field, InitVar
import typing
import uuid

@dataclass
class Customer(object):
    database: InitVar[typing.Any]
    id: int
    name: str
    address: str

    def __post_init__(self, database):
        self.address = self.address.capitalize()
        self._connection = database.connect()

@dataclass(frozen=True, order= True)
class Customerbill(object):
    id: int = field(default_factory=uuid.uuid4, init=False)
    value: float
    product: str = field(compare=False)
