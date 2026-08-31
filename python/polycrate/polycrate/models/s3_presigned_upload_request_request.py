from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="S3PresignedUploadRequestRequest")


@_attrs_define
class S3PresignedUploadRequestRequest:
    """
    Attributes:
        key (str): Target object key (full path including filename, e.g. 'uploads/photo.jpg')
        content_type (str | Unset): MIME type of the file to upload (default: application/octet-stream) Default:
            'application/octet-stream'.
        overwrite (bool | Unset): Allow overwriting an existing object (default: false) Default: False.
    """

    key: str
    content_type: str | Unset = "application/octet-stream"
    overwrite: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        content_type = self.content_type

        overwrite = self.overwrite

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
            }
        )
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if overwrite is not UNSET:
            field_dict["overwrite"] = overwrite

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("key", (None, str(self.key).encode(), "text/plain")))

        if not isinstance(self.content_type, Unset):
            files.append(("content_type", (None, str(self.content_type).encode(), "text/plain")))

        if not isinstance(self.overwrite, Unset):
            files.append(("overwrite", (None, str(self.overwrite).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        content_type = d.pop("content_type", UNSET)

        overwrite = d.pop("overwrite", UNSET)

        s3_presigned_upload_request_request = cls(
            key=key,
            content_type=content_type,
            overwrite=overwrite,
        )

        s3_presigned_upload_request_request.additional_properties = d
        return s3_presigned_upload_request_request

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
