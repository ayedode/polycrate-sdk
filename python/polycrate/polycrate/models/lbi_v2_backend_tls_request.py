from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LbiV2BackendTlsRequest")


@_attrs_define
class LbiV2BackendTlsRequest:
    """
    Attributes:
        verify (bool | Unset):  Default: True.
        sni (None | str | Unset):
    """

    verify: bool | Unset = True
    sni: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        verify = self.verify

        sni: None | str | Unset
        if isinstance(self.sni, Unset):
            sni = UNSET
        else:
            sni = self.sni

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if verify is not UNSET:
            field_dict["verify"] = verify
        if sni is not UNSET:
            field_dict["sni"] = sni

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        verify = d.pop("verify", UNSET)

        def _parse_sni(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sni = _parse_sni(d.pop("sni", UNSET))

        lbi_v2_backend_tls_request = cls(
            verify=verify,
            sni=sni,
        )

        lbi_v2_backend_tls_request.additional_properties = d
        return lbi_v2_backend_tls_request

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
