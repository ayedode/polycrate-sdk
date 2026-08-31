from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contact_group_membership_role_enum import (
    ContactGroupMembershipRoleEnum,
    check_contact_group_membership_role_enum,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactGroupMembershipRequest")


@_attrs_define
class ContactGroupMembershipRequest:
    """Serializer for ContactGroupMembership through table.

    Used for managing contact-group relationships with roles.

        Attributes:
            contact (UUID):
            role (ContactGroupMembershipRoleEnum | Unset): * `owner` - Owner
                * `maintainer` - Maintainer
                * `contributor` - Contributor
    """

    contact: UUID
    role: ContactGroupMembershipRoleEnum | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contact = str(self.contact)

        role: str | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contact": contact,
            }
        )
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        contact = UUID(d.pop("contact"))

        _role = d.pop("role", UNSET)
        role: ContactGroupMembershipRoleEnum | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = check_contact_group_membership_role_enum(_role)

        contact_group_membership_request = cls(
            contact=contact,
            role=role,
        )

        contact_group_membership_request.additional_properties = d
        return contact_group_membership_request

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
