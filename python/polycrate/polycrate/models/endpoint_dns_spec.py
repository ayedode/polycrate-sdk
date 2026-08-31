from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.protocol_enum import ProtocolEnum, check_protocol_enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="EndpointDNSSpec")


@_attrs_define
class EndpointDNSSpec:
    """
    Attributes:
        timeout (int | Unset):  Default: 10.
        interval (int | Unset):  Default: 60.
        record_name (str | Unset):  Default: ''.
        record_type (str | Unset):  Default: 'A'.
        protocol (ProtocolEnum | Unset): * `udp` - udp
            * `tcp` - tcp Default: 'udp'.
        expected_results (list[str] | Unset):
        expected_rcode (str | Unset):  Default: ''.
        tls_enabled (bool | Unset):  Default: False.
        tls_ignore_errors (bool | Unset):  Default: False.
        dnssec (bool | Unset):  Default: False.
    """

    timeout: int | Unset = 10
    interval: int | Unset = 60
    record_name: str | Unset = ""
    record_type: str | Unset = "A"
    protocol: ProtocolEnum | Unset = "udp"
    expected_results: list[str] | Unset = UNSET
    expected_rcode: str | Unset = ""
    tls_enabled: bool | Unset = False
    tls_ignore_errors: bool | Unset = False
    dnssec: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timeout = self.timeout

        interval = self.interval

        record_name = self.record_name

        record_type = self.record_type

        protocol: str | Unset = UNSET
        if not isinstance(self.protocol, Unset):
            protocol = self.protocol

        expected_results: list[str] | Unset = UNSET
        if not isinstance(self.expected_results, Unset):
            expected_results = self.expected_results

        expected_rcode = self.expected_rcode

        tls_enabled = self.tls_enabled

        tls_ignore_errors = self.tls_ignore_errors

        dnssec = self.dnssec

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if interval is not UNSET:
            field_dict["interval"] = interval
        if record_name is not UNSET:
            field_dict["record_name"] = record_name
        if record_type is not UNSET:
            field_dict["record_type"] = record_type
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if expected_results is not UNSET:
            field_dict["expected_results"] = expected_results
        if expected_rcode is not UNSET:
            field_dict["expected_rcode"] = expected_rcode
        if tls_enabled is not UNSET:
            field_dict["tls_enabled"] = tls_enabled
        if tls_ignore_errors is not UNSET:
            field_dict["tls_ignore_errors"] = tls_ignore_errors
        if dnssec is not UNSET:
            field_dict["dnssec"] = dnssec

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timeout = d.pop("timeout", UNSET)

        interval = d.pop("interval", UNSET)

        record_name = d.pop("record_name", UNSET)

        record_type = d.pop("record_type", UNSET)

        _protocol = d.pop("protocol", UNSET)
        protocol: ProtocolEnum | Unset
        if isinstance(_protocol, Unset):
            protocol = UNSET
        else:
            protocol = check_protocol_enum(_protocol)

        expected_results = cast(list[str], d.pop("expected_results", UNSET))

        expected_rcode = d.pop("expected_rcode", UNSET)

        tls_enabled = d.pop("tls_enabled", UNSET)

        tls_ignore_errors = d.pop("tls_ignore_errors", UNSET)

        dnssec = d.pop("dnssec", UNSET)

        endpoint_dns_spec = cls(
            timeout=timeout,
            interval=interval,
            record_name=record_name,
            record_type=record_type,
            protocol=protocol,
            expected_results=expected_results,
            expected_rcode=expected_rcode,
            tls_enabled=tls_enabled,
            tls_ignore_errors=tls_ignore_errors,
            dnssec=dnssec,
        )

        endpoint_dns_spec.additional_properties = d
        return endpoint_dns_spec

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
