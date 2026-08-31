from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.s3_credential_list_data import S3CredentialListData
    from ..models.s3_credential_list_meta import S3CredentialListMeta


T = TypeVar("T", bound="S3CredentialListResponse")


@_attrs_define
class S3CredentialListResponse:
    """
    Attributes:
        data (S3CredentialListData):
        meta (S3CredentialListMeta):
        success (bool | Unset):  Default: True.
    """

    data: S3CredentialListData
    meta: S3CredentialListMeta
    success: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        meta = self.meta.to_dict()

        success = self.success

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "meta": meta,
            }
        )
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.s3_credential_list_data import S3CredentialListData
        from ..models.s3_credential_list_meta import S3CredentialListMeta

        d = dict(src_dict)
        data = S3CredentialListData.from_dict(d.pop("data"))

        meta = S3CredentialListMeta.from_dict(d.pop("meta"))

        success = d.pop("success", UNSET)

        s3_credential_list_response = cls(
            data=data,
            meta=meta,
            success=success,
        )

        s3_credential_list_response.additional_properties = d
        return s3_credential_list_response

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
