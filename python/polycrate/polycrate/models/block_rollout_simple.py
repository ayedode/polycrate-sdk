from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.block_rollout_status_enum import BlockRolloutStatusEnum, check_block_rollout_status_enum

T = TypeVar("T", bound="BlockRolloutSimple")


@_attrs_define
class BlockRolloutSimple:
    """
    Attributes:
        id (UUID):
        name (str):
        batch_identifier (str):
        status (BlockRolloutStatusEnum): * `active` - Active
            * `paused` - Paused
            * `blocked` - Blocked
            * `completed` - Completed
            * `cancelled` - Cancelled
        total_items (int):
        completed_items (int):
        failed_items (int):
        url (str):
    """

    id: UUID
    name: str
    batch_identifier: str
    status: BlockRolloutStatusEnum
    total_items: int
    completed_items: int
    failed_items: int
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        batch_identifier = self.batch_identifier

        status: str = self.status

        total_items = self.total_items

        completed_items = self.completed_items

        failed_items = self.failed_items

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "batch_identifier": batch_identifier,
                "status": status,
                "total_items": total_items,
                "completed_items": completed_items,
                "failed_items": failed_items,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        batch_identifier = d.pop("batch_identifier")

        status = check_block_rollout_status_enum(d.pop("status"))

        total_items = d.pop("total_items")

        completed_items = d.pop("completed_items")

        failed_items = d.pop("failed_items")

        url = d.pop("url")

        block_rollout_simple = cls(
            id=id,
            name=name,
            batch_identifier=batch_identifier,
            status=status,
            total_items=total_items,
            completed_items=completed_items,
            failed_items=failed_items,
            url=url,
        )

        block_rollout_simple.additional_properties = d
        return block_rollout_simple

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
