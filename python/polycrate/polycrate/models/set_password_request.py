from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="SetPasswordRequest")


@_attrs_define
class SetPasswordRequest:
    """Set or reset Keycloak password. Spec 525

    Attributes:
        password (str): New password (write-only; never returned in responses or logs)
        temporary (bool | Unset): If true, Keycloak requires the user to change the password on next login. Default
            false = final password (invite activation). Default: False.
    """

    password: str
    temporary: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        password = self.password

        temporary = self.temporary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "password": password,
            }
        )
        if temporary is not UNSET:
            field_dict["temporary"] = temporary

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("password", (None, str(self.password).encode(), "text/plain")))

        if not isinstance(self.temporary, Unset):
            files.append(("temporary", (None, str(self.temporary).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        password = d.pop("password")

        temporary = d.pop("temporary", UNSET)

        set_password_request = cls(
            password=password,
            temporary=temporary,
        )

        set_password_request.additional_properties = d
        return set_password_request

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
