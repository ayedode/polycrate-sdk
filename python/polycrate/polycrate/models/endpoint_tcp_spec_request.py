from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EndpointTCPSpecRequest")


@_attrs_define
class EndpointTCPSpecRequest:
    """
    Attributes:
        tls (bool | Unset):  Default: False.
        ignore_tls_errors (bool | Unset):  Default: False.
        alert_expiry_days (int | Unset):  Default: 30.
        timeout (int | Unset):  Default: 10.
        interval (int | Unset):  Default: 60.
        send_string (str | Unset):  Default: ''.
        expected_response (str | Unset):  Default: ''.
    """

    tls: bool | Unset = False
    ignore_tls_errors: bool | Unset = False
    alert_expiry_days: int | Unset = 30
    timeout: int | Unset = 10
    interval: int | Unset = 60
    send_string: str | Unset = ""
    expected_response: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tls = self.tls

        ignore_tls_errors = self.ignore_tls_errors

        alert_expiry_days = self.alert_expiry_days

        timeout = self.timeout

        interval = self.interval

        send_string = self.send_string

        expected_response = self.expected_response

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tls is not UNSET:
            field_dict["tls"] = tls
        if ignore_tls_errors is not UNSET:
            field_dict["ignore_tls_errors"] = ignore_tls_errors
        if alert_expiry_days is not UNSET:
            field_dict["alert_expiry_days"] = alert_expiry_days
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if interval is not UNSET:
            field_dict["interval"] = interval
        if send_string is not UNSET:
            field_dict["send_string"] = send_string
        if expected_response is not UNSET:
            field_dict["expected_response"] = expected_response

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tls = d.pop("tls", UNSET)

        ignore_tls_errors = d.pop("ignore_tls_errors", UNSET)

        alert_expiry_days = d.pop("alert_expiry_days", UNSET)

        timeout = d.pop("timeout", UNSET)

        interval = d.pop("interval", UNSET)

        send_string = d.pop("send_string", UNSET)

        expected_response = d.pop("expected_response", UNSET)

        endpoint_tcp_spec_request = cls(
            tls=tls,
            ignore_tls_errors=ignore_tls_errors,
            alert_expiry_days=alert_expiry_days,
            timeout=timeout,
            interval=interval,
            send_string=send_string,
            expected_response=expected_response,
        )

        endpoint_tcp_spec_request.additional_properties = d
        return endpoint_tcp_spec_request

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
