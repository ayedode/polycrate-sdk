from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OrganizationCachedMetricsS3")


@_attrs_define
class OrganizationCachedMetricsS3:
    """
    Attributes:
        storage_bytes (int):
        bucket_count (int):
        object_count (int):
    """

    storage_bytes: int
    bucket_count: int
    object_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        storage_bytes = self.storage_bytes

        bucket_count = self.bucket_count

        object_count = self.object_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "storage_bytes": storage_bytes,
                "bucket_count": bucket_count,
                "object_count": object_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        storage_bytes = d.pop("storage_bytes")

        bucket_count = d.pop("bucket_count")

        object_count = d.pop("object_count")

        organization_cached_metrics_s3 = cls(
            storage_bytes=storage_bytes,
            bucket_count=bucket_count,
            object_count=object_count,
        )

        organization_cached_metrics_s3.additional_properties = d
        return organization_cached_metrics_s3

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
