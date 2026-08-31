from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_role_enum import UserRoleEnum, check_user_role_enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="MembershipCreate")


@_attrs_define
class MembershipCreate:
    """Add user to another organization with role. Spec 525

    Attributes:
        organization_id (UUID): Polycrate organization UUID to add the user to
        role (UserRoleEnum | Unset): * `admin` - Admin
            * `developer` - Developer
            * `billing` - Billing
            * `viewer` - Viewer
            * `owner` - Owner Default: 'viewer'.
    """

    organization_id: UUID
    role: UserRoleEnum | Unset = "viewer"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        organization_id = str(self.organization_id)

        role: str | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "organization_id": organization_id,
            }
        )
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        organization_id = UUID(d.pop("organization_id"))

        _role = d.pop("role", UNSET)
        role: UserRoleEnum | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = check_user_role_enum(_role)

        membership_create = cls(
            organization_id=organization_id,
            role=role,
        )

        membership_create.additional_properties = d
        return membership_create

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
