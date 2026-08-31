from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_kind_enum import ApiKindEnum, check_api_kind_enum

T = TypeVar("T", bound="ProviderAccountSimple")


@_attrs_define
class ProviderAccountSimple:
    """
    Attributes:
        id (UUID):
        name (str):
        display_name (None | str): The display name is used to display the object in the UI. It can be different from
            the name.
        api_kind (ApiKindEnum): * `hetzner_cloud` - Hetzner Cloud
            * `openstack` - OpenStack
            * `ovhcloud` - OVHcloud
            * `ionos` - IONOS Cloud
            * `proxmox` - Proxmox VE
            * `openai_compat` - OpenAI Compatible
            * `cloudflare` - Cloudflare DNS
        url (str):
    """

    id: UUID
    name: str
    display_name: None | str
    api_kind: ApiKindEnum
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        display_name: None | str
        display_name = self.display_name

        api_kind: str = self.api_kind

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "display_name": display_name,
                "api_kind": api_kind,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        def _parse_display_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        display_name = _parse_display_name(d.pop("display_name"))

        api_kind = check_api_kind_enum(d.pop("api_kind"))

        url = d.pop("url")

        provider_account_simple = cls(
            id=id,
            name=name,
            display_name=display_name,
            api_kind=api_kind,
            url=url,
        )

        provider_account_simple.additional_properties = d
        return provider_account_simple

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
