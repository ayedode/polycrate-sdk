from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.s3_credential_with_secrets import S3CredentialWithSecrets


T = TypeVar("T", bound="ApiV1S3BucketsCredentialsCreateCreateResponse201")


@_attrs_define
class ApiV1S3BucketsCredentialsCreateCreateResponse201:
    """
    Attributes:
        success (bool | Unset):  Example: True.
        data (S3CredentialWithSecrets | Unset): S3 Access Key including secrets.

            `access_key` maps to `api_user` (the RadosGW access key ID).
            `secret_key` maps to `api_key` (the RadosGW secret key).

            Spec 508: returned in the legacy list envelope (`data.credentials`) and in
            the create envelope (`data`). Callers that must avoid persisting secrets
            should discard them client-side after use.
        message (str | Unset):  Example: Access key 'CI/CD Pipeline' created successfully.
    """

    success: bool | Unset = UNSET
    data: S3CredentialWithSecrets | Unset = UNSET
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if data is not UNSET:
            field_dict["data"] = data
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.s3_credential_with_secrets import S3CredentialWithSecrets

        d = dict(src_dict)
        success = d.pop("success", UNSET)

        _data = d.pop("data", UNSET)
        data: S3CredentialWithSecrets | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = S3CredentialWithSecrets.from_dict(_data)

        message = d.pop("message", UNSET)

        api_v1s3_buckets_credentials_create_create_response_201 = cls(
            success=success,
            data=data,
            message=message,
        )

        api_v1s3_buckets_credentials_create_create_response_201.additional_properties = d
        return api_v1s3_buckets_credentials_create_create_response_201

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
