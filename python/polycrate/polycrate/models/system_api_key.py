from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.access_mode_enum import AccessModeEnum, check_access_mode_enum
from ..models.blank_enum import BlankEnum, check_blank_enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="SystemAPIKey")


@_attrs_define
class SystemAPIKey:
    """Serializer for System API Keys (kind='system_api_key').
    token is only included on create (write-once).
    Spec 488: System and Organization API Keys

        Attributes:
            id (UUID):
            name (str):
            created_at (datetime.datetime):
            last_used_at (datetime.datetime | None): Timestamp of the last successful authentication using this credential.
            token (None | str): Return raw token only on create (stored in context by view).
            organization_name (None | str):
            access_mode (AccessModeEnum | BlankEnum | None | Unset): Access mode for system_api_key and org_api_key
                credentials. Ignored for other kinds.

                * `read` - Read
                * `read_write` - Read/Write
    """

    id: UUID
    name: str
    created_at: datetime.datetime
    last_used_at: datetime.datetime | None
    token: None | str
    organization_name: None | str
    access_mode: AccessModeEnum | BlankEnum | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        created_at = self.created_at.isoformat()

        last_used_at: None | str
        if isinstance(self.last_used_at, datetime.datetime):
            last_used_at = self.last_used_at.isoformat()
        else:
            last_used_at = self.last_used_at

        token: None | str
        token = self.token

        organization_name: None | str
        organization_name = self.organization_name

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
                "id": id,
                "name": name,
                "created_at": created_at,
                "last_used_at": last_used_at,
                "token": token,
                "organization_name": organization_name,
            }
        )
        if access_mode is not UNSET:
            field_dict["access_mode"] = access_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_last_used_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_used_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_used_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_used_at = _parse_last_used_at(d.pop("last_used_at"))

        def _parse_token(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        token = _parse_token(d.pop("token"))

        def _parse_organization_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        organization_name = _parse_organization_name(d.pop("organization_name"))

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

        system_api_key = cls(
            id=id,
            name=name,
            created_at=created_at,
            last_used_at=last_used_at,
            token=token,
            organization_name=organization_name,
            access_mode=access_mode,
        )

        system_api_key.additional_properties = d
        return system_api_key

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
