from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="S3ObjectDownloadResponse")


@_attrs_define
class S3ObjectDownloadResponse:
    """
    Attributes:
        url (str): Presigned download URL (valid for 1 hour)
        key (str):
        filename (str):
        expires_in (int):
    """

    url: str
    key: str
    filename: str
    expires_in: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        key = self.key

        filename = self.filename

        expires_in = self.expires_in

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "key": key,
                "filename": filename,
                "expires_in": expires_in,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        key = d.pop("key")

        filename = d.pop("filename")

        expires_in = d.pop("expires_in")

        s3_object_download_response = cls(
            url=url,
            key=key,
            filename=filename,
            expires_in=expires_in,
        )

        s3_object_download_response.additional_properties = d
        return s3_object_download_response

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
