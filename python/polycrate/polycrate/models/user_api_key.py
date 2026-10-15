from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_api_key_access_mode import UserAPIKeyAccessMode, check_user_api_key_access_mode
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserAPIKey")


@_attrs_define
class UserAPIKey:
    """Knox user API key metadata. token is write-once via context['raw_token'].
    Spec: polycrate spec inspect 868 / 873

        Attributes:
            id (str):
            name (str): User-defined name for this API key (e.g., 'MacBook Pro', 'CI/CD Pipeline')
            created_at (datetime.datetime):
            last_used_at (datetime.datetime | None): Last time this key was used for authentication
            expires_at (datetime.datetime):
            prefix (str):
            is_expired (bool):
            token (None | str): Return raw token only on create (stored in context by the view).
            access_mode (UserAPIKeyAccessMode | Unset): read blocks non-safe HTTP methods; default read_write.

                * `read` - Read
                * `read_write` - Read/Write Default: 'read_write'.
    """

    id: str
    name: str
    created_at: datetime.datetime
    last_used_at: datetime.datetime | None
    expires_at: datetime.datetime
    prefix: str
    is_expired: bool
    token: None | str
    access_mode: UserAPIKeyAccessMode | Unset = "read_write"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        created_at = self.created_at.isoformat()

        last_used_at: None | str
        if isinstance(self.last_used_at, datetime.datetime):
            last_used_at = self.last_used_at.isoformat()
        else:
            last_used_at = self.last_used_at

        expires_at = self.expires_at.isoformat()

        prefix = self.prefix

        is_expired = self.is_expired

        token: None | str
        token = self.token

        access_mode: str | Unset = UNSET
        if not isinstance(self.access_mode, Unset):
            access_mode = self.access_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "created_at": created_at,
                "last_used_at": last_used_at,
                "expires_at": expires_at,
                "prefix": prefix,
                "is_expired": is_expired,
                "token": token,
            }
        )
        if access_mode is not UNSET:
            field_dict["access_mode"] = access_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

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

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        prefix = d.pop("prefix")

        is_expired = d.pop("is_expired")

        def _parse_token(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        token = _parse_token(d.pop("token"))

        _access_mode = d.pop("access_mode", UNSET)
        access_mode: UserAPIKeyAccessMode | Unset
        if isinstance(_access_mode, Unset):
            access_mode = UNSET
        else:
            access_mode = check_user_api_key_access_mode(_access_mode)

        user_api_key = cls(
            id=id,
            name=name,
            created_at=created_at,
            last_used_at=last_used_at,
            expires_at=expires_at,
            prefix=prefix,
            is_expired=is_expired,
            token=token,
            access_mode=access_mode,
        )

        user_api_key.additional_properties = d
        return user_api_key

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
