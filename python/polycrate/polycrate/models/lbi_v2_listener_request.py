from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.lbi_v2_listener_request_protocol import (
    LbiV2ListenerRequestProtocol,
    check_lbi_v2_listener_request_protocol,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lbi_v2_tls_request import LbiV2TlsRequest


T = TypeVar("T", bound="LbiV2ListenerRequest")


@_attrs_define
class LbiV2ListenerRequest:
    """
    Attributes:
        name (str):
        port (int):
        protocol (LbiV2ListenerRequestProtocol): * `HTTP` - HTTP
            * `HTTPS` - HTTPS
            * `TLS` - TLS
            * `TCP` - TCP
            * `GRPC` - GRPC
        hostname (None | str | Unset):
        tls (LbiV2TlsRequest | None | Unset):
    """

    name: str
    port: int
    protocol: LbiV2ListenerRequestProtocol
    hostname: None | str | Unset = UNSET
    tls: LbiV2TlsRequest | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.lbi_v2_tls_request import LbiV2TlsRequest  # noqa: PLC0415

        name = self.name

        port = self.port

        protocol: str = self.protocol

        hostname: None | str | Unset
        if isinstance(self.hostname, Unset):
            hostname = UNSET
        else:
            hostname = self.hostname

        tls: dict[str, Any] | None | Unset
        if isinstance(self.tls, Unset):
            tls = UNSET
        elif isinstance(self.tls, LbiV2TlsRequest):
            tls = self.tls.to_dict()
        else:
            tls = self.tls

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "port": port,
                "protocol": protocol,
            }
        )
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if tls is not UNSET:
            field_dict["tls"] = tls

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lbi_v2_tls_request import LbiV2TlsRequest  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        port = d.pop("port")

        protocol = check_lbi_v2_listener_request_protocol(d.pop("protocol"))

        def _parse_hostname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hostname = _parse_hostname(d.pop("hostname", UNSET))

        def _parse_tls(data: object) -> LbiV2TlsRequest | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tls_type_1 = LbiV2TlsRequest.from_dict(data)

                return tls_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LbiV2TlsRequest | None | Unset, data)

        tls = _parse_tls(d.pop("tls", UNSET))

        lbi_v2_listener_request = cls(
            name=name,
            port=port,
            protocol=protocol,
            hostname=hostname,
            tls=tls,
        )

        lbi_v2_listener_request.additional_properties = d
        return lbi_v2_listener_request

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
