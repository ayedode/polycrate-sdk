from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.match_type_enum import MatchTypeEnum, check_match_type_enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedAlertCategoryMappingRequest")


@_attrs_define
class PatchedAlertCategoryMappingRequest:
    """
    Attributes:
        category_id (UUID | Unset):
        match_type (MatchTypeEnum | Unset): * `exact` - Exact
            * `prefix` - Prefix
            * `contains` - Contains
            * `contains_all` - Contains all (AND) Default: 'exact'.
        pattern (str | Unset): Normalized pattern (lowercase). For contains_all use part1|||part2.
        priority (int | Unset): Lower priority wins (first match).
    """

    category_id: UUID | Unset = UNSET
    match_type: MatchTypeEnum | Unset = "exact"
    pattern: str | Unset = UNSET
    priority: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category_id: str | Unset = UNSET
        if not isinstance(self.category_id, Unset):
            category_id = str(self.category_id)

        match_type: str | Unset = UNSET
        if not isinstance(self.match_type, Unset):
            match_type = self.match_type

        pattern = self.pattern

        priority = self.priority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category_id is not UNSET:
            field_dict["category_id"] = category_id
        if match_type is not UNSET:
            field_dict["match_type"] = match_type
        if pattern is not UNSET:
            field_dict["pattern"] = pattern
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.category_id, Unset):
            files.append(("category_id", (None, str(self.category_id), "text/plain")))

        if not isinstance(self.match_type, Unset):
            files.append(("match_type", (None, str(self.match_type).encode(), "text/plain")))

        if not isinstance(self.pattern, Unset):
            files.append(("pattern", (None, str(self.pattern).encode(), "text/plain")))

        if not isinstance(self.priority, Unset):
            files.append(("priority", (None, str(self.priority).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _category_id = d.pop("category_id", UNSET)
        category_id: UUID | Unset
        if isinstance(_category_id, Unset):
            category_id = UNSET
        else:
            category_id = UUID(_category_id)

        _match_type = d.pop("match_type", UNSET)
        match_type: MatchTypeEnum | Unset
        if isinstance(_match_type, Unset):
            match_type = UNSET
        else:
            match_type = check_match_type_enum(_match_type)

        pattern = d.pop("pattern", UNSET)

        priority = d.pop("priority", UNSET)

        patched_alert_category_mapping_request = cls(
            category_id=category_id,
            match_type=match_type,
            pattern=pattern,
            priority=priority,
        )

        patched_alert_category_mapping_request.additional_properties = d
        return patched_alert_category_mapping_request

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
