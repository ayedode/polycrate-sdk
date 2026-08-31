from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.match_type_enum import MatchTypeEnum, check_match_type_enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertCategoryMapping")


@_attrs_define
class AlertCategoryMapping:
    """
    Attributes:
        id (int):
        category_id (UUID):
        category_name (str):
        pattern (str): Normalized pattern (lowercase). For contains_all use part1|||part2.
        is_system (bool):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        match_type (MatchTypeEnum | Unset): * `exact` - Exact
            * `prefix` - Prefix
            * `contains` - Contains
            * `contains_all` - Contains all (AND) Default: 'exact'.
        priority (int | Unset): Lower priority wins (first match).
    """

    id: int
    category_id: UUID
    category_name: str
    pattern: str
    is_system: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    match_type: MatchTypeEnum | Unset = "exact"
    priority: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        category_id = str(self.category_id)

        category_name = self.category_name

        pattern = self.pattern

        is_system = self.is_system

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        match_type: str | Unset = UNSET
        if not isinstance(self.match_type, Unset):
            match_type = self.match_type

        priority = self.priority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "category_id": category_id,
                "category_name": category_name,
                "pattern": pattern,
                "is_system": is_system,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if match_type is not UNSET:
            field_dict["match_type"] = match_type
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        category_id = UUID(d.pop("category_id"))

        category_name = d.pop("category_name")

        pattern = d.pop("pattern")

        is_system = d.pop("is_system")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        _match_type = d.pop("match_type", UNSET)
        match_type: MatchTypeEnum | Unset
        if isinstance(_match_type, Unset):
            match_type = UNSET
        else:
            match_type = check_match_type_enum(_match_type)

        priority = d.pop("priority", UNSET)

        alert_category_mapping = cls(
            id=id,
            category_id=category_id,
            category_name=category_name,
            pattern=pattern,
            is_system=is_system,
            created_at=created_at,
            updated_at=updated_at,
            match_type=match_type,
            priority=priority,
        )

        alert_category_mapping.additional_properties = d
        return alert_category_mapping

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
