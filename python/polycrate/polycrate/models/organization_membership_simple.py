from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OrganizationMembershipSimple")


@_attrs_define
class OrganizationMembershipSimple:
    """Simple read-only serializer for OrganizationMembership — used in workspace/org owner field.

    Attributes:
        id (int):
        user_id (UUID):
        email (str):
        full_name (str):
        role (str): Organization-scoped role: admin, developer, billing, viewer, or owner
        date_joined (datetime.datetime):
    """

    id: int
    user_id: UUID
    email: str
    full_name: str
    role: str
    date_joined: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_id = str(self.user_id)

        email = self.email

        full_name = self.full_name

        role = self.role

        date_joined = self.date_joined.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user_id": user_id,
                "email": email,
                "full_name": full_name,
                "role": role,
                "date_joined": date_joined,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        user_id = UUID(d.pop("user_id"))

        email = d.pop("email")

        full_name = d.pop("full_name")

        role = d.pop("role")

        date_joined = datetime.datetime.fromisoformat(d.pop("date_joined"))

        organization_membership_simple = cls(
            id=id,
            user_id=user_id,
            email=email,
            full_name=full_name,
            role=role,
            date_joined=date_joined,
        )

        organization_membership_simple.additional_properties = d
        return organization_membership_simple

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
