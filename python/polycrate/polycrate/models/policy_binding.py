from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.scope_enum import ScopeEnum, check_scope_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.policy import Policy


T = TypeVar("T", bound="PolicyBinding")


@_attrs_define
class PolicyBinding:
    """Serializer for PolicyBinding model.

    NEW in v4.0 - Replaces active_policies JSONField access via API.

        Attributes:
            id (int):
            policy (Policy): Serializer for Policy model.
                Per .specs/0.11.4/dynamic-table-v2.md - inherits from ManagedObjectDetailSerializer.
                organization/workspace werden automatisch von ManagedObjectDetailSerializer bereitgestellt.
            target_type (None | str):
            target_id (str):
            target_display_name (None | str):
            cached_policy_name (str): Cached policy display_name
            cached_policy_order (int): Cached policy order
            assigned_at (datetime.datetime):
            last_applied_at (datetime.datetime | None):
            enabled (bool | Unset): Whether this binding is active
            scope (ScopeEnum | Unset): * `system` - System
                * `user` - User
            applied (bool | Unset): Whether policy was successfully applied
            execution_log (Any | Unset): List of actions performed/logged during last execution
    """

    id: int
    policy: Policy
    target_type: None | str
    target_id: str
    target_display_name: None | str
    cached_policy_name: str
    cached_policy_order: int
    assigned_at: datetime.datetime
    last_applied_at: datetime.datetime | None
    enabled: bool | Unset = UNSET
    scope: ScopeEnum | Unset = UNSET
    applied: bool | Unset = UNSET
    execution_log: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        policy = self.policy.to_dict()

        target_type: None | str
        target_type = self.target_type

        target_id = self.target_id

        target_display_name: None | str
        target_display_name = self.target_display_name

        cached_policy_name = self.cached_policy_name

        cached_policy_order = self.cached_policy_order

        assigned_at = self.assigned_at.isoformat()

        last_applied_at: None | str
        if isinstance(self.last_applied_at, datetime.datetime):
            last_applied_at = self.last_applied_at.isoformat()
        else:
            last_applied_at = self.last_applied_at

        enabled = self.enabled

        scope: str | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope

        applied = self.applied

        execution_log = self.execution_log

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "policy": policy,
                "target_type": target_type,
                "target_id": target_id,
                "target_display_name": target_display_name,
                "cached_policy_name": cached_policy_name,
                "cached_policy_order": cached_policy_order,
                "assigned_at": assigned_at,
                "last_applied_at": last_applied_at,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if scope is not UNSET:
            field_dict["scope"] = scope
        if applied is not UNSET:
            field_dict["applied"] = applied
        if execution_log is not UNSET:
            field_dict["execution_log"] = execution_log

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.policy import Policy

        d = dict(src_dict)
        id = d.pop("id")

        policy = Policy.from_dict(d.pop("policy"))

        def _parse_target_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        target_type = _parse_target_type(d.pop("target_type"))

        target_id = d.pop("target_id")

        def _parse_target_display_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        target_display_name = _parse_target_display_name(d.pop("target_display_name"))

        cached_policy_name = d.pop("cached_policy_name")

        cached_policy_order = d.pop("cached_policy_order")

        assigned_at = datetime.datetime.fromisoformat(d.pop("assigned_at"))

        def _parse_last_applied_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_applied_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_applied_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_applied_at = _parse_last_applied_at(d.pop("last_applied_at"))

        enabled = d.pop("enabled", UNSET)

        _scope = d.pop("scope", UNSET)
        scope: ScopeEnum | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = check_scope_enum(_scope)

        applied = d.pop("applied", UNSET)

        execution_log = d.pop("execution_log", UNSET)

        policy_binding = cls(
            id=id,
            policy=policy,
            target_type=target_type,
            target_id=target_id,
            target_display_name=target_display_name,
            cached_policy_name=cached_policy_name,
            cached_policy_order=cached_policy_order,
            assigned_at=assigned_at,
            last_applied_at=last_applied_at,
            enabled=enabled,
            scope=scope,
            applied=applied,
            execution_log=execution_log,
        )

        policy_binding.additional_properties = d
        return policy_binding

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
