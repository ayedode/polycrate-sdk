from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_role_enum import UserRoleEnum, check_user_role_enum

T = TypeVar("T", bound="MembershipRoleUpdate")


@_attrs_define
class MembershipRoleUpdate:
    """Update org-scoped membership role. Spec 525

    Attributes:
        organization_id (UUID): Polycrate organization UUID of the membership to update
        role (UserRoleEnum): * `admin` - Admin
            * `developer` - Developer
            * `billing` - Billing
            * `viewer` - Viewer
            * `owner` - Owner
    """

    organization_id: UUID
    role: UserRoleEnum
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        organization_id = str(self.organization_id)

        role: str = self.role

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "organization_id": organization_id,
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        organization_id = UUID(d.pop("organization_id"))

        role = check_user_role_enum(d.pop("role"))

        membership_role_update = cls(
            organization_id=organization_id,
            role=role,
        )

        membership_role_update.additional_properties = d
        return membership_role_update

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
