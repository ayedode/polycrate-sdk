from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="S3BucketPolicyResponse")


@_attrs_define
class S3BucketPolicyResponse:
    """
    Attributes:
        policy (None | str): Policy JSON-String oder null wenn keine Policy gesetzt
        has_policy (bool): True wenn eine Policy gesetzt ist
    """

    policy: None | str
    has_policy: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        policy: None | str
        policy = self.policy

        has_policy = self.has_policy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "policy": policy,
                "has_policy": has_policy,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_policy(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        policy = _parse_policy(d.pop("policy"))

        has_policy = d.pop("has_policy")

        s3_bucket_policy_response = cls(
            policy=policy,
            has_policy=has_policy,
        )

        s3_bucket_policy_response.additional_properties = d
        return s3_bucket_policy_response

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
