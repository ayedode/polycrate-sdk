from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EndpointICMPSpecRequest")


@_attrs_define
class EndpointICMPSpecRequest:
    """
    Attributes:
        ttl (int | Unset):  Default: 255.
        timeout (float | Unset):  Default: 1.0.
        interval (float | Unset):  Default: 1.0.
    """

    ttl: int | Unset = 255
    timeout: float | Unset = 1.0
    interval: float | Unset = 1.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ttl = self.ttl

        timeout = self.timeout

        interval = self.interval

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ttl is not UNSET:
            field_dict["ttl"] = ttl
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if interval is not UNSET:
            field_dict["interval"] = interval

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ttl = d.pop("ttl", UNSET)

        timeout = d.pop("timeout", UNSET)

        interval = d.pop("interval", UNSET)

        endpoint_icmp_spec_request = cls(
            ttl=ttl,
            timeout=timeout,
            interval=interval,
        )

        endpoint_icmp_spec_request.additional_properties = d
        return endpoint_icmp_spec_request

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
