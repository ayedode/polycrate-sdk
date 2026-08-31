from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="K8SVolumeSimple")


@_attrs_define
class K8SVolumeSimple:
    """Simple serializer for embedding K8sVolume in other serializers.

    Attributes:
        id (UUID):
        name (str):
        url (str):
        pvc_name (None | str):
    """

    id: UUID
    name: str
    url: str
    pvc_name: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        url = self.url

        pvc_name: None | str
        pvc_name = self.pvc_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "url": url,
                "pvc_name": pvc_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        url = d.pop("url")

        def _parse_pvc_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        pvc_name = _parse_pvc_name(d.pop("pvc_name"))

        k8s_volume_simple = cls(
            id=id,
            name=name,
            url=url,
            pvc_name=pvc_name,
        )

        k8s_volume_simple.additional_properties = d
        return k8s_volume_simple

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
