from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.organization_cached_metrics_s3_by_region import OrganizationCachedMetricsS3ByRegion


T = TypeVar("T", bound="OrganizationCachedMetricsS3")


@_attrs_define
class OrganizationCachedMetricsS3:
    """
    Attributes:
        storage_bytes (int): All-region owned plus Loopback-delegated bucket storage in bytes after exclude_archived
            (object, workspace, organization)
        bucket_count (int): All-region owned plus Loopback-delegated S3 bucket count after exclude_archived (object,
            workspace, organization)
        object_count (int): All-region object count across owned plus Loopback-delegated buckets after exclude_archived
        by_region (list[OrganizationCachedMetricsS3ByRegion]): Same exclude_archived scope as the top-level totals,
            grouped by effective region. Missing region means zero.
    """

    storage_bytes: int
    bucket_count: int
    object_count: int
    by_region: list[OrganizationCachedMetricsS3ByRegion]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        storage_bytes = self.storage_bytes

        bucket_count = self.bucket_count

        object_count = self.object_count

        by_region = []
        for by_region_item_data in self.by_region:
            by_region_item = by_region_item_data.to_dict()
            by_region.append(by_region_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "storage_bytes": storage_bytes,
                "bucket_count": bucket_count,
                "object_count": object_count,
                "by_region": by_region,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organization_cached_metrics_s3_by_region import OrganizationCachedMetricsS3ByRegion  # noqa: PLC0415

        d = dict(src_dict)
        storage_bytes = d.pop("storage_bytes")

        bucket_count = d.pop("bucket_count")

        object_count = d.pop("object_count")

        by_region = []
        _by_region = d.pop("by_region")
        for by_region_item_data in _by_region:
            by_region_item = OrganizationCachedMetricsS3ByRegion.from_dict(by_region_item_data)

            by_region.append(by_region_item)

        organization_cached_metrics_s3 = cls(
            storage_bytes=storage_bytes,
            bucket_count=bucket_count,
            object_count=object_count,
            by_region=by_region,
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
