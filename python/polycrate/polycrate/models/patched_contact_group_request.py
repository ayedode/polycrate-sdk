from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.contact_group_kind_enum import ContactGroupKindEnum, check_contact_group_kind_enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedContactGroupRequest")


@_attrs_define
class PatchedContactGroupRequest:
    """Full serializer for ContactGroup detail views and CRUD operations.

    Includes complete related object data and computed fields.

        Attributes:
            name (str | Unset):
            kind (ContactGroupKindEnum | Unset): * `generic` - Generic
                * `dynamic` - Dynamic
            organization_id (UUID | Unset):
            email (None | str | Unset): Group email address for notifications
            dynamic_rules (Any | Unset): Rules for dynamic group membership (JSON format)
            keycloak_group_id (None | str | Unset): Keycloak group ID for automatic synchronization
    """

    name: str | Unset = UNSET
    kind: ContactGroupKindEnum | Unset = UNSET
    organization_id: UUID | Unset = UNSET
    email: None | str | Unset = UNSET
    dynamic_rules: Any | Unset = UNSET
    keycloak_group_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        organization_id: str | Unset = UNSET
        if not isinstance(self.organization_id, Unset):
            organization_id = str(self.organization_id)

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        dynamic_rules = self.dynamic_rules

        keycloak_group_id: None | str | Unset
        if isinstance(self.keycloak_group_id, Unset):
            keycloak_group_id = UNSET
        else:
            keycloak_group_id = self.keycloak_group_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if kind is not UNSET:
            field_dict["kind"] = kind
        if organization_id is not UNSET:
            field_dict["organization_id"] = organization_id
        if email is not UNSET:
            field_dict["email"] = email
        if dynamic_rules is not UNSET:
            field_dict["dynamic_rules"] = dynamic_rules
        if keycloak_group_id is not UNSET:
            field_dict["keycloak_group_id"] = keycloak_group_id

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.kind, Unset):
            files.append(("kind", (None, str(self.kind).encode(), "text/plain")))

        if not isinstance(self.organization_id, Unset):
            files.append(("organization_id", (None, str(self.organization_id), "text/plain")))

        if not isinstance(self.email, Unset):
            if isinstance(self.email, str):
                files.append(("email", (None, str(self.email).encode(), "text/plain")))
            else:
                files.append(("email", (None, str(self.email).encode(), "text/plain")))

        if not isinstance(self.dynamic_rules, Unset):
            files.append(("dynamic_rules", (None, str(self.dynamic_rules).encode(), "text/plain")))

        if not isinstance(self.keycloak_group_id, Unset):
            if isinstance(self.keycloak_group_id, str):
                files.append(("keycloak_group_id", (None, str(self.keycloak_group_id).encode(), "text/plain")))
            else:
                files.append(("keycloak_group_id", (None, str(self.keycloak_group_id).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: ContactGroupKindEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_contact_group_kind_enum(_kind)

        _organization_id = d.pop("organization_id", UNSET)
        organization_id: UUID | Unset
        if isinstance(_organization_id, Unset):
            organization_id = UNSET
        else:
            organization_id = UUID(_organization_id)

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        dynamic_rules = d.pop("dynamic_rules", UNSET)

        def _parse_keycloak_group_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        keycloak_group_id = _parse_keycloak_group_id(d.pop("keycloak_group_id", UNSET))

        patched_contact_group_request = cls(
            name=name,
            kind=kind,
            organization_id=organization_id,
            email=email,
            dynamic_rules=dynamic_rules,
            keycloak_group_id=keycloak_group_id,
        )

        patched_contact_group_request.additional_properties = d
        return patched_contact_group_request

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
