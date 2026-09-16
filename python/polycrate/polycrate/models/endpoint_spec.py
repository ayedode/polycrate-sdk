from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.endpoint_dns_spec import EndpointDNSSpec
    from ..models.endpoint_http_spec import EndpointHTTPSpec
    from ..models.endpoint_icmp_spec import EndpointICMPSpec
    from ..models.endpoint_retry_spec import EndpointRetrySpec
    from ..models.endpoint_tcp_spec import EndpointTCPSpec


T = TypeVar("T", bound="EndpointSpec")


@_attrs_define
class EndpointSpec:
    """Typed representation of the endpoint spec JSONField.
    Each sub-serializer covers one check kind; unused kinds are omitted (null).
    Consumed by the Go operator/agent via the generated API client.

        Attributes:
            retry (EndpointRetrySpec | None | Unset):
            http (EndpointHTTPSpec | None | Unset):
            icmp (EndpointICMPSpec | None | Unset):
            tcp (EndpointTCPSpec | None | Unset):
            dns (EndpointDNSSpec | None | Unset):
    """

    retry: EndpointRetrySpec | None | Unset = UNSET
    http: EndpointHTTPSpec | None | Unset = UNSET
    icmp: EndpointICMPSpec | None | Unset = UNSET
    tcp: EndpointTCPSpec | None | Unset = UNSET
    dns: EndpointDNSSpec | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.endpoint_dns_spec import EndpointDNSSpec  # noqa: PLC0415
        from ..models.endpoint_http_spec import EndpointHTTPSpec  # noqa: PLC0415
        from ..models.endpoint_icmp_spec import EndpointICMPSpec  # noqa: PLC0415
        from ..models.endpoint_retry_spec import EndpointRetrySpec  # noqa: PLC0415
        from ..models.endpoint_tcp_spec import EndpointTCPSpec  # noqa: PLC0415

        retry: dict[str, Any] | None | Unset
        if isinstance(self.retry, Unset):
            retry = UNSET
        elif isinstance(self.retry, EndpointRetrySpec):
            retry = self.retry.to_dict()
        else:
            retry = self.retry

        http: dict[str, Any] | None | Unset
        if isinstance(self.http, Unset):
            http = UNSET
        elif isinstance(self.http, EndpointHTTPSpec):
            http = self.http.to_dict()
        else:
            http = self.http

        icmp: dict[str, Any] | None | Unset
        if isinstance(self.icmp, Unset):
            icmp = UNSET
        elif isinstance(self.icmp, EndpointICMPSpec):
            icmp = self.icmp.to_dict()
        else:
            icmp = self.icmp

        tcp: dict[str, Any] | None | Unset
        if isinstance(self.tcp, Unset):
            tcp = UNSET
        elif isinstance(self.tcp, EndpointTCPSpec):
            tcp = self.tcp.to_dict()
        else:
            tcp = self.tcp

        dns: dict[str, Any] | None | Unset
        if isinstance(self.dns, Unset):
            dns = UNSET
        elif isinstance(self.dns, EndpointDNSSpec):
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
        from ..models.endpoint_dns_spec import EndpointDNSSpec  # noqa: PLC0415
        from ..models.endpoint_http_spec import EndpointHTTPSpec  # noqa: PLC0415
        from ..models.endpoint_icmp_spec import EndpointICMPSpec  # noqa: PLC0415
        from ..models.endpoint_retry_spec import EndpointRetrySpec  # noqa: PLC0415
        from ..models.endpoint_tcp_spec import EndpointTCPSpec  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_retry(data: object) -> EndpointRetrySpec | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                retry_type_1 = EndpointRetrySpec.from_dict(data)

                return retry_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EndpointRetrySpec | None | Unset, data)

        retry = _parse_retry(d.pop("retry", UNSET))

        def _parse_http(data: object) -> EndpointHTTPSpec | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                http_type_1 = EndpointHTTPSpec.from_dict(data)

                return http_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EndpointHTTPSpec | None | Unset, data)

        http = _parse_http(d.pop("http", UNSET))

        def _parse_icmp(data: object) -> EndpointICMPSpec | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                icmp_type_1 = EndpointICMPSpec.from_dict(data)

                return icmp_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EndpointICMPSpec | None | Unset, data)

        icmp = _parse_icmp(d.pop("icmp", UNSET))

        def _parse_tcp(data: object) -> EndpointTCPSpec | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tcp_type_1 = EndpointTCPSpec.from_dict(data)

                return tcp_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EndpointTCPSpec | None | Unset, data)

        tcp = _parse_tcp(d.pop("tcp", UNSET))

        def _parse_dns(data: object) -> EndpointDNSSpec | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dns_type_1 = EndpointDNSSpec.from_dict(data)

                return dns_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EndpointDNSSpec | None | Unset, data)

        dns = _parse_dns(d.pop("dns", UNSET))

        endpoint_spec = cls(
            retry=retry,
            http=http,
            icmp=icmp,
            tcp=tcp,
            dns=dns,
        )

        endpoint_spec.additional_properties = d
        return endpoint_spec

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
