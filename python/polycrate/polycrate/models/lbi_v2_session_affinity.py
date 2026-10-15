from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.lbi_v2_session_affinity_type import LbiV2SessionAffinityType, check_lbi_v2_session_affinity_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="LbiV2SessionAffinity")


@_attrs_define
class LbiV2SessionAffinity:
    """
    Attributes:
        type_ (LbiV2SessionAffinityType | Unset): * `none` - none
            * `source` - source
            * `cookie` - cookie Default: 'none'.
        cookie_name (str | Unset):
    """

    type_: LbiV2SessionAffinityType | Unset = "none"
    cookie_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        cookie_name = self.cookie_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if cookie_name is not UNSET:
            field_dict["cookieName"] = cookie_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: LbiV2SessionAffinityType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_lbi_v2_session_affinity_type(_type_)

        cookie_name = d.pop("cookieName", UNSET)

        lbi_v2_session_affinity = cls(
            type_=type_,
            cookie_name=cookie_name,
        )

        lbi_v2_session_affinity.additional_properties = d
        return lbi_v2_session_affinity

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
