from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OrganizationCachedMetricsS3ByRegion")


@_attrs_define
class OrganizationCachedMetricsS3ByRegion:
    """
    Attributes:
        region_id (None | UUID): S3Bucket.region_id; null when the bucket has no region
        bucket_count (int):
        storage_bytes (int):
        object_count (int):
    """

    region_id: None | UUID
    bucket_count: int
    storage_bytes: int
    object_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        region_id: None | str
        if isinstance(self.region_id, UUID):
            region_id = str(self.region_id)
        else:
            region_id = self.region_id

        bucket_count = self.bucket_count

        storage_bytes = self.storage_bytes

        object_count = self.object_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "region_id": region_id,
                "bucket_count": bucket_count,
                "storage_bytes": storage_bytes,
                "object_count": object_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_region_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                region_id_type_0 = UUID(data)

                return region_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        region_id = _parse_region_id(d.pop("region_id"))

        bucket_count = d.pop("bucket_count")

        storage_bytes = d.pop("storage_bytes")

        object_count = d.pop("object_count")

        organization_cached_metrics_s3_by_region = cls(
            region_id=region_id,
            bucket_count=bucket_count,
            storage_bytes=storage_bytes,
            object_count=object_count,
        )

        organization_cached_metrics_s3_by_region.additional_properties = d
        return organization_cached_metrics_s3_by_region

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
