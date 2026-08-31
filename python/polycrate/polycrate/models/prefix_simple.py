from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PrefixSimple")


@_attrs_define
class PrefixSimple:
    """Simple serializer for embedding Prefix in other serializers.

    Attributes:
        id (UUID):
        name (str):
        cidr (str): Prefix CIDR, e.g. 192.168.1.0/24
        url (str):
    """

    id: UUID
    name: str
    cidr: str
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        cidr = self.cidr

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "cidr": cidr,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        cidr = d.pop("cidr")

        url = d.pop("url")

        prefix_simple = cls(
            id=id,
            name=name,
            cidr=cidr,
            url=url,
        )

        prefix_simple.additional_properties = d
        return prefix_simple

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
