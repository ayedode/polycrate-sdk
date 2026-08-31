from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.access_mode_enum import AccessModeEnum, check_access_mode_enum
from ..models.blank_enum import BlankEnum, check_blank_enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrgAPIKeyRequest")


@_attrs_define
class OrgAPIKeyRequest:
    """Serializer for Organization API Keys (kind='org_api_key').
    token is only included on create (write-once).
    Spec 488: System and Organization API Keys

        Attributes:
            name (str):
            access_mode (AccessModeEnum | BlankEnum | None | Unset): Access mode for system_api_key and org_api_key
                credentials. Ignored for other kinds.

                * `read` - Read
                * `read_write` - Read/Write
    """

    name: str
    access_mode: AccessModeEnum | BlankEnum | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        access_mode: None | str | Unset
        if isinstance(self.access_mode, Unset):
            access_mode = UNSET
        elif isinstance(self.access_mode, str):
            access_mode = self.access_mode
        elif isinstance(self.access_mode, str):
            access_mode = self.access_mode
        else:
            access_mode = self.access_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if access_mode is not UNSET:
            field_dict["access_mode"] = access_mode

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.access_mode, Unset):
            if isinstance(self.access_mode, str):
                files.append(("access_mode", (None, str(self.access_mode).encode(), "text/plain")))
            elif isinstance(self.access_mode, str):
                files.append(("access_mode", (None, str(self.access_mode).encode(), "text/plain")))
            else:
                files.append(("access_mode", (None, str(self.access_mode).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_access_mode(data: object) -> AccessModeEnum | BlankEnum | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                access_mode_type_0 = check_access_mode_enum(data)

                return access_mode_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                access_mode_type_1 = check_blank_enum(data)

                return access_mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AccessModeEnum | BlankEnum | None | Unset, data)

        access_mode = _parse_access_mode(d.pop("access_mode", UNSET))

        org_api_key_request = cls(
            name=name,
            access_mode=access_mode,
        )

        org_api_key_request.additional_properties = d
        return org_api_key_request

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
