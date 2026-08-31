from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.s3_bucket_settings_response_provider_metadata import S3BucketSettingsResponseProviderMetadata


T = TypeVar("T", bound="S3BucketSettingsResponse")


@_attrs_define
class S3BucketSettingsResponse:
    """
    Attributes:
        provider_metadata (S3BucketSettingsResponseProviderMetadata): Updated provider_metadata after the settings
            change.
    """

    provider_metadata: S3BucketSettingsResponseProviderMetadata
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider_metadata = self.provider_metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider_metadata": provider_metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.s3_bucket_settings_response_provider_metadata import S3BucketSettingsResponseProviderMetadata

        d = dict(src_dict)
        provider_metadata = S3BucketSettingsResponseProviderMetadata.from_dict(d.pop("provider_metadata"))

        s3_bucket_settings_response = cls(
            provider_metadata=provider_metadata,
        )

        s3_bucket_settings_response.additional_properties = d
        return s3_bucket_settings_response

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
