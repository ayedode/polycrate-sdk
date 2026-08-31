from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.block_kind_enum import BlockKindEnum, check_block_kind_enum

T = TypeVar("T", bound="BlockRef")


@_attrs_define
class BlockRef:
    """Minimaler Block-Serializer für List-Contexts (z.B. ActionRunListSerializer).

    Enthält NUR id, name und url — keine nested workspace/organization.
    Eliminiert die teuren JOIN-Ketten block→workspace→organization aus List-Queries.

        Attributes:
            id (UUID):
            name (str):
            kind (BlockKindEnum): * `dockerapp` - Docker App
                * `linuxapp` - Linux App
                * `k8sapp` - Kubernetes App
                * `k8sappinstance` - Kubernetes App Instance
                * `k8scluster` - Kubernetes Cluster
                * `library` - Block Library
                * `generic` - Anything
            url (str):
    """

    id: UUID
    name: str
    kind: BlockKindEnum
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        kind: str = self.kind

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
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

        kind = check_block_kind_enum(d.pop("kind"))

        url = d.pop("url")

        block_ref = cls(
            id=id,
            name=name,
            kind=kind,
            url=url,
        )

        block_ref.additional_properties = d
        return block_ref

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
