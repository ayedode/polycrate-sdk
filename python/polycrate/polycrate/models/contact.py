from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contact_contact_role import ContactContactRole, check_contact_contact_role
from ..models.contact_kind import ContactKind, check_contact_kind
from ..models.contact_state import ContactState, check_contact_state
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.credential_simple import CredentialSimple
    from ..models.organization_simple import OrganizationSimple


T = TypeVar("T", bound="Contact")


@_attrs_define
class Contact:
    """Full serializer for Contact detail views and CRUD operations.

    Includes complete related object data and computed fields.

        Attributes:
            id (UUID):
            name (str):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            state (ContactState): * `OK` - Ok
                * `WARNING` - Warning
                * `CRITICAL` - Critical
                * `READY` - Ready
                * `DEGRADED` - Degraded
                * `DOWN` - Down
            conditions (Any): Conditions are managed by the API and will be added during the reconcile phase. Some
                conditions are `degrading`, meaning an object becomes DEGRADED if it has such a condition.
            organization (OrganizationSimple): Simple Organization serializer for nested representations.

                Includes `url` field for direct navigation.
            credential (CredentialSimple): Simple serializer for embedding Credential in other serializers.
            firstname (str): First name of the contact
            lastname (str): Last name of the contact
            full_name (str):
            email (str): Email address of the contact
            kind (ContactKind | Unset): Type of contact

                * `generic` - Generic
            phone (None | str | Unset): Phone number of the contact
            address (None | str | Unset): Address of the contact
            city (None | str | Unset): City of the contact
            country (None | str | Unset): Country of the contact
            zipcode (None | str | Unset): Zipcode of the contact
            note (None | str | Unset): Note about the contact
            contact_role (ContactContactRole | Unset): Role of the contact (Developer, Admin, Billing, Viewer)

                * `developer` - Developer
                * `admin` - Admin
                * `billing` - Billing
                * `viewer` - Viewer
            is_maintenance_contact (bool | Unset): Whether this contact should receive maintenance notifications
            is_billing_contact (bool | Unset): Whether this contact should receive billing notifications
            keycloak_user_id (None | str | Unset): Keycloak user ID for automatic synchronization
            sync_source (None | str | Unset): Source of automatic synchronization (e.g., 'keycloak', 'ldap')
            last_sync_at (datetime.datetime | None | Unset): When this contact was last synchronized from external source
    """

    id: UUID
    name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    state: ContactState
    conditions: Any
    organization: OrganizationSimple
    credential: CredentialSimple
    firstname: str
    lastname: str
    full_name: str
    email: str
    kind: ContactKind | Unset = UNSET
    phone: None | str | Unset = UNSET
    address: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
    country: None | str | Unset = UNSET
    zipcode: None | str | Unset = UNSET
    note: None | str | Unset = UNSET
    contact_role: ContactContactRole | Unset = UNSET
    is_maintenance_contact: bool | Unset = UNSET
    is_billing_contact: bool | Unset = UNSET
    keycloak_user_id: None | str | Unset = UNSET
    sync_source: None | str | Unset = UNSET
    last_sync_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        state: str = self.state

        conditions = self.conditions

        organization = self.organization.to_dict()

        credential = self.credential.to_dict()

        firstname = self.firstname

        lastname = self.lastname

        full_name = self.full_name

        email = self.email

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        zipcode: None | str | Unset
        if isinstance(self.zipcode, Unset):
            zipcode = UNSET
        else:
            zipcode = self.zipcode

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        contact_role: str | Unset = UNSET
        if not isinstance(self.contact_role, Unset):
            contact_role = self.contact_role

        is_maintenance_contact = self.is_maintenance_contact

        is_billing_contact = self.is_billing_contact

        keycloak_user_id: None | str | Unset
        if isinstance(self.keycloak_user_id, Unset):
            keycloak_user_id = UNSET
        else:
            keycloak_user_id = self.keycloak_user_id

        sync_source: None | str | Unset
        if isinstance(self.sync_source, Unset):
            sync_source = UNSET
        else:
            sync_source = self.sync_source

        last_sync_at: None | str | Unset
        if isinstance(self.last_sync_at, Unset):
            last_sync_at = UNSET
        elif isinstance(self.last_sync_at, datetime.datetime):
            last_sync_at = self.last_sync_at.isoformat()
        else:
            last_sync_at = self.last_sync_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "created_at": created_at,
                "updated_at": updated_at,
                "state": state,
                "conditions": conditions,
                "organization": organization,
                "credential": credential,
                "firstname": firstname,
                "lastname": lastname,
                "full_name": full_name,
                "email": email,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if phone is not UNSET:
            field_dict["phone"] = phone
        if address is not UNSET:
            field_dict["address"] = address
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if zipcode is not UNSET:
            field_dict["zipcode"] = zipcode
        if note is not UNSET:
            field_dict["note"] = note
        if contact_role is not UNSET:
            field_dict["contact_role"] = contact_role
        if is_maintenance_contact is not UNSET:
            field_dict["is_maintenance_contact"] = is_maintenance_contact
        if is_billing_contact is not UNSET:
            field_dict["is_billing_contact"] = is_billing_contact
        if keycloak_user_id is not UNSET:
            field_dict["keycloak_user_id"] = keycloak_user_id
        if sync_source is not UNSET:
            field_dict["sync_source"] = sync_source
        if last_sync_at is not UNSET:
            field_dict["last_sync_at"] = last_sync_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credential_simple import CredentialSimple  # noqa: PLC0415
        from ..models.organization_simple import OrganizationSimple  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        state = check_contact_state(d.pop("state"))

        conditions = d.pop("conditions")

        organization = OrganizationSimple.from_dict(d.pop("organization"))

        credential = CredentialSimple.from_dict(d.pop("credential"))

        firstname = d.pop("firstname")

        lastname = d.pop("lastname")

        full_name = d.pop("full_name")

        email = d.pop("email")

        _kind = d.pop("kind", UNSET)
        kind: ContactKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_contact_kind(_kind)

        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("phone", UNSET))

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))

        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))

        def _parse_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country = _parse_country(d.pop("country", UNSET))

        def _parse_zipcode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        zipcode = _parse_zipcode(d.pop("zipcode", UNSET))

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        _contact_role = d.pop("contact_role", UNSET)
        contact_role: ContactContactRole | Unset
        if isinstance(_contact_role, Unset):
            contact_role = UNSET
        else:
            contact_role = check_contact_contact_role(_contact_role)

        is_maintenance_contact = d.pop("is_maintenance_contact", UNSET)

        is_billing_contact = d.pop("is_billing_contact", UNSET)

        def _parse_keycloak_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        keycloak_user_id = _parse_keycloak_user_id(d.pop("keycloak_user_id", UNSET))

        def _parse_sync_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sync_source = _parse_sync_source(d.pop("sync_source", UNSET))

        def _parse_last_sync_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_sync_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_sync_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_sync_at = _parse_last_sync_at(d.pop("last_sync_at", UNSET))

        contact = cls(
            id=id,
            name=name,
            created_at=created_at,
            updated_at=updated_at,
            state=state,
            conditions=conditions,
            organization=organization,
            credential=credential,
            firstname=firstname,
            lastname=lastname,
            full_name=full_name,
            email=email,
            kind=kind,
            phone=phone,
            address=address,
            city=city,
            country=country,
            zipcode=zipcode,
            note=note,
            contact_role=contact_role,
            is_maintenance_contact=is_maintenance_contact,
            is_billing_contact=is_billing_contact,
            keycloak_user_id=keycloak_user_id,
            sync_source=sync_source,
            last_sync_at=last_sync_at,
        )

        contact.additional_properties = d
        return contact

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
