from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="S3CredentialListMeta")


@_attrs_define
class S3CredentialListMeta:
    """
    Attributes:
        total_credentials (int):
        primary_credentials (int):
        additional_credentials (int):
    """

    total_credentials: int
    primary_credentials: int
    additional_credentials: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_credentials = self.total_credentials

        primary_credentials = self.primary_credentials

        additional_credentials = self.additional_credentials

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_credentials": total_credentials,
                "primary_credentials": primary_credentials,
                "additional_credentials": additional_credentials,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_credentials = d.pop("total_credentials")

        primary_credentials = d.pop("primary_credentials")

        additional_credentials = d.pop("additional_credentials")

        s3_credential_list_meta = cls(
            total_credentials=total_credentials,
            primary_credentials=primary_credentials,
            additional_credentials=additional_credentials,
        )

        s3_credential_list_meta.additional_properties = d
        return s3_credential_list_meta

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
