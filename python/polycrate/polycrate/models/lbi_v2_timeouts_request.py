from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LbiV2TimeoutsRequest")


@_attrs_define
class LbiV2TimeoutsRequest:
    """
    Attributes:
        connect (int | Unset):
        idle (int | Unset):
        request (int | Unset):
    """

    connect: int | Unset = UNSET
    idle: int | Unset = UNSET
    request: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connect = self.connect

        idle = self.idle

        request = self.request

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connect is not UNSET:
            field_dict["connect"] = connect
        if idle is not UNSET:
            field_dict["idle"] = idle
        if request is not UNSET:
            field_dict["request"] = request

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connect = d.pop("connect", UNSET)

        idle = d.pop("idle", UNSET)

        request = d.pop("request", UNSET)

        lbi_v2_timeouts_request = cls(
            connect=connect,
            idle=idle,
            request=request,
        )

        lbi_v2_timeouts_request.additional_properties = d
        return lbi_v2_timeouts_request

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
