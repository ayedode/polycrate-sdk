from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.s3_credential_with_secrets import S3CredentialWithSecrets


T = TypeVar("T", bound="S3CredentialListData")


@_attrs_define
class S3CredentialListData:
    """
    Attributes:
        bucket_id (UUID):
        bucket_name (str):
        credentials (list[S3CredentialWithSecrets]):
    """

    bucket_id: UUID
    bucket_name: str
    credentials: list[S3CredentialWithSecrets]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket_id = str(self.bucket_id)

        bucket_name = self.bucket_name

        credentials = []
        for credentials_item_data in self.credentials:
            credentials_item = credentials_item_data.to_dict()
            credentials.append(credentials_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bucket_id": bucket_id,
                "bucket_name": bucket_name,
                "credentials": credentials,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.s3_credential_with_secrets import S3CredentialWithSecrets

        d = dict(src_dict)
        bucket_id = UUID(d.pop("bucket_id"))

        bucket_name = d.pop("bucket_name")

        credentials = []
        _credentials = d.pop("credentials")
        for credentials_item_data in _credentials:
            credentials_item = S3CredentialWithSecrets.from_dict(credentials_item_data)

            credentials.append(credentials_item)

        s3_credential_list_data = cls(
            bucket_id=bucket_id,
            bucket_name=bucket_name,
            credentials=credentials,
        )

        s3_credential_list_data.additional_properties = d
        return s3_credential_list_data

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
