from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.lbi_v2_waf_request_fail_mode import LbiV2WafRequestFailMode, check_lbi_v2_waf_request_fail_mode
from ..models.lbi_v2_waf_request_mode import LbiV2WafRequestMode, check_lbi_v2_waf_request_mode
from ..types import UNSET, Unset

T = TypeVar("T", bound="LbiV2WafRequest")


@_attrs_define
class LbiV2WafRequest:
    """
    Attributes:
        enabled (bool | Unset):  Default: False.
        mode (LbiV2WafRequestMode | Unset): * `monitor` - monitor
            * `protect` - protect
            * `strict` - strict Default: 'monitor'.
        profile (None | str | Unset):
        fail_mode (LbiV2WafRequestFailMode | Unset): * `open` - open
            * `closed` - closed Default: 'open'.
        body_limit_bytes (int | Unset):
        routes (list[str] | Unset):
    """

    enabled: bool | Unset = False
    mode: LbiV2WafRequestMode | Unset = "monitor"
    profile: None | str | Unset = UNSET
    fail_mode: LbiV2WafRequestFailMode | Unset = "open"
    body_limit_bytes: int | Unset = UNSET
    routes: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode

        profile: None | str | Unset
        if isinstance(self.profile, Unset):
            profile = UNSET
        else:
            profile = self.profile

        fail_mode: str | Unset = UNSET
        if not isinstance(self.fail_mode, Unset):
            fail_mode = self.fail_mode

        body_limit_bytes = self.body_limit_bytes

        routes: list[str] | Unset = UNSET
        if not isinstance(self.routes, Unset):
            routes = self.routes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if mode is not UNSET:
            field_dict["mode"] = mode
        if profile is not UNSET:
            field_dict["profile"] = profile
        if fail_mode is not UNSET:
            field_dict["failMode"] = fail_mode
        if body_limit_bytes is not UNSET:
            field_dict["bodyLimitBytes"] = body_limit_bytes
        if routes is not UNSET:
            field_dict["routes"] = routes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: LbiV2WafRequestMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = check_lbi_v2_waf_request_mode(_mode)

        def _parse_profile(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        profile = _parse_profile(d.pop("profile", UNSET))

        _fail_mode = d.pop("failMode", UNSET)
        fail_mode: LbiV2WafRequestFailMode | Unset
        if isinstance(_fail_mode, Unset):
            fail_mode = UNSET
        else:
            fail_mode = check_lbi_v2_waf_request_fail_mode(_fail_mode)

        body_limit_bytes = d.pop("bodyLimitBytes", UNSET)

        routes = cast(list[str], d.pop("routes", UNSET))

        lbi_v2_waf_request = cls(
            enabled=enabled,
            mode=mode,
            profile=profile,
            fail_mode=fail_mode,
            body_limit_bytes=body_limit_bytes,
            routes=routes,
        )

        lbi_v2_waf_request.additional_properties = d
        return lbi_v2_waf_request

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
