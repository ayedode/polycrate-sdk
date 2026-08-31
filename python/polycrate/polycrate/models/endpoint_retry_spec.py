from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EndpointRetrySpec")


@_attrs_define
class EndpointRetrySpec:
    """
    Attributes:
        enabled (bool | Unset):  Default: False.
        count (int | Unset):  Default: 5.
        sleep (float | Unset):  Default: 1.0.
    """

    enabled: bool | Unset = False
    count: int | Unset = 5
    sleep: float | Unset = 1.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        count = self.count

        sleep = self.sleep

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if count is not UNSET:
            field_dict["count"] = count
        if sleep is not UNSET:
            field_dict["sleep"] = sleep

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        count = d.pop("count", UNSET)

        sleep = d.pop("sleep", UNSET)

        endpoint_retry_spec = cls(
            enabled=enabled,
            count=count,
            sleep=sleep,
        )

        endpoint_retry_spec.additional_properties = d
        return endpoint_retry_spec

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
