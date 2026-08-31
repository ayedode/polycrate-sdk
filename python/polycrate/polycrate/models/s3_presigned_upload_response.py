from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.s3_presigned_upload_response_fields import S3PresignedUploadResponseFields


T = TypeVar("T", bound="S3PresignedUploadResponse")


@_attrs_define
class S3PresignedUploadResponse:
    """
    Attributes:
        url (str): Presigned POST URL to upload the file to directly from the browser
        method (str): HTTP method to use (always 'POST')
        fields (S3PresignedUploadResponseFields): Form fields to include in the multipart/form-data POST request
        key (str): Object key that will be used
        expires_in (int): URL validity in seconds (900 = 15 minutes)
        max_size (int): Maximum upload size in bytes (5 GiB)
    """

    url: str
    method: str
    fields: S3PresignedUploadResponseFields
    key: str
    expires_in: int
    max_size: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        method = self.method

        fields = self.fields.to_dict()

        key = self.key

        expires_in = self.expires_in

        max_size = self.max_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "method": method,
                "fields": fields,
                "key": key,
                "expires_in": expires_in,
                "max_size": max_size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.s3_presigned_upload_response_fields import S3PresignedUploadResponseFields

        d = dict(src_dict)
        url = d.pop("url")

        method = d.pop("method")

        fields = S3PresignedUploadResponseFields.from_dict(d.pop("fields"))

        key = d.pop("key")

        expires_in = d.pop("expires_in")

        max_size = d.pop("max_size")

        s3_presigned_upload_response = cls(
            url=url,
            method=method,
            fields=fields,
            key=key,
            expires_in=expires_in,
            max_size=max_size,
        )

        s3_presigned_upload_response.additional_properties = d
        return s3_presigned_upload_response

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
