from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.permissions_enum import PermissionsEnum, check_permissions_enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="S3CredentialCreateRequest")


@_attrs_define
class S3CredentialCreateRequest:
    """Serializer für Access Key Erstellung

    Attributes:
        description (str): Beschreibung für den Access Key
        permissions (PermissionsEnum | Unset): * `read` - read
            * `write` - write
            * `readwrite` - readwrite
            * `full` - full Default: 'full'.
    """

    description: str
    permissions: PermissionsEnum | Unset = "full"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        permissions: str | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
            }
        )
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("description", (None, str(self.description).encode(), "text/plain")))

        if not isinstance(self.permissions, Unset):
            files.append(("permissions", (None, str(self.permissions).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description")

        _permissions = d.pop("permissions", UNSET)
        permissions: PermissionsEnum | Unset
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = check_permissions_enum(_permissions)

        s3_credential_create_request = cls(
            description=description,
            permissions=permissions,
        )

        s3_credential_create_request.additional_properties = d
        return s3_credential_create_request

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
