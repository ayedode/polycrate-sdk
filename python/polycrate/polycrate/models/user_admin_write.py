from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.blank_enum import BlankEnum, check_blank_enum
from ..models.user_role_enum import UserRoleEnum, check_user_role_enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserAdminWrite")


@_attrs_define
class UserAdminWrite:
    """Writable serializer for admin user CRUD.

    keycloak_user_id is intentionally omitted (read-only / provision-managed).
    Spec: polycrate spec inspect 131 / 525

        Attributes:
            id (int):
            email (str):
            first_name (str | Unset):
            last_name (str | Unset):
            is_active (bool | Unset): Active flag. Synced to Keycloak enabled on change (blocking). Spec 561.
            is_staff (bool | Unset):
            is_superuser (bool | Unset): Designates that this user has all permissions without explicitly assigning them.
            role (BlankEnum | None | Unset | UserRoleEnum): Legacy system-wide role (developer, admin, billing, viewer,
                owner). Prefer OrganizationMembership.role for org-scoped portal roles (Spec 525).

                * `developer` - Developer
                * `admin` - Admin
                * `billing` - Billing
                * `viewer` - Viewer
                * `owner` - Owner
            is_maintenance_contact (bool | Unset): Receive maintenance notifications (default: false)
            is_billing_contact (bool | Unset): Receive billing notifications (default: false)
            email_verified (bool | Unset): Whether the email is verified. Synced to Keycloak emailVerified. Spec 561.
    """

    id: int
    email: str
    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    is_active: bool | Unset = UNSET
    is_staff: bool | Unset = UNSET
    is_superuser: bool | Unset = UNSET
    role: BlankEnum | None | Unset | UserRoleEnum = UNSET
    is_maintenance_contact: bool | Unset = UNSET
    is_billing_contact: bool | Unset = UNSET
    email_verified: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        email = self.email

        first_name = self.first_name

        last_name = self.last_name

        is_active = self.is_active

        is_staff = self.is_staff

        is_superuser = self.is_superuser

        role: None | str | Unset
        if isinstance(self.role, Unset):
            role = UNSET
        elif isinstance(self.role, str):
            role = self.role
        elif isinstance(self.role, str):
            role = self.role
        else:
            role = self.role

        is_maintenance_contact = self.is_maintenance_contact

        is_billing_contact = self.is_billing_contact

        email_verified = self.email_verified

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "email": email,
            }
        )
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if is_staff is not UNSET:
            field_dict["is_staff"] = is_staff
        if is_superuser is not UNSET:
            field_dict["is_superuser"] = is_superuser
        if role is not UNSET:
            field_dict["role"] = role
        if is_maintenance_contact is not UNSET:
            field_dict["is_maintenance_contact"] = is_maintenance_contact
        if is_billing_contact is not UNSET:
            field_dict["is_billing_contact"] = is_billing_contact
        if email_verified is not UNSET:
            field_dict["email_verified"] = email_verified

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        email = d.pop("email")

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        is_active = d.pop("is_active", UNSET)

        is_staff = d.pop("is_staff", UNSET)

        is_superuser = d.pop("is_superuser", UNSET)

        def _parse_role(data: object) -> BlankEnum | None | Unset | UserRoleEnum:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                role_type_0 = check_user_role_enum(data)

                return role_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                role_type_1 = check_blank_enum(data)

                return role_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlankEnum | None | Unset | UserRoleEnum, data)

        role = _parse_role(d.pop("role", UNSET))

        is_maintenance_contact = d.pop("is_maintenance_contact", UNSET)

        is_billing_contact = d.pop("is_billing_contact", UNSET)

        email_verified = d.pop("email_verified", UNSET)

        user_admin_write = cls(
            id=id,
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_active=is_active,
            is_staff=is_staff,
            is_superuser=is_superuser,
            role=role,
            is_maintenance_contact=is_maintenance_contact,
            is_billing_contact=is_billing_contact,
            email_verified=email_verified,
        )

        user_admin_write.additional_properties = d
        return user_admin_write

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
