from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.scope_enum import ScopeEnum, check_scope_enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PolicyBindingList")


@_attrs_define
class PolicyBindingList:
    """Lightweight serializer for binding lists.

    Attributes:
        id (int):
        policy_id (UUID): The policy to bind
        assigned_at (datetime.datetime):
        cached_policy_name (str | Unset): Cached policy display_name
        enabled (bool | Unset): Whether this binding is active
        scope (ScopeEnum | Unset): * `system` - System
            * `user` - User
        applied (bool | Unset): Whether policy was successfully applied
    """

    id: int
    policy_id: UUID
    assigned_at: datetime.datetime
    cached_policy_name: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    scope: ScopeEnum | Unset = UNSET
    applied: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        policy_id = str(self.policy_id)

        assigned_at = self.assigned_at.isoformat()

        cached_policy_name = self.cached_policy_name

        enabled = self.enabled

        scope: str | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope

        applied = self.applied

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "policy_id": policy_id,
                "assigned_at": assigned_at,
            }
        )
        if cached_policy_name is not UNSET:
            field_dict["cached_policy_name"] = cached_policy_name
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if scope is not UNSET:
            field_dict["scope"] = scope
        if applied is not UNSET:
            field_dict["applied"] = applied

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        policy_id = UUID(d.pop("policy_id"))

        assigned_at = datetime.datetime.fromisoformat(d.pop("assigned_at"))

        cached_policy_name = d.pop("cached_policy_name", UNSET)

        enabled = d.pop("enabled", UNSET)

        _scope = d.pop("scope", UNSET)
        scope: ScopeEnum | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = check_scope_enum(_scope)

        applied = d.pop("applied", UNSET)

        policy_binding_list = cls(
            id=id,
            policy_id=policy_id,
            assigned_at=assigned_at,
            cached_policy_name=cached_policy_name,
            enabled=enabled,
            scope=scope,
            applied=applied,
        )

        policy_binding_list.additional_properties = d
        return policy_binding_list

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
