from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pop_kind_enum import PopKindEnum, check_pop_kind_enum

T = TypeVar("T", bound="PopSimple")


@_attrs_define
class PopSimple:
    """Simple serializer for embedding Pop in other serializers.

    Attributes:
        id (UUID):
        name (str):
        reconciliation_running (bool):
        kind (PopKindEnum): * `datacenter` - Datacenter
            * `datacenter-park` - Datacenter Park
            * `region` - Region
        url (str):
    """

    id: UUID
    name: str
    reconciliation_running: bool
    kind: PopKindEnum
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        reconciliation_running = self.reconciliation_running

        kind: str = self.kind

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "reconciliation_running": reconciliation_running,
                "kind": kind,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        reconciliation_running = d.pop("reconciliation_running")

        kind = check_pop_kind_enum(d.pop("kind"))

        url = d.pop("url")

        pop_simple = cls(
            id=id,
            name=name,
            reconciliation_running=reconciliation_running,
            kind=kind,
            url=url,
        )

        pop_simple.additional_properties = d
        return pop_simple

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
