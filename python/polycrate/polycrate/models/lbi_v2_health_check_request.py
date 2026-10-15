from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.lbi_v2_health_check_request_type import (
    LbiV2HealthCheckRequestType,
    check_lbi_v2_health_check_request_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="LbiV2HealthCheckRequest")


@_attrs_define
class LbiV2HealthCheckRequest:
    """
    Attributes:
        type_ (LbiV2HealthCheckRequestType | Unset): * `TCP` - TCP
            * `HTTP` - HTTP Default: 'TCP'.
        interval (int | Unset):
        timeout (int | Unset):
        unhealthy_threshold (int | Unset):
        healthy_threshold (int | Unset):
        path (str | Unset):
    """

    type_: LbiV2HealthCheckRequestType | Unset = "TCP"
    interval: int | Unset = UNSET
    timeout: int | Unset = UNSET
    unhealthy_threshold: int | Unset = UNSET
    healthy_threshold: int | Unset = UNSET
    path: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        interval = self.interval

        timeout = self.timeout

        unhealthy_threshold = self.unhealthy_threshold

        healthy_threshold = self.healthy_threshold

        path = self.path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if interval is not UNSET:
            field_dict["interval"] = interval
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if unhealthy_threshold is not UNSET:
            field_dict["unhealthyThreshold"] = unhealthy_threshold
        if healthy_threshold is not UNSET:
            field_dict["healthyThreshold"] = healthy_threshold
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: LbiV2HealthCheckRequestType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_lbi_v2_health_check_request_type(_type_)

        interval = d.pop("interval", UNSET)

        timeout = d.pop("timeout", UNSET)

        unhealthy_threshold = d.pop("unhealthyThreshold", UNSET)

        healthy_threshold = d.pop("healthyThreshold", UNSET)

        path = d.pop("path", UNSET)

        lbi_v2_health_check_request = cls(
            type_=type_,
            interval=interval,
            timeout=timeout,
            unhealthy_threshold=unhealthy_threshold,
            healthy_threshold=healthy_threshold,
            path=path,
        )

        lbi_v2_health_check_request.additional_properties = d
        return lbi_v2_health_check_request

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
