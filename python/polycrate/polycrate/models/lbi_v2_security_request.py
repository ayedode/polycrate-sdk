from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lbi_v2_security_request_auth import LbiV2SecurityRequestAuth
    from ..models.lbi_v2_security_request_rate_limit import LbiV2SecurityRequestRateLimit
    from ..models.lbi_v2_waf_request import LbiV2WafRequest


T = TypeVar("T", bound="LbiV2SecurityRequest")


@_attrs_define
class LbiV2SecurityRequest:
    """
    Attributes:
        rate_limit (LbiV2SecurityRequestRateLimit | Unset):
        ip_allow_list (list[str] | Unset):
        ip_deny_list (list[str] | Unset):
        auth (LbiV2SecurityRequestAuth | Unset):
        waf (LbiV2WafRequest | None | Unset):
    """

    rate_limit: LbiV2SecurityRequestRateLimit | Unset = UNSET
    ip_allow_list: list[str] | Unset = UNSET
    ip_deny_list: list[str] | Unset = UNSET
    auth: LbiV2SecurityRequestAuth | Unset = UNSET
    waf: LbiV2WafRequest | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.lbi_v2_waf_request import LbiV2WafRequest  # noqa: PLC0415

        rate_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rate_limit, Unset):
            rate_limit = self.rate_limit.to_dict()

        ip_allow_list: list[str] | Unset = UNSET
        if not isinstance(self.ip_allow_list, Unset):
            ip_allow_list = self.ip_allow_list

        ip_deny_list: list[str] | Unset = UNSET
        if not isinstance(self.ip_deny_list, Unset):
            ip_deny_list = self.ip_deny_list

        auth: dict[str, Any] | Unset = UNSET
        if not isinstance(self.auth, Unset):
            auth = self.auth.to_dict()

        waf: dict[str, Any] | None | Unset
        if isinstance(self.waf, Unset):
            waf = UNSET
        elif isinstance(self.waf, LbiV2WafRequest):
            waf = self.waf.to_dict()
        else:
            waf = self.waf

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rate_limit is not UNSET:
            field_dict["rateLimit"] = rate_limit
        if ip_allow_list is not UNSET:
            field_dict["ipAllowList"] = ip_allow_list
        if ip_deny_list is not UNSET:
            field_dict["ipDenyList"] = ip_deny_list
        if auth is not UNSET:
            field_dict["auth"] = auth
        if waf is not UNSET:
            field_dict["waf"] = waf

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lbi_v2_security_request_auth import LbiV2SecurityRequestAuth  # noqa: PLC0415
        from ..models.lbi_v2_security_request_rate_limit import LbiV2SecurityRequestRateLimit  # noqa: PLC0415
        from ..models.lbi_v2_waf_request import LbiV2WafRequest  # noqa: PLC0415

        d = dict(src_dict)
        _rate_limit = d.pop("rateLimit", UNSET)
        rate_limit: LbiV2SecurityRequestRateLimit | Unset
        if isinstance(_rate_limit, Unset):
            rate_limit = UNSET
        else:
            rate_limit = LbiV2SecurityRequestRateLimit.from_dict(_rate_limit)

        ip_allow_list = cast(list[str], d.pop("ipAllowList", UNSET))

        ip_deny_list = cast(list[str], d.pop("ipDenyList", UNSET))

        _auth = d.pop("auth", UNSET)
        auth: LbiV2SecurityRequestAuth | Unset
        if isinstance(_auth, Unset):
            auth = UNSET
        else:
            auth = LbiV2SecurityRequestAuth.from_dict(_auth)

        def _parse_waf(data: object) -> LbiV2WafRequest | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                waf_type_1 = LbiV2WafRequest.from_dict(data)

                return waf_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LbiV2WafRequest | None | Unset, data)

        waf = _parse_waf(d.pop("waf", UNSET))

        lbi_v2_security_request = cls(
            rate_limit=rate_limit,
            ip_allow_list=ip_allow_list,
            ip_deny_list=ip_deny_list,
            auth=auth,
            waf=waf,
        )

        lbi_v2_security_request.additional_properties = d
        return lbi_v2_security_request

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
