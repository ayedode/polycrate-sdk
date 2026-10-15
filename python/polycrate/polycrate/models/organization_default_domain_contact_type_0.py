from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrganizationDefaultDomainContactType0")


@_attrs_define
class OrganizationDefaultDomainContactType0:
    """
    Attributes:
        id (UUID | Unset):
        name (str | Unset):
        display_name (str | Unset):
        email (str | Unset):
        kind (str | Unset):
        url (str | Unset):
    """

    id: UUID | Unset = UNSET
    name: str | Unset = UNSET
    display_name: str | Unset = UNSET
    email: str | Unset = UNSET
    kind: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name = self.name

        display_name = self.display_name

        email = self.email

        kind = self.kind

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if email is not UNSET:
            field_dict["email"] = email
        if kind is not UNSET:
            field_dict["kind"] = kind
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        name = d.pop("name", UNSET)

        display_name = d.pop("display_name", UNSET)

        email = d.pop("email", UNSET)

        kind = d.pop("kind", UNSET)

        url = d.pop("url", UNSET)

        organization_default_domain_contact_type_0 = cls(
            id=id,
            name=name,
            display_name=display_name,
            email=email,
            kind=kind,
            url=url,
        )

        organization_default_domain_contact_type_0.additional_properties = d
        return organization_default_domain_contact_type_0

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
