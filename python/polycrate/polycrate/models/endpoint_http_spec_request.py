from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EndpointHTTPSpecRequest")


@_attrs_define
class EndpointHTTPSpecRequest:
    """
    Attributes:
        path (str | Unset):  Default: '/'.
        tls (bool | Unset):  Default: False.
        alert_tls_expiry (bool | Unset):  Default: True.
        ignore_tls_errors (bool | Unset):  Default: False.
        timeout (int | Unset):  Default: 5.
        interval (int | Unset):  Default: 60.
        method (str | Unset):  Default: 'GET'.
        user_agent (str | Unset):
        referer (str | Unset):
        follow_redirect (bool | Unset):  Default: True.
        max_redirects (int | Unset):  Default: 10.
        expected_status_code (int | Unset):  Default: 200.
        accepted_status_codes (list[int] | Unset):
        bad_status_codes (list[int] | Unset):
    """

    path: str | Unset = "/"
    tls: bool | Unset = False
    alert_tls_expiry: bool | Unset = True
    ignore_tls_errors: bool | Unset = False
    timeout: int | Unset = 5
    interval: int | Unset = 60
    method: str | Unset = "GET"
    user_agent: str | Unset = UNSET
    referer: str | Unset = UNSET
    follow_redirect: bool | Unset = True
    max_redirects: int | Unset = 10
    expected_status_code: int | Unset = 200
    accepted_status_codes: list[int] | Unset = UNSET
    bad_status_codes: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        tls = self.tls

        alert_tls_expiry = self.alert_tls_expiry

        ignore_tls_errors = self.ignore_tls_errors

        timeout = self.timeout

        interval = self.interval

        method = self.method

        user_agent = self.user_agent

        referer = self.referer

        follow_redirect = self.follow_redirect

        max_redirects = self.max_redirects

        expected_status_code = self.expected_status_code

        accepted_status_codes: list[int] | Unset = UNSET
        if not isinstance(self.accepted_status_codes, Unset):
            accepted_status_codes = self.accepted_status_codes

        bad_status_codes: list[int] | Unset = UNSET
        if not isinstance(self.bad_status_codes, Unset):
            bad_status_codes = self.bad_status_codes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if tls is not UNSET:
            field_dict["tls"] = tls
        if alert_tls_expiry is not UNSET:
            field_dict["alert_tls_expiry"] = alert_tls_expiry
        if ignore_tls_errors is not UNSET:
            field_dict["ignore_tls_errors"] = ignore_tls_errors
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if interval is not UNSET:
            field_dict["interval"] = interval
        if method is not UNSET:
            field_dict["method"] = method
        if user_agent is not UNSET:
            field_dict["user_agent"] = user_agent
        if referer is not UNSET:
            field_dict["referer"] = referer
        if follow_redirect is not UNSET:
            field_dict["follow_redirect"] = follow_redirect
        if max_redirects is not UNSET:
            field_dict["max_redirects"] = max_redirects
        if expected_status_code is not UNSET:
            field_dict["expected_status_code"] = expected_status_code
        if accepted_status_codes is not UNSET:
            field_dict["accepted_status_codes"] = accepted_status_codes
        if bad_status_codes is not UNSET:
            field_dict["bad_status_codes"] = bad_status_codes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path", UNSET)

        tls = d.pop("tls", UNSET)

        alert_tls_expiry = d.pop("alert_tls_expiry", UNSET)

        ignore_tls_errors = d.pop("ignore_tls_errors", UNSET)

        timeout = d.pop("timeout", UNSET)

        interval = d.pop("interval", UNSET)

        method = d.pop("method", UNSET)

        user_agent = d.pop("user_agent", UNSET)

        referer = d.pop("referer", UNSET)

        follow_redirect = d.pop("follow_redirect", UNSET)

        max_redirects = d.pop("max_redirects", UNSET)

        expected_status_code = d.pop("expected_status_code", UNSET)

        accepted_status_codes = cast(list[int], d.pop("accepted_status_codes", UNSET))

        bad_status_codes = cast(list[int], d.pop("bad_status_codes", UNSET))

        endpoint_http_spec_request = cls(
            path=path,
            tls=tls,
            alert_tls_expiry=alert_tls_expiry,
            ignore_tls_errors=ignore_tls_errors,
            timeout=timeout,
            interval=interval,
            method=method,
            user_agent=user_agent,
            referer=referer,
            follow_redirect=follow_redirect,
            max_redirects=max_redirects,
            expected_status_code=expected_status_code,
            accepted_status_codes=accepted_status_codes,
            bad_status_codes=bad_status_codes,
        )

        endpoint_http_spec_request.additional_properties = d
        return endpoint_http_spec_request

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
