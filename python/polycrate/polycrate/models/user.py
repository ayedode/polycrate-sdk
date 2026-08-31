from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """User serializer for API responses.

    Per .specs/0.11.12/milkdown-mention-plugin.md:
    - Read-only fields only
    - No sensitive data (password, is_superuser, is_staff, etc.)
    - avatar_url for mention rendering
    - display_name for user-friendly display
    - profile_url for mention links

        Attributes:
            id (int):
            email (str):
            first_name (str):
            last_name (str):
            display_name (str): Return display name: full name or email.
            avatar_url (str): Return avatar URL (custom upload or Gravatar).
            profile_url (str): Return placeholder URL - no profile pages yet.
    """

    id: int
    email: str
    first_name: str
    last_name: str
    display_name: str
    avatar_url: str
    profile_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        email = self.email

        first_name = self.first_name

        last_name = self.last_name

        display_name = self.display_name

        avatar_url = self.avatar_url

        profile_url = self.profile_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "email": email,
                "first_name": first_name,
                "last_name": last_name,
                "display_name": display_name,
                "avatar_url": avatar_url,
                "profile_url": profile_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        email = d.pop("email")

        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        display_name = d.pop("display_name")

        avatar_url = d.pop("avatar_url")

        profile_url = d.pop("profile_url")

        user = cls(
            id=id,
            email=email,
            first_name=first_name,
            last_name=last_name,
            display_name=display_name,
            avatar_url=avatar_url,
            profile_url=profile_url,
        )

        user.additional_properties = d
        return user

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
