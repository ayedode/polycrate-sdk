from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.user_membership import UserMembership


T = TypeVar("T", bound="UserDetail")


@_attrs_define
class UserDetail:
    """Portal-facing user detail/create response.

    Includes keycloak_user_id (read-only), contact flags, and memberships with role.
    Spec: polycrate spec inspect 525

        Attributes:
            id (int):
            uuid (UUID):
            email (str):
            first_name (str):
            last_name (str):
            keycloak_user_id (str): Keycloak user UUID set by Polycrate provisioning (never writable)
            is_maintenance_contact (bool): Receive maintenance notifications (default: false)
            is_billing_contact (bool): Receive billing notifications (default: false)
            email_verified (bool): Whether the email is verified. Polycrate is SoT; synced to Keycloak. Spec 561.
            is_active (bool): Active flag (synced to Keycloak enabled on admin PATCH). Spec 561.
            memberships (list[UserMembership]): Organization memberships with organization_id and role
    """

    id: int
    uuid: UUID
    email: str
    first_name: str
    last_name: str
    keycloak_user_id: str
    is_maintenance_contact: bool
    is_billing_contact: bool
    email_verified: bool
    is_active: bool
    memberships: list[UserMembership]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = str(self.uuid)

        email = self.email

        first_name = self.first_name

        last_name = self.last_name

        keycloak_user_id = self.keycloak_user_id

        is_maintenance_contact = self.is_maintenance_contact

        is_billing_contact = self.is_billing_contact

        email_verified = self.email_verified

        is_active = self.is_active

        memberships = []
        for memberships_item_data in self.memberships:
            memberships_item = memberships_item_data.to_dict()
            memberships.append(memberships_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "uuid": uuid,
                "email": email,
                "first_name": first_name,
                "last_name": last_name,
                "keycloak_user_id": keycloak_user_id,
                "is_maintenance_contact": is_maintenance_contact,
                "is_billing_contact": is_billing_contact,
                "email_verified": email_verified,
                "is_active": is_active,
                "memberships": memberships,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_membership import UserMembership  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        uuid = UUID(d.pop("uuid"))

        email = d.pop("email")

        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        keycloak_user_id = d.pop("keycloak_user_id")

        is_maintenance_contact = d.pop("is_maintenance_contact")

        is_billing_contact = d.pop("is_billing_contact")

        email_verified = d.pop("email_verified")

        is_active = d.pop("is_active")

        memberships = []
        _memberships = d.pop("memberships")
        for memberships_item_data in _memberships:
            memberships_item = UserMembership.from_dict(memberships_item_data)

            memberships.append(memberships_item)

        user_detail = cls(
            id=id,
            uuid=uuid,
            email=email,
            first_name=first_name,
            last_name=last_name,
            keycloak_user_id=keycloak_user_id,
            is_maintenance_contact=is_maintenance_contact,
            is_billing_contact=is_billing_contact,
            email_verified=email_verified,
            is_active=is_active,
            memberships=memberships,
        )

        user_detail.additional_properties = d
        return user_detail

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
