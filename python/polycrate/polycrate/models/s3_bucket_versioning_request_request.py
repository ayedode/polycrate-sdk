from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.s3_bucket_versioning_request_status_enum import (
    S3BucketVersioningRequestStatusEnum,
    check_s3_bucket_versioning_request_status_enum,
)

T = TypeVar("T", bound="S3BucketVersioningRequestRequest")


@_attrs_define
class S3BucketVersioningRequestRequest:
    """
    Attributes:
        status (S3BucketVersioningRequestStatusEnum): * `Enabled` - Enabled
            * `Suspended` - Suspended
    """

    status: S3BucketVersioningRequestStatusEnum
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("status", (None, str(self.status).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = check_s3_bucket_versioning_request_status_enum(d.pop("status"))

        s3_bucket_versioning_request_request = cls(
            status=status,
        )

        s3_bucket_versioning_request_request.additional_properties = d
        return s3_bucket_versioning_request_request

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
