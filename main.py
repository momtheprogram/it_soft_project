from dataclasses import dataclass, asdict
from enum import StrEnum
from typing import Any


class StatusEnum(StrEnum):
    ON = 'on'
    OFF = 'off'


@dataclass
class Device:
    """
    Объектами класса Device будут устройства с определенными параметрами.
    """
    id: int
    alias: str
    status: StatusEnum
    ip: str

    @classmethod
    def from_jsonable(cls, jsonable: dict[str, Any]) -> 'Device':
        return cls(
            id=jsonable['id'],
            alias=jsonable['alias'],
            status=jsonable['status'],
            ip=jsonable['ip']
        )

    def to_jsonable(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class Entity:
    """
    Объект класса Entity будет представлять собой некую сущность типа шкафа,
    хранящего в себе коллекцию неких устройств с определенными параметрами (объектов класса Device).
    """

    devices: list[Device]

    @classmethod
    def from_jsonable(cls, jsonable: dict[str, Any]) -> 'Entity':
        devices = [Device.from_jsonable(device) for device in jsonable['devices']]

        return cls(devices)

    def to_jsonable(self) -> dict[str, Any]:
        return {
            'devices': [device.to_jsonable() for device in self.devices]
        }
