from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dns_provider_catalog_item_credential_schema import DNSProviderCatalogItemCredentialSchema


T = TypeVar("T", bound="DNSProviderCatalogItem")


@_attrs_define
class DNSProviderCatalogItem:
    """
    Attributes:
        slug (str): Lexicon provider slug (used in DNSZone.provider and Credential.metadata.dns_provider).
        label (str): Human-readable provider name.
        credential_schema (DNSProviderCatalogItemCredentialSchema): Required and optional Credential fields for this
            provider. Keys: api_key, api_user, metadata. Each entry has: label, required, sensitive, help (optional), hint
            (optional).
    """

    slug: str
    label: str
    credential_schema: DNSProviderCatalogItemCredentialSchema
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        label = self.label

        credential_schema = self.credential_schema.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "slug": slug,
                "label": label,
                "credential_schema": credential_schema,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dns_provider_catalog_item_credential_schema import (
            DNSProviderCatalogItemCredentialSchema,  # noqa: PLC0415
        )

        d = dict(src_dict)
        slug = d.pop("slug")

        label = d.pop("label")

        credential_schema = DNSProviderCatalogItemCredentialSchema.from_dict(d.pop("credential_schema"))

        dns_provider_catalog_item = cls(
            slug=slug,
            label=label,
            credential_schema=credential_schema,
        )

        dns_provider_catalog_item.additional_properties = d
        return dns_provider_catalog_item

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
