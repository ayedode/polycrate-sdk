from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.scope_enum import ScopeEnum, check_scope_enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PolicyBindingRequest")


@_attrs_define
class PolicyBindingRequest:
    """Serializer for PolicyBinding model.

    NEW in v4.0 - Replaces active_policies JSONField access via API.

        Attributes:
            policy_id (UUID):
            enabled (bool | Unset): Whether this binding is active
            scope (ScopeEnum | Unset): * `system` - System
                * `user` - User
            applied (bool | Unset): Whether policy was successfully applied
            execution_log (Any | Unset): List of actions performed/logged during last execution
    """

    policy_id: UUID
    enabled: bool | Unset = UNSET
    scope: ScopeEnum | Unset = UNSET
    applied: bool | Unset = UNSET
    execution_log: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        policy_id = str(self.policy_id)

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
                "policy_id": policy_id,
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

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("policy_id", (None, str(self.policy_id), "text/plain")))

        if not isinstance(self.enabled, Unset):
            files.append(("enabled", (None, str(self.enabled).encode(), "text/plain")))

        if not isinstance(self.scope, Unset):
            files.append(("scope", (None, str(self.scope).encode(), "text/plain")))

        if not isinstance(self.applied, Unset):
            files.append(("applied", (None, str(self.applied).encode(), "text/plain")))

        if not isinstance(self.execution_log, Unset):
            files.append(("execution_log", (None, str(self.execution_log).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        policy_id = UUID(d.pop("policy_id"))

        enabled = d.pop("enabled", UNSET)

        _scope = d.pop("scope", UNSET)
        scope: ScopeEnum | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = check_scope_enum(_scope)

        applied = d.pop("applied", UNSET)

        execution_log = d.pop("execution_log", UNSET)

        policy_binding_request = cls(
            policy_id=policy_id,
            enabled=enabled,
            scope=scope,
            applied=applied,
            execution_log=execution_log,
        )

        policy_binding_request.additional_properties = d
        return policy_binding_request

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
