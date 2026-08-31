from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.user_role_enum import UserRoleEnum, check_user_role_enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedMembershipRoleUpdateRequest")


@_attrs_define
class PatchedMembershipRoleUpdateRequest:
    """Update org-scoped membership role. Spec 525

    Attributes:
        organization_id (UUID | Unset): Polycrate organization UUID of the membership to update
        role (UserRoleEnum | Unset): * `admin` - Admin
            * `developer` - Developer
            * `billing` - Billing
            * `viewer` - Viewer
            * `owner` - Owner
    """

    organization_id: UUID | Unset = UNSET
    role: UserRoleEnum | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        organization_id: str | Unset = UNSET
        if not isinstance(self.organization_id, Unset):
            organization_id = str(self.organization_id)

        role: str | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if organization_id is not UNSET:
            field_dict["organization_id"] = organization_id
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.organization_id, Unset):
            files.append(("organization_id", (None, str(self.organization_id), "text/plain")))

        if not isinstance(self.role, Unset):
            files.append(("role", (None, str(self.role).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _organization_id = d.pop("organization_id", UNSET)
        organization_id: UUID | Unset
        if isinstance(_organization_id, Unset):
            organization_id = UNSET
        else:
            organization_id = UUID(_organization_id)

        _role = d.pop("role", UNSET)
        role: UserRoleEnum | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = check_user_role_enum(_role)

        patched_membership_role_update_request = cls(
            organization_id=organization_id,
            role=role,
        )

        patched_membership_role_update_request.additional_properties = d
        return patched_membership_role_update_request

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
