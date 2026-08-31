from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedUserFlagsUpdateRequest")


@_attrs_define
class PatchedUserFlagsUpdateRequest:
    """Partial update for contact notification flags. Spec 525

    Attributes:
        is_maintenance_contact (bool | Unset): Receive maintenance notifications (default: false)
        is_billing_contact (bool | Unset): Receive billing notifications (default: false)
        first_name (str | Unset):
        last_name (str | Unset):
    """

    is_maintenance_contact: bool | Unset = UNSET
    is_billing_contact: bool | Unset = UNSET
    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_maintenance_contact = self.is_maintenance_contact

        is_billing_contact = self.is_billing_contact

        first_name = self.first_name

        last_name = self.last_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_maintenance_contact is not UNSET:
            field_dict["is_maintenance_contact"] = is_maintenance_contact
        if is_billing_contact is not UNSET:
            field_dict["is_billing_contact"] = is_billing_contact
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.is_maintenance_contact, Unset):
            files.append(("is_maintenance_contact", (None, str(self.is_maintenance_contact).encode(), "text/plain")))

        if not isinstance(self.is_billing_contact, Unset):
            files.append(("is_billing_contact", (None, str(self.is_billing_contact).encode(), "text/plain")))

        if not isinstance(self.first_name, Unset):
            files.append(("first_name", (None, str(self.first_name).encode(), "text/plain")))

        if not isinstance(self.last_name, Unset):
            files.append(("last_name", (None, str(self.last_name).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_maintenance_contact = d.pop("is_maintenance_contact", UNSET)

        is_billing_contact = d.pop("is_billing_contact", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        patched_user_flags_update_request = cls(
            is_maintenance_contact=is_maintenance_contact,
            is_billing_contact=is_billing_contact,
            first_name=first_name,
            last_name=last_name,
        )

        patched_user_flags_update_request.additional_properties = d
        return patched_user_flags_update_request

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
