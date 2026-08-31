from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.user_role_enum import UserRoleEnum, check_user_role_enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserCreateRequest")


@_attrs_define
class UserCreateRequest:
    """Create a user with organization membership and blocking Keycloak provision.

    Spec: polycrate spec inspect 525

        Attributes:
            email (str): Unique email address (also used as Keycloak username)
            first_name (str): Given name
            last_name (str): Family name
            organization_id (UUID): Polycrate organization UUID; organization must have keycloak_org_id
            role (UserRoleEnum): * `admin` - Admin
                * `developer` - Developer
                * `billing` - Billing
                * `viewer` - Viewer
                * `owner` - Owner
            is_maintenance_contact (bool | Unset): Receive maintenance notifications (default: false) Default: False.
            is_billing_contact (bool | Unset): Receive billing notifications (default: false) Default: False.
            email_verified (bool | Unset): Whether the email is verified (default true). Persisted in Polycrate and synced
                to Keycloak emailVerified. Spec 561. Default: True.
            password (str | Unset): Optional write-only password set in Keycloak after create (prefer POST .../set-password/
                for invite activation)
    """

    email: str
    first_name: str
    last_name: str
    organization_id: UUID
    role: UserRoleEnum
    is_maintenance_contact: bool | Unset = False
    is_billing_contact: bool | Unset = False
    email_verified: bool | Unset = True
    password: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        first_name = self.first_name

        last_name = self.last_name

        organization_id = str(self.organization_id)

        role: str = self.role

        is_maintenance_contact = self.is_maintenance_contact

        is_billing_contact = self.is_billing_contact

        email_verified = self.email_verified

        password = self.password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "first_name": first_name,
                "last_name": last_name,
                "organization_id": organization_id,
                "role": role,
            }
        )
        if is_maintenance_contact is not UNSET:
            field_dict["is_maintenance_contact"] = is_maintenance_contact
        if is_billing_contact is not UNSET:
            field_dict["is_billing_contact"] = is_billing_contact
        if email_verified is not UNSET:
            field_dict["email_verified"] = email_verified
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("email", (None, str(self.email).encode(), "text/plain")))

        files.append(("first_name", (None, str(self.first_name).encode(), "text/plain")))

        files.append(("last_name", (None, str(self.last_name).encode(), "text/plain")))

        files.append(("organization_id", (None, str(self.organization_id), "text/plain")))

        files.append(("role", (None, str(self.role).encode(), "text/plain")))

        if not isinstance(self.is_maintenance_contact, Unset):
            files.append(("is_maintenance_contact", (None, str(self.is_maintenance_contact).encode(), "text/plain")))

        if not isinstance(self.is_billing_contact, Unset):
            files.append(("is_billing_contact", (None, str(self.is_billing_contact).encode(), "text/plain")))

        if not isinstance(self.email_verified, Unset):
            files.append(("email_verified", (None, str(self.email_verified).encode(), "text/plain")))

        if not isinstance(self.password, Unset):
            files.append(("password", (None, str(self.password).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        organization_id = UUID(d.pop("organization_id"))

        role = check_user_role_enum(d.pop("role"))

        is_maintenance_contact = d.pop("is_maintenance_contact", UNSET)

        is_billing_contact = d.pop("is_billing_contact", UNSET)

        email_verified = d.pop("email_verified", UNSET)

        password = d.pop("password", UNSET)

        user_create_request = cls(
            email=email,
            first_name=first_name,
            last_name=last_name,
            organization_id=organization_id,
            role=role,
            is_maintenance_contact=is_maintenance_contact,
            is_billing_contact=is_billing_contact,
            email_verified=email_verified,
            password=password,
        )

        user_create_request.additional_properties = d
        return user_create_request

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
