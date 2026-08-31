from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_role_enum import UserRoleEnum, check_user_role_enum

if TYPE_CHECKING:
    from ..models.user_admin_organizations import UserAdminOrganizations


T = TypeVar("T", bound="UserAdmin")


@_attrs_define
class UserAdmin:
    """Extended user serializer for admin API.
    Spec: polycrate spec inspect 127

        Attributes:
            id (int):
            uuid (UUID):
            email (str):
            first_name (str):
            last_name (str):
            display_name (str):
            is_active (bool):
            is_staff (bool):
            is_superuser (bool): Designates that this user has all permissions without explicitly assigning them.
            role (None | UserRoleEnum): Legacy system-wide role (developer, admin, billing, viewer, owner). Prefer
                OrganizationMembership.role for org-scoped portal roles (Spec 525).

                * `developer` - Developer
                * `admin` - Admin
                * `billing` - Billing
                * `viewer` - Viewer
                * `owner` - Owner
            keycloak_user_id (None | str): Keycloak user ID, migrated from Contact or resolved via Keycloak API
            grafana_user_id (int | None): Platform Grafana user ID (global, not org-specific). Set during org user sync.
            migrated_from_contact (None | UUID): Reference to the Contact this user was migrated from
            is_maintenance_contact (bool): Receive maintenance notifications for organizations this user belongs to
            is_billing_contact (bool): Receive billing notifications for organizations this user belongs to
            email_verified (bool): Whether the email is verified. Polycrate is SoT; value reflects last successful
                write/sync to Keycloak (not a live Keycloak read). Spec 561.
            date_joined (datetime.datetime):
            last_login (datetime.datetime | None):
            membership_joined_at (datetime.datetime):
            organizations (UserAdminOrganizations):
            has_social_account (bool):
    """

    id: int
    uuid: UUID
    email: str
    first_name: str
    last_name: str
    display_name: str
    is_active: bool
    is_staff: bool
    is_superuser: bool
    role: None | UserRoleEnum
    keycloak_user_id: None | str
    grafana_user_id: int | None
    migrated_from_contact: None | UUID
    is_maintenance_contact: bool
    is_billing_contact: bool
    email_verified: bool
    date_joined: datetime.datetime
    last_login: datetime.datetime | None
    membership_joined_at: datetime.datetime
    organizations: UserAdminOrganizations
    has_social_account: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = str(self.uuid)

        email = self.email

        first_name = self.first_name

        last_name = self.last_name

        display_name = self.display_name

        is_active = self.is_active

        is_staff = self.is_staff

        is_superuser = self.is_superuser

        role: None | str
        if isinstance(self.role, str):
            role = self.role
        else:
            role = self.role

        keycloak_user_id: None | str
        keycloak_user_id = self.keycloak_user_id

        grafana_user_id: int | None
        grafana_user_id = self.grafana_user_id

        migrated_from_contact: None | str
        if isinstance(self.migrated_from_contact, UUID):
            migrated_from_contact = str(self.migrated_from_contact)
        else:
            migrated_from_contact = self.migrated_from_contact

        is_maintenance_contact = self.is_maintenance_contact

        is_billing_contact = self.is_billing_contact

        email_verified = self.email_verified

        date_joined = self.date_joined.isoformat()

        last_login: None | str
        if isinstance(self.last_login, datetime.datetime):
            last_login = self.last_login.isoformat()
        else:
            last_login = self.last_login

        membership_joined_at = self.membership_joined_at.isoformat()

        organizations = self.organizations.to_dict()

        has_social_account = self.has_social_account

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "uuid": uuid,
                "email": email,
                "first_name": first_name,
                "last_name": last_name,
                "display_name": display_name,
                "is_active": is_active,
                "is_staff": is_staff,
                "is_superuser": is_superuser,
                "role": role,
                "keycloak_user_id": keycloak_user_id,
                "grafana_user_id": grafana_user_id,
                "migrated_from_contact": migrated_from_contact,
                "is_maintenance_contact": is_maintenance_contact,
                "is_billing_contact": is_billing_contact,
                "email_verified": email_verified,
                "date_joined": date_joined,
                "last_login": last_login,
                "membership_joined_at": membership_joined_at,
                "organizations": organizations,
                "has_social_account": has_social_account,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_admin_organizations import UserAdminOrganizations

        d = dict(src_dict)
        id = d.pop("id")

        uuid = UUID(d.pop("uuid"))

        email = d.pop("email")

        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        display_name = d.pop("display_name")

        is_active = d.pop("is_active")

        is_staff = d.pop("is_staff")

        is_superuser = d.pop("is_superuser")

        def _parse_role(data: object) -> None | UserRoleEnum:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                role_type_0 = check_user_role_enum(data)

                return role_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UserRoleEnum, data)

        role = _parse_role(d.pop("role"))

        def _parse_keycloak_user_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        keycloak_user_id = _parse_keycloak_user_id(d.pop("keycloak_user_id"))

        def _parse_grafana_user_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        grafana_user_id = _parse_grafana_user_id(d.pop("grafana_user_id"))

        def _parse_migrated_from_contact(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                migrated_from_contact_type_0 = UUID(data)

                return migrated_from_contact_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        migrated_from_contact = _parse_migrated_from_contact(d.pop("migrated_from_contact"))

        is_maintenance_contact = d.pop("is_maintenance_contact")

        is_billing_contact = d.pop("is_billing_contact")

        email_verified = d.pop("email_verified")

        date_joined = datetime.datetime.fromisoformat(d.pop("date_joined"))

        def _parse_last_login(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_login_type_0 = datetime.datetime.fromisoformat(data)

                return last_login_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_login = _parse_last_login(d.pop("last_login"))

        membership_joined_at = datetime.datetime.fromisoformat(d.pop("membership_joined_at"))

        organizations = UserAdminOrganizations.from_dict(d.pop("organizations"))

        has_social_account = d.pop("has_social_account")

        user_admin = cls(
            id=id,
            uuid=uuid,
            email=email,
            first_name=first_name,
            last_name=last_name,
            display_name=display_name,
            is_active=is_active,
            is_staff=is_staff,
            is_superuser=is_superuser,
            role=role,
            keycloak_user_id=keycloak_user_id,
            grafana_user_id=grafana_user_id,
            migrated_from_contact=migrated_from_contact,
            is_maintenance_contact=is_maintenance_contact,
            is_billing_contact=is_billing_contact,
            email_verified=email_verified,
            date_joined=date_joined,
            last_login=last_login,
            membership_joined_at=membership_joined_at,
            organizations=organizations,
            has_social_account=has_social_account,
        )

        user_admin.additional_properties = d
        return user_admin

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
