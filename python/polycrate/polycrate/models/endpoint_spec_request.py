from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.endpoint_dns_spec_request import EndpointDNSSpecRequest
    from ..models.endpoint_http_spec_request import EndpointHTTPSpecRequest
    from ..models.endpoint_icmp_spec_request import EndpointICMPSpecRequest
    from ..models.endpoint_retry_spec_request import EndpointRetrySpecRequest
    from ..models.endpoint_tcp_spec_request import EndpointTCPSpecRequest


T = TypeVar("T", bound="EndpointSpecRequest")


@_attrs_define
class EndpointSpecRequest:
    """Typed representation of the endpoint spec JSONField.
    Each sub-serializer covers one check kind; unused kinds are omitted (null).
    Consumed by the Go operator/agent via the generated API client.

        Attributes:
            retry (EndpointRetrySpecRequest | None | Unset):
            http (EndpointHTTPSpecRequest | None | Unset):
            icmp (EndpointICMPSpecRequest | None | Unset):
            tcp (EndpointTCPSpecRequest | None | Unset):
            dns (EndpointDNSSpecRequest | None | Unset):
    """

    retry: EndpointRetrySpecRequest | None | Unset = UNSET
    http: EndpointHTTPSpecRequest | None | Unset = UNSET
    icmp: EndpointICMPSpecRequest | None | Unset = UNSET
    tcp: EndpointTCPSpecRequest | None | Unset = UNSET
    dns: EndpointDNSSpecRequest | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.endpoint_dns_spec_request import EndpointDNSSpecRequest  # noqa: PLC0415
        from ..models.endpoint_http_spec_request import EndpointHTTPSpecRequest  # noqa: PLC0415
        from ..models.endpoint_icmp_spec_request import EndpointICMPSpecRequest  # noqa: PLC0415
        from ..models.endpoint_retry_spec_request import EndpointRetrySpecRequest  # noqa: PLC0415
        from ..models.endpoint_tcp_spec_request import EndpointTCPSpecRequest  # noqa: PLC0415

        retry: dict[str, Any] | None | Unset
        if isinstance(self.retry, Unset):
            retry = UNSET
        elif isinstance(self.retry, EndpointRetrySpecRequest):
            retry = self.retry.to_dict()
        else:
            retry = self.retry

        http: dict[str, Any] | None | Unset
        if isinstance(self.http, Unset):
            http = UNSET
        elif isinstance(self.http, EndpointHTTPSpecRequest):
            http = self.http.to_dict()
        else:
            http = self.http

        icmp: dict[str, Any] | None | Unset
        if isinstance(self.icmp, Unset):
            icmp = UNSET
        elif isinstance(self.icmp, EndpointICMPSpecRequest):
            icmp = self.icmp.to_dict()
        else:
            icmp = self.icmp

        tcp: dict[str, Any] | None | Unset
        if isinstance(self.tcp, Unset):
            tcp = UNSET
        elif isinstance(self.tcp, EndpointTCPSpecRequest):
            tcp = self.tcp.to_dict()
        else:
            tcp = self.tcp

        dns: dict[str, Any] | None | Unset
        if isinstance(self.dns, Unset):
            dns = UNSET
        elif isinstance(self.dns, EndpointDNSSpecRequest):
            dns = self.dns.to_dict()
        else:
            dns = self.dns

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if retry is not UNSET:
            field_dict["retry"] = retry
        if http is not UNSET:
            field_dict["http"] = http
        if icmp is not UNSET:
            field_dict["icmp"] = icmp
        if tcp is not UNSET:
            field_dict["tcp"] = tcp
        if dns is not UNSET:
            field_dict["dns"] = dns

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.endpoint_dns_spec_request import EndpointDNSSpecRequest  # noqa: PLC0415
        from ..models.endpoint_http_spec_request import EndpointHTTPSpecRequest  # noqa: PLC0415
        from ..models.endpoint_icmp_spec_request import EndpointICMPSpecRequest  # noqa: PLC0415
        from ..models.endpoint_retry_spec_request import EndpointRetrySpecRequest  # noqa: PLC0415
        from ..models.endpoint_tcp_spec_request import EndpointTCPSpecRequest  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_retry(data: object) -> EndpointRetrySpecRequest | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                retry_type_1 = EndpointRetrySpecRequest.from_dict(data)

                return retry_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EndpointRetrySpecRequest | None | Unset, data)

        retry = _parse_retry(d.pop("retry", UNSET))

        def _parse_http(data: object) -> EndpointHTTPSpecRequest | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                http_type_1 = EndpointHTTPSpecRequest.from_dict(data)

                return http_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EndpointHTTPSpecRequest | None | Unset, data)

        http = _parse_http(d.pop("http", UNSET))

        def _parse_icmp(data: object) -> EndpointICMPSpecRequest | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                icmp_type_1 = EndpointICMPSpecRequest.from_dict(data)

                return icmp_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EndpointICMPSpecRequest | None | Unset, data)

        icmp = _parse_icmp(d.pop("icmp", UNSET))

        def _parse_tcp(data: object) -> EndpointTCPSpecRequest | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tcp_type_1 = EndpointTCPSpecRequest.from_dict(data)

                return tcp_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EndpointTCPSpecRequest | None | Unset, data)

        tcp = _parse_tcp(d.pop("tcp", UNSET))

        def _parse_dns(data: object) -> EndpointDNSSpecRequest | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dns_type_1 = EndpointDNSSpecRequest.from_dict(data)

                return dns_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EndpointDNSSpecRequest | None | Unset, data)

        dns = _parse_dns(d.pop("dns", UNSET))

        endpoint_spec_request = cls(
            retry=retry,
            http=http,
            icmp=icmp,
            tcp=tcp,
            dns=dns,
        )

        endpoint_spec_request.additional_properties = d
        return endpoint_spec_request

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
