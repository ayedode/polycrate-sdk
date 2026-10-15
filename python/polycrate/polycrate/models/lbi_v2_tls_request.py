from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.lbi_v2_tls_request_challenge import LbiV2TlsRequestChallenge, check_lbi_v2_tls_request_challenge
from ..models.lbi_v2_tls_request_mode import LbiV2TlsRequestMode, check_lbi_v2_tls_request_mode
from ..types import UNSET, Unset

T = TypeVar("T", bound="LbiV2TlsRequest")


@_attrs_define
class LbiV2TlsRequest:
    """
    Attributes:
        mode (LbiV2TlsRequestMode | Unset): * `terminate` - terminate
            * `passthrough` - passthrough Default: 'terminate'.
        challenge (LbiV2TlsRequestChallenge | Unset): * `http01` - http01
            * `dns01` - dns01 Default: 'dns01'.
        domains (list[str] | Unset):
    """

    mode: LbiV2TlsRequestMode | Unset = "terminate"
    challenge: LbiV2TlsRequestChallenge | Unset = "dns01"
    domains: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode

        challenge: str | Unset = UNSET
        if not isinstance(self.challenge, Unset):
            challenge = self.challenge

        domains: list[str] | Unset = UNSET
        if not isinstance(self.domains, Unset):
            domains = self.domains

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mode is not UNSET:
            field_dict["mode"] = mode
        if challenge is not UNSET:
            field_dict["challenge"] = challenge
        if domains is not UNSET:
            field_dict["domains"] = domains

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _mode = d.pop("mode", UNSET)
        mode: LbiV2TlsRequestMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = check_lbi_v2_tls_request_mode(_mode)

        _challenge = d.pop("challenge", UNSET)
        challenge: LbiV2TlsRequestChallenge | Unset
        if isinstance(_challenge, Unset):
            challenge = UNSET
        else:
            challenge = check_lbi_v2_tls_request_challenge(_challenge)

        domains = cast(list[str], d.pop("domains", UNSET))

        lbi_v2_tls_request = cls(
            mode=mode,
            challenge=challenge,
            domains=domains,
        )

        lbi_v2_tls_request.additional_properties = d
        return lbi_v2_tls_request

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
