from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="DNSEnableDnssecRequestRequest")


@_attrs_define
class DNSEnableDnssecRequestRequest:
    """
    Attributes:
        algorithm (str | Unset): DNSSEC signing algorithm. Default: 'ecdsa256'. Default: 'ecdsa256'.
        nsec3 (bool | Unset): Enable NSEC3 denial-of-existence. Default: false. Default: False.
    """

    algorithm: str | Unset = "ecdsa256"
    nsec3: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        algorithm = self.algorithm

        nsec3 = self.nsec3

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if algorithm is not UNSET:
            field_dict["algorithm"] = algorithm
        if nsec3 is not UNSET:
            field_dict["nsec3"] = nsec3

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.algorithm, Unset):
            files.append(("algorithm", (None, str(self.algorithm).encode(), "text/plain")))

        if not isinstance(self.nsec3, Unset):
            files.append(("nsec3", (None, str(self.nsec3).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        algorithm = d.pop("algorithm", UNSET)

        nsec3 = d.pop("nsec3", UNSET)

        dns_enable_dnssec_request_request = cls(
            algorithm=algorithm,
            nsec3=nsec3,
        )

        dns_enable_dnssec_request_request.additional_properties = d
        return dns_enable_dnssec_request_request

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
