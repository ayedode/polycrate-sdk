from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dns_zone_kind_enum import DNSZoneKindEnum, check_dns_zone_kind_enum

T = TypeVar("T", bound="DNSZoneSimple")


@_attrs_define
class DNSZoneSimple:
    """
    Attributes:
        id (UUID):
        name (str): Zone name without trailing dot. May be a registered domain (e.g. 'example.com') or a delegated
            subdomain (e.g. 'project.example.com').
        kind (DNSZoneKindEnum): * `internal` - Internal
            * `external` - External
        provider (None | str): Lexicon provider name (e.g. 'cloudflare', 'hetzner', 'route53'). Required for
            kind='external'. Immutable after creation.
        primary_zone (bool): When multiple external DNS zones share the same name in an organization (different
            providers), the primary zone is preferred for DNS01/ACME and other single-writer automations. Default true.
        url (str):
    """

    id: UUID
    name: str
    kind: DNSZoneKindEnum
    provider: None | str
    primary_zone: bool
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        kind: str = self.kind

        provider: None | str
        provider = self.provider

        primary_zone = self.primary_zone

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "kind": kind,
                "provider": provider,
                "primary_zone": primary_zone,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        kind = check_dns_zone_kind_enum(d.pop("kind"))

        def _parse_provider(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        provider = _parse_provider(d.pop("provider"))

        primary_zone = d.pop("primary_zone")

        url = d.pop("url")

        dns_zone_simple = cls(
            id=id,
            name=name,
            kind=kind,
            provider=provider,
            primary_zone=primary_zone,
            url=url,
        )

        dns_zone_simple.additional_properties = d
        return dns_zone_simple

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
