from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.contact_role_enum import ContactRoleEnum, check_contact_role_enum
from ..models.generic_object_kind_enum import GenericObjectKindEnum, check_generic_object_kind_enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedContactRequest")


@_attrs_define
class PatchedContactRequest:
    """Full serializer for Contact detail views and CRUD operations.

    Includes complete related object data and computed fields.

        Attributes:
            name (str | Unset):
            kind (GenericObjectKindEnum | Unset): * `generic` - Generic
            organization_id (UUID | Unset):
            credential_id (None | Unset | UUID):
            firstname (str | Unset): First name of the contact
            lastname (str | Unset): Last name of the contact
            email (str | Unset): Email address of the contact
            phone (None | str | Unset): Phone number of the contact
            address (None | str | Unset): Address of the contact
            city (None | str | Unset): City of the contact
            country (None | str | Unset): Country of the contact
            zipcode (None | str | Unset): Zipcode of the contact
            note (None | str | Unset): Note about the contact
            contact_role (ContactRoleEnum | Unset): * `developer` - Developer
                * `admin` - Admin
                * `billing` - Billing
                * `viewer` - Viewer
            is_maintenance_contact (bool | Unset): Whether this contact should receive maintenance notifications
            is_billing_contact (bool | Unset): Whether this contact should receive billing notifications
            keycloak_user_id (None | str | Unset): Keycloak user ID for automatic synchronization
            sync_source (None | str | Unset): Source of automatic synchronization (e.g., 'keycloak', 'ldap')
            last_sync_at (datetime.datetime | None | Unset): When this contact was last synchronized from external source
    """

    name: str | Unset = UNSET
    kind: GenericObjectKindEnum | Unset = UNSET
    organization_id: UUID | Unset = UNSET
    credential_id: None | Unset | UUID = UNSET
    firstname: str | Unset = UNSET
    lastname: str | Unset = UNSET
    email: str | Unset = UNSET
    phone: None | str | Unset = UNSET
    address: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
    country: None | str | Unset = UNSET
    zipcode: None | str | Unset = UNSET
    note: None | str | Unset = UNSET
    contact_role: ContactRoleEnum | Unset = UNSET
    is_maintenance_contact: bool | Unset = UNSET
    is_billing_contact: bool | Unset = UNSET
    keycloak_user_id: None | str | Unset = UNSET
    sync_source: None | str | Unset = UNSET
    last_sync_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        organization_id: str | Unset = UNSET
        if not isinstance(self.organization_id, Unset):
            organization_id = str(self.organization_id)

        credential_id: None | str | Unset
        if isinstance(self.credential_id, Unset):
            credential_id = UNSET
        elif isinstance(self.credential_id, UUID):
            credential_id = str(self.credential_id)
        else:
            credential_id = self.credential_id

        firstname = self.firstname

        lastname = self.lastname

        email = self.email

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
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if kind is not UNSET:
            field_dict["kind"] = kind
        if organization_id is not UNSET:
            field_dict["organization_id"] = organization_id
        if credential_id is not UNSET:
            field_dict["credential_id"] = credential_id
        if firstname is not UNSET:
            field_dict["firstname"] = firstname
        if lastname is not UNSET:
            field_dict["lastname"] = lastname
        if email is not UNSET:
            field_dict["email"] = email
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

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.kind, Unset):
            files.append(("kind", (None, str(self.kind).encode(), "text/plain")))

        if not isinstance(self.organization_id, Unset):
            files.append(("organization_id", (None, str(self.organization_id), "text/plain")))

        if not isinstance(self.credential_id, Unset):
            if isinstance(self.credential_id, UUID):
                files.append(("credential_id", (None, str(self.credential_id), "text/plain")))
            else:
                files.append(("credential_id", (None, str(self.credential_id).encode(), "text/plain")))

        if not isinstance(self.firstname, Unset):
            files.append(("firstname", (None, str(self.firstname).encode(), "text/plain")))

        if not isinstance(self.lastname, Unset):
            files.append(("lastname", (None, str(self.lastname).encode(), "text/plain")))

        if not isinstance(self.email, Unset):
            files.append(("email", (None, str(self.email).encode(), "text/plain")))

        if not isinstance(self.phone, Unset):
            if isinstance(self.phone, str):
                files.append(("phone", (None, str(self.phone).encode(), "text/plain")))
            else:
                files.append(("phone", (None, str(self.phone).encode(), "text/plain")))

        if not isinstance(self.address, Unset):
            if isinstance(self.address, str):
                files.append(("address", (None, str(self.address).encode(), "text/plain")))
            else:
                files.append(("address", (None, str(self.address).encode(), "text/plain")))

        if not isinstance(self.city, Unset):
            if isinstance(self.city, str):
                files.append(("city", (None, str(self.city).encode(), "text/plain")))
            else:
                files.append(("city", (None, str(self.city).encode(), "text/plain")))

        if not isinstance(self.country, Unset):
            if isinstance(self.country, str):
                files.append(("country", (None, str(self.country).encode(), "text/plain")))
            else:
                files.append(("country", (None, str(self.country).encode(), "text/plain")))

        if not isinstance(self.zipcode, Unset):
            if isinstance(self.zipcode, str):
                files.append(("zipcode", (None, str(self.zipcode).encode(), "text/plain")))
            else:
                files.append(("zipcode", (None, str(self.zipcode).encode(), "text/plain")))

        if not isinstance(self.note, Unset):
            if isinstance(self.note, str):
                files.append(("note", (None, str(self.note).encode(), "text/plain")))
            else:
                files.append(("note", (None, str(self.note).encode(), "text/plain")))

        if not isinstance(self.contact_role, Unset):
            files.append(("contact_role", (None, str(self.contact_role).encode(), "text/plain")))

        if not isinstance(self.is_maintenance_contact, Unset):
            files.append(("is_maintenance_contact", (None, str(self.is_maintenance_contact).encode(), "text/plain")))

        if not isinstance(self.is_billing_contact, Unset):
            files.append(("is_billing_contact", (None, str(self.is_billing_contact).encode(), "text/plain")))

        if not isinstance(self.keycloak_user_id, Unset):
            if isinstance(self.keycloak_user_id, str):
                files.append(("keycloak_user_id", (None, str(self.keycloak_user_id).encode(), "text/plain")))
            else:
                files.append(("keycloak_user_id", (None, str(self.keycloak_user_id).encode(), "text/plain")))

        if not isinstance(self.sync_source, Unset):
            if isinstance(self.sync_source, str):
                files.append(("sync_source", (None, str(self.sync_source).encode(), "text/plain")))
            else:
                files.append(("sync_source", (None, str(self.sync_source).encode(), "text/plain")))

        if not isinstance(self.last_sync_at, Unset):
            if isinstance(self.last_sync_at, datetime.datetime):
                files.append(("last_sync_at", (None, self.last_sync_at.isoformat().encode(), "text/plain")))
            else:
                files.append(("last_sync_at", (None, str(self.last_sync_at).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: GenericObjectKindEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_generic_object_kind_enum(_kind)

        _organization_id = d.pop("organization_id", UNSET)
        organization_id: UUID | Unset
        if isinstance(_organization_id, Unset):
            organization_id = UNSET
        else:
            organization_id = UUID(_organization_id)

        def _parse_credential_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                credential_id_type_0 = UUID(data)

                return credential_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        credential_id = _parse_credential_id(d.pop("credential_id", UNSET))

        firstname = d.pop("firstname", UNSET)

        lastname = d.pop("lastname", UNSET)

        email = d.pop("email", UNSET)

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
        contact_role: ContactRoleEnum | Unset
        if isinstance(_contact_role, Unset):
            contact_role = UNSET
        else:
            contact_role = check_contact_role_enum(_contact_role)

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

        patched_contact_request = cls(
            name=name,
            kind=kind,
            organization_id=organization_id,
            credential_id=credential_id,
            firstname=firstname,
            lastname=lastname,
            email=email,
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

        patched_contact_request.additional_properties = d
        return patched_contact_request

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
