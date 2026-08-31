from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contact_role_enum import ContactRoleEnum, check_contact_role_enum
from ..models.generic_object_kind_enum import GenericObjectKindEnum, check_generic_object_kind_enum

T = TypeVar("T", bound="ContactSimple")


@_attrs_define
class ContactSimple:
    """Simple Contact serializer for nested representations.

    Includes `url` field for direct navigation.

        Attributes:
            id (UUID):
            name (str):
            full_name (str): Get formatted full name.
            email (str): Email address of the contact
            phone (None | str): Phone number of the contact
            kind (GenericObjectKindEnum): * `generic` - Generic
            contact_role (ContactRoleEnum): * `developer` - Developer
                * `admin` - Admin
                * `billing` - Billing
                * `viewer` - Viewer
            url (str): Return absolute URL for the contact.
    """

    id: UUID
    name: str
    full_name: str
    email: str
    phone: None | str
    kind: GenericObjectKindEnum
    contact_role: ContactRoleEnum
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        full_name = self.full_name

        email = self.email

        phone: None | str
        phone = self.phone

        kind: str = self.kind

        contact_role: str = self.contact_role

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "full_name": full_name,
                "email": email,
                "phone": phone,
                "kind": kind,
                "contact_role": contact_role,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        full_name = d.pop("full_name")

        email = d.pop("email")

        def _parse_phone(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        phone = _parse_phone(d.pop("phone"))

        kind = check_generic_object_kind_enum(d.pop("kind"))

        contact_role = check_contact_role_enum(d.pop("contact_role"))

        url = d.pop("url")

        contact_simple = cls(
            id=id,
            name=name,
            full_name=full_name,
            email=email,
            phone=phone,
            kind=kind,
            contact_role=contact_role,
            url=url,
        )

        contact_simple.additional_properties = d
        return contact_simple

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
