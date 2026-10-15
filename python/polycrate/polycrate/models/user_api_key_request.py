from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.user_api_key_request_access_mode import (
    UserAPIKeyRequestAccessMode,
    check_user_api_key_request_access_mode,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserAPIKeyRequest")


@_attrs_define
class UserAPIKeyRequest:
    """Knox user API key metadata. token is write-once via context['raw_token'].
    Spec: polycrate spec inspect 868 / 873

        Attributes:
            name (str): User-defined name for this API key (e.g., 'MacBook Pro', 'CI/CD Pipeline')
            access_mode (UserAPIKeyRequestAccessMode | Unset): read blocks non-safe HTTP methods; default read_write.

                * `read` - Read
                * `read_write` - Read/Write Default: 'read_write'.
            expires_in_days (int | Unset): Optional expiry in days (>= 1). Omit for no expiration.
    """

    name: str
    access_mode: UserAPIKeyRequestAccessMode | Unset = "read_write"
    expires_in_days: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        access_mode: str | Unset = UNSET
        if not isinstance(self.access_mode, Unset):
            access_mode = self.access_mode

        expires_in_days = self.expires_in_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if access_mode is not UNSET:
            field_dict["access_mode"] = access_mode
        if expires_in_days is not UNSET:
            field_dict["expires_in_days"] = expires_in_days

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.access_mode, Unset):
            files.append(("access_mode", (None, str(self.access_mode).encode(), "text/plain")))

        if not isinstance(self.expires_in_days, Unset):
            files.append(("expires_in_days", (None, str(self.expires_in_days).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        _access_mode = d.pop("access_mode", UNSET)
        access_mode: UserAPIKeyRequestAccessMode | Unset
        if isinstance(_access_mode, Unset):
            access_mode = UNSET
        else:
            access_mode = check_user_api_key_request_access_mode(_access_mode)

        expires_in_days = d.pop("expires_in_days", UNSET)

        user_api_key_request = cls(
            name=name,
            access_mode=access_mode,
            expires_in_days=expires_in_days,
        )

        user_api_key_request.additional_properties = d
        return user_api_key_request

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
