from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckResultInputRequest")


@_attrs_define
class CheckResultInputRequest:
    """Serializer for individual check results in health submission.

    These are submitted by the operator along with the health report
    and stored in EndpointAgentAssignment.

    Per .specs/0.11.9/index.md - Sektion 4

        Attributes:
            endpoint_id (UUID): UUID of the endpoint that was checked
            success (bool): Whether the check was successful
            checked_at (datetime.datetime | Unset): When the check was performed (RFC3339)
            status_code (int | None | Unset): HTTP status code (for HTTP endpoints)
            error_code (int | Unset): Error code (0 = no error) Default: 0.
            error_name (str | Unset): Human-readable error name Default: ''.
            duration_ms (int | None | Unset): Check duration in milliseconds
            ssl_cert_not_after (datetime.datetime | None | Unset): TLS certificate NotAfter timestamp (HTTPS endpoints only)
            http_dns_lookup_ms (int | None | Unset): DNS lookup duration in milliseconds
            http_tcp_connect_ms (int | None | Unset): TCP connection duration in milliseconds
            http_tls_handshake_ms (int | None | Unset): TLS handshake duration in milliseconds
            http_time_to_first_byte_ms (int | None | Unset): Time to first byte in milliseconds
            http_response_size_bytes (int | None | Unset): HTTP response body size in bytes
            http_tls_version (None | str | Unset): TLS version string (e.g. 'TLS 1.3')
            http_resolved_ip (None | str | Unset): Resolved IP address of the endpoint hostname (HTTP legacy)
            resolved_ip (None | str | Unset): Resolved IP address of the endpoint hostname (generic, all check types)
            http_error_category (None | str | Unset): Error category
                (timeout/connection/dns/network/response/configuration/other)
            http_tls_valid (bool | None | Unset): Whether the TLS certificate is currently valid
            http_tls_days_until_expiry (int | None | Unset): Days until TLS certificate expiry
            http_tls_issuer (None | str | Unset): TLS certificate issuer CommonName
            http_tls_subject (None | str | Unset): TLS certificate subject CommonName
            icmp_rtt_ms (float | None | Unset): Average round-trip time in milliseconds
            icmp_packet_loss_percent (float | None | Unset): Packet loss percentage (0.0–100.0)
            icmp_packets_sent (int | None | Unset): Number of ICMP packets sent
            icmp_packets_received (int | None | Unset): Number of ICMP packets received
            icmp_min_rtt_ms (float | None | Unset): Minimum RTT across packets in milliseconds
            icmp_max_rtt_ms (float | None | Unset): Maximum RTT across packets in milliseconds
            tcp_connected (bool | None | Unset): Whether the TCP connection was established
            tcp_banner (None | str | Unset): First bytes sent by the server after connection
            tcp_response_matched (bool | None | Unset): Whether the expected_response was found in the server
                response/banner
            dns_rcode (None | str | Unset): DNS RCODE string (NOERROR, NXDOMAIN, SERVFAIL, ...)
            dns_records (list[str] | None | Unset): DNS answer records as strings
            dns_matched (bool | None | Unset): Whether the DNS response matched the expected_results
            dns_query_time_ms (int | None | Unset): DNS query RTT in milliseconds
            dns_protocol (None | str | Unset): Protocol used: udp, tcp, tcp-tls
            dns_record_type (None | str | Unset): DNS record type queried: A, AAAA, CNAME, MX, ...
            dns_dnssec_valid (bool | None | Unset): Whether the DNSSEC Authenticated Data flag was set in the response
    """

    endpoint_id: UUID
    success: bool
    checked_at: datetime.datetime | Unset = UNSET
    status_code: int | None | Unset = UNSET
    error_code: int | Unset = 0
    error_name: str | Unset = ""
    duration_ms: int | None | Unset = UNSET
    ssl_cert_not_after: datetime.datetime | None | Unset = UNSET
    http_dns_lookup_ms: int | None | Unset = UNSET
    http_tcp_connect_ms: int | None | Unset = UNSET
    http_tls_handshake_ms: int | None | Unset = UNSET
    http_time_to_first_byte_ms: int | None | Unset = UNSET
    http_response_size_bytes: int | None | Unset = UNSET
    http_tls_version: None | str | Unset = UNSET
    http_resolved_ip: None | str | Unset = UNSET
    resolved_ip: None | str | Unset = UNSET
    http_error_category: None | str | Unset = UNSET
    http_tls_valid: bool | None | Unset = UNSET
    http_tls_days_until_expiry: int | None | Unset = UNSET
    http_tls_issuer: None | str | Unset = UNSET
    http_tls_subject: None | str | Unset = UNSET
    icmp_rtt_ms: float | None | Unset = UNSET
    icmp_packet_loss_percent: float | None | Unset = UNSET
    icmp_packets_sent: int | None | Unset = UNSET
    icmp_packets_received: int | None | Unset = UNSET
    icmp_min_rtt_ms: float | None | Unset = UNSET
    icmp_max_rtt_ms: float | None | Unset = UNSET
    tcp_connected: bool | None | Unset = UNSET
    tcp_banner: None | str | Unset = UNSET
    tcp_response_matched: bool | None | Unset = UNSET
    dns_rcode: None | str | Unset = UNSET
    dns_records: list[str] | None | Unset = UNSET
    dns_matched: bool | None | Unset = UNSET
    dns_query_time_ms: int | None | Unset = UNSET
    dns_protocol: None | str | Unset = UNSET
    dns_record_type: None | str | Unset = UNSET
    dns_dnssec_valid: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        endpoint_id = str(self.endpoint_id)

        success = self.success

        checked_at: str | Unset = UNSET
        if not isinstance(self.checked_at, Unset):
            checked_at = self.checked_at.isoformat()

        status_code: int | None | Unset
        if isinstance(self.status_code, Unset):
            status_code = UNSET
        else:
            status_code = self.status_code

        error_code = self.error_code

        error_name = self.error_name

        duration_ms: int | None | Unset
        if isinstance(self.duration_ms, Unset):
            duration_ms = UNSET
        else:
            duration_ms = self.duration_ms

        ssl_cert_not_after: None | str | Unset
        if isinstance(self.ssl_cert_not_after, Unset):
            ssl_cert_not_after = UNSET
        elif isinstance(self.ssl_cert_not_after, datetime.datetime):
            ssl_cert_not_after = self.ssl_cert_not_after.isoformat()
        else:
            ssl_cert_not_after = self.ssl_cert_not_after

        http_dns_lookup_ms: int | None | Unset
        if isinstance(self.http_dns_lookup_ms, Unset):
            http_dns_lookup_ms = UNSET
        else:
            http_dns_lookup_ms = self.http_dns_lookup_ms

        http_tcp_connect_ms: int | None | Unset
        if isinstance(self.http_tcp_connect_ms, Unset):
            http_tcp_connect_ms = UNSET
        else:
            http_tcp_connect_ms = self.http_tcp_connect_ms

        http_tls_handshake_ms: int | None | Unset
        if isinstance(self.http_tls_handshake_ms, Unset):
            http_tls_handshake_ms = UNSET
        else:
            http_tls_handshake_ms = self.http_tls_handshake_ms

        http_time_to_first_byte_ms: int | None | Unset
        if isinstance(self.http_time_to_first_byte_ms, Unset):
            http_time_to_first_byte_ms = UNSET
        else:
            http_time_to_first_byte_ms = self.http_time_to_first_byte_ms

        http_response_size_bytes: int | None | Unset
        if isinstance(self.http_response_size_bytes, Unset):
            http_response_size_bytes = UNSET
        else:
            http_response_size_bytes = self.http_response_size_bytes

        http_tls_version: None | str | Unset
        if isinstance(self.http_tls_version, Unset):
            http_tls_version = UNSET
        else:
            http_tls_version = self.http_tls_version

        http_resolved_ip: None | str | Unset
        if isinstance(self.http_resolved_ip, Unset):
            http_resolved_ip = UNSET
        else:
            http_resolved_ip = self.http_resolved_ip

        resolved_ip: None | str | Unset
        if isinstance(self.resolved_ip, Unset):
            resolved_ip = UNSET
        else:
            resolved_ip = self.resolved_ip

        http_error_category: None | str | Unset
        if isinstance(self.http_error_category, Unset):
            http_error_category = UNSET
        else:
            http_error_category = self.http_error_category

        http_tls_valid: bool | None | Unset
        if isinstance(self.http_tls_valid, Unset):
            http_tls_valid = UNSET
        else:
            http_tls_valid = self.http_tls_valid

        http_tls_days_until_expiry: int | None | Unset
        if isinstance(self.http_tls_days_until_expiry, Unset):
            http_tls_days_until_expiry = UNSET
        else:
            http_tls_days_until_expiry = self.http_tls_days_until_expiry

        http_tls_issuer: None | str | Unset
        if isinstance(self.http_tls_issuer, Unset):
            http_tls_issuer = UNSET
        else:
            http_tls_issuer = self.http_tls_issuer

        http_tls_subject: None | str | Unset
        if isinstance(self.http_tls_subject, Unset):
            http_tls_subject = UNSET
        else:
            http_tls_subject = self.http_tls_subject

        icmp_rtt_ms: float | None | Unset
        if isinstance(self.icmp_rtt_ms, Unset):
            icmp_rtt_ms = UNSET
        else:
            icmp_rtt_ms = self.icmp_rtt_ms

        icmp_packet_loss_percent: float | None | Unset
        if isinstance(self.icmp_packet_loss_percent, Unset):
            icmp_packet_loss_percent = UNSET
        else:
            icmp_packet_loss_percent = self.icmp_packet_loss_percent

        icmp_packets_sent: int | None | Unset
        if isinstance(self.icmp_packets_sent, Unset):
            icmp_packets_sent = UNSET
        else:
            icmp_packets_sent = self.icmp_packets_sent

        icmp_packets_received: int | None | Unset
        if isinstance(self.icmp_packets_received, Unset):
            icmp_packets_received = UNSET
        else:
            icmp_packets_received = self.icmp_packets_received

        icmp_min_rtt_ms: float | None | Unset
        if isinstance(self.icmp_min_rtt_ms, Unset):
            icmp_min_rtt_ms = UNSET
        else:
            icmp_min_rtt_ms = self.icmp_min_rtt_ms

        icmp_max_rtt_ms: float | None | Unset
        if isinstance(self.icmp_max_rtt_ms, Unset):
            icmp_max_rtt_ms = UNSET
        else:
            icmp_max_rtt_ms = self.icmp_max_rtt_ms

        tcp_connected: bool | None | Unset
        if isinstance(self.tcp_connected, Unset):
            tcp_connected = UNSET
        else:
            tcp_connected = self.tcp_connected

        tcp_banner: None | str | Unset
        if isinstance(self.tcp_banner, Unset):
            tcp_banner = UNSET
        else:
            tcp_banner = self.tcp_banner

        tcp_response_matched: bool | None | Unset
        if isinstance(self.tcp_response_matched, Unset):
            tcp_response_matched = UNSET
        else:
            tcp_response_matched = self.tcp_response_matched

        dns_rcode: None | str | Unset
        if isinstance(self.dns_rcode, Unset):
            dns_rcode = UNSET
        else:
            dns_rcode = self.dns_rcode

        dns_records: list[str] | None | Unset
        if isinstance(self.dns_records, Unset):
            dns_records = UNSET
        elif isinstance(self.dns_records, list):
            dns_records = self.dns_records

        else:
            dns_records = self.dns_records

        dns_matched: bool | None | Unset
        if isinstance(self.dns_matched, Unset):
            dns_matched = UNSET
        else:
            dns_matched = self.dns_matched

        dns_query_time_ms: int | None | Unset
        if isinstance(self.dns_query_time_ms, Unset):
            dns_query_time_ms = UNSET
        else:
            dns_query_time_ms = self.dns_query_time_ms

        dns_protocol: None | str | Unset
        if isinstance(self.dns_protocol, Unset):
            dns_protocol = UNSET
        else:
            dns_protocol = self.dns_protocol

        dns_record_type: None | str | Unset
        if isinstance(self.dns_record_type, Unset):
            dns_record_type = UNSET
        else:
            dns_record_type = self.dns_record_type

        dns_dnssec_valid: bool | None | Unset
        if isinstance(self.dns_dnssec_valid, Unset):
            dns_dnssec_valid = UNSET
        else:
            dns_dnssec_valid = self.dns_dnssec_valid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endpoint_id": endpoint_id,
                "success": success,
            }
        )
        if checked_at is not UNSET:
            field_dict["checked_at"] = checked_at
        if status_code is not UNSET:
            field_dict["status_code"] = status_code
        if error_code is not UNSET:
            field_dict["error_code"] = error_code
        if error_name is not UNSET:
            field_dict["error_name"] = error_name
        if duration_ms is not UNSET:
            field_dict["duration_ms"] = duration_ms
        if ssl_cert_not_after is not UNSET:
            field_dict["ssl_cert_not_after"] = ssl_cert_not_after
        if http_dns_lookup_ms is not UNSET:
            field_dict["http_dns_lookup_ms"] = http_dns_lookup_ms
        if http_tcp_connect_ms is not UNSET:
            field_dict["http_tcp_connect_ms"] = http_tcp_connect_ms
        if http_tls_handshake_ms is not UNSET:
            field_dict["http_tls_handshake_ms"] = http_tls_handshake_ms
        if http_time_to_first_byte_ms is not UNSET:
            field_dict["http_time_to_first_byte_ms"] = http_time_to_first_byte_ms
        if http_response_size_bytes is not UNSET:
            field_dict["http_response_size_bytes"] = http_response_size_bytes
        if http_tls_version is not UNSET:
            field_dict["http_tls_version"] = http_tls_version
        if http_resolved_ip is not UNSET:
            field_dict["http_resolved_ip"] = http_resolved_ip
        if resolved_ip is not UNSET:
            field_dict["resolved_ip"] = resolved_ip
        if http_error_category is not UNSET:
            field_dict["http_error_category"] = http_error_category
        if http_tls_valid is not UNSET:
            field_dict["http_tls_valid"] = http_tls_valid
        if http_tls_days_until_expiry is not UNSET:
            field_dict["http_tls_days_until_expiry"] = http_tls_days_until_expiry
        if http_tls_issuer is not UNSET:
            field_dict["http_tls_issuer"] = http_tls_issuer
        if http_tls_subject is not UNSET:
            field_dict["http_tls_subject"] = http_tls_subject
        if icmp_rtt_ms is not UNSET:
            field_dict["icmp_rtt_ms"] = icmp_rtt_ms
        if icmp_packet_loss_percent is not UNSET:
            field_dict["icmp_packet_loss_percent"] = icmp_packet_loss_percent
        if icmp_packets_sent is not UNSET:
            field_dict["icmp_packets_sent"] = icmp_packets_sent
        if icmp_packets_received is not UNSET:
            field_dict["icmp_packets_received"] = icmp_packets_received
        if icmp_min_rtt_ms is not UNSET:
            field_dict["icmp_min_rtt_ms"] = icmp_min_rtt_ms
        if icmp_max_rtt_ms is not UNSET:
            field_dict["icmp_max_rtt_ms"] = icmp_max_rtt_ms
        if tcp_connected is not UNSET:
            field_dict["tcp_connected"] = tcp_connected
        if tcp_banner is not UNSET:
            field_dict["tcp_banner"] = tcp_banner
        if tcp_response_matched is not UNSET:
            field_dict["tcp_response_matched"] = tcp_response_matched
        if dns_rcode is not UNSET:
            field_dict["dns_rcode"] = dns_rcode
        if dns_records is not UNSET:
            field_dict["dns_records"] = dns_records
        if dns_matched is not UNSET:
            field_dict["dns_matched"] = dns_matched
        if dns_query_time_ms is not UNSET:
            field_dict["dns_query_time_ms"] = dns_query_time_ms
        if dns_protocol is not UNSET:
            field_dict["dns_protocol"] = dns_protocol
        if dns_record_type is not UNSET:
            field_dict["dns_record_type"] = dns_record_type
        if dns_dnssec_valid is not UNSET:
            field_dict["dns_dnssec_valid"] = dns_dnssec_valid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        endpoint_id = UUID(d.pop("endpoint_id"))

        success = d.pop("success")

        _checked_at = d.pop("checked_at", UNSET)
        checked_at: datetime.datetime | Unset
        if isinstance(_checked_at, Unset):
            checked_at = UNSET
        else:
            checked_at = datetime.datetime.fromisoformat(_checked_at)

        def _parse_status_code(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        status_code = _parse_status_code(d.pop("status_code", UNSET))

        error_code = d.pop("error_code", UNSET)

        error_name = d.pop("error_name", UNSET)

        def _parse_duration_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        duration_ms = _parse_duration_ms(d.pop("duration_ms", UNSET))

        def _parse_ssl_cert_not_after(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ssl_cert_not_after_type_0 = datetime.datetime.fromisoformat(data)

                return ssl_cert_not_after_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        ssl_cert_not_after = _parse_ssl_cert_not_after(d.pop("ssl_cert_not_after", UNSET))

        def _parse_http_dns_lookup_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        http_dns_lookup_ms = _parse_http_dns_lookup_ms(d.pop("http_dns_lookup_ms", UNSET))

        def _parse_http_tcp_connect_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        http_tcp_connect_ms = _parse_http_tcp_connect_ms(d.pop("http_tcp_connect_ms", UNSET))

        def _parse_http_tls_handshake_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        http_tls_handshake_ms = _parse_http_tls_handshake_ms(d.pop("http_tls_handshake_ms", UNSET))

        def _parse_http_time_to_first_byte_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        http_time_to_first_byte_ms = _parse_http_time_to_first_byte_ms(d.pop("http_time_to_first_byte_ms", UNSET))

        def _parse_http_response_size_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        http_response_size_bytes = _parse_http_response_size_bytes(d.pop("http_response_size_bytes", UNSET))

        def _parse_http_tls_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        http_tls_version = _parse_http_tls_version(d.pop("http_tls_version", UNSET))

        def _parse_http_resolved_ip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        http_resolved_ip = _parse_http_resolved_ip(d.pop("http_resolved_ip", UNSET))

        def _parse_resolved_ip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resolved_ip = _parse_resolved_ip(d.pop("resolved_ip", UNSET))

        def _parse_http_error_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        http_error_category = _parse_http_error_category(d.pop("http_error_category", UNSET))

        def _parse_http_tls_valid(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        http_tls_valid = _parse_http_tls_valid(d.pop("http_tls_valid", UNSET))

        def _parse_http_tls_days_until_expiry(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        http_tls_days_until_expiry = _parse_http_tls_days_until_expiry(d.pop("http_tls_days_until_expiry", UNSET))

        def _parse_http_tls_issuer(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        http_tls_issuer = _parse_http_tls_issuer(d.pop("http_tls_issuer", UNSET))

        def _parse_http_tls_subject(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        http_tls_subject = _parse_http_tls_subject(d.pop("http_tls_subject", UNSET))

        def _parse_icmp_rtt_ms(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        icmp_rtt_ms = _parse_icmp_rtt_ms(d.pop("icmp_rtt_ms", UNSET))

        def _parse_icmp_packet_loss_percent(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        icmp_packet_loss_percent = _parse_icmp_packet_loss_percent(d.pop("icmp_packet_loss_percent", UNSET))

        def _parse_icmp_packets_sent(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        icmp_packets_sent = _parse_icmp_packets_sent(d.pop("icmp_packets_sent", UNSET))

        def _parse_icmp_packets_received(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        icmp_packets_received = _parse_icmp_packets_received(d.pop("icmp_packets_received", UNSET))

        def _parse_icmp_min_rtt_ms(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        icmp_min_rtt_ms = _parse_icmp_min_rtt_ms(d.pop("icmp_min_rtt_ms", UNSET))

        def _parse_icmp_max_rtt_ms(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        icmp_max_rtt_ms = _parse_icmp_max_rtt_ms(d.pop("icmp_max_rtt_ms", UNSET))

        def _parse_tcp_connected(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        tcp_connected = _parse_tcp_connected(d.pop("tcp_connected", UNSET))

        def _parse_tcp_banner(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tcp_banner = _parse_tcp_banner(d.pop("tcp_banner", UNSET))

        def _parse_tcp_response_matched(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        tcp_response_matched = _parse_tcp_response_matched(d.pop("tcp_response_matched", UNSET))

        def _parse_dns_rcode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dns_rcode = _parse_dns_rcode(d.pop("dns_rcode", UNSET))

        def _parse_dns_records(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                dns_records_type_0 = cast(list[str], data)

                return dns_records_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        dns_records = _parse_dns_records(d.pop("dns_records", UNSET))

        def _parse_dns_matched(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        dns_matched = _parse_dns_matched(d.pop("dns_matched", UNSET))

        def _parse_dns_query_time_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        dns_query_time_ms = _parse_dns_query_time_ms(d.pop("dns_query_time_ms", UNSET))

        def _parse_dns_protocol(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dns_protocol = _parse_dns_protocol(d.pop("dns_protocol", UNSET))

        def _parse_dns_record_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dns_record_type = _parse_dns_record_type(d.pop("dns_record_type", UNSET))

        def _parse_dns_dnssec_valid(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        dns_dnssec_valid = _parse_dns_dnssec_valid(d.pop("dns_dnssec_valid", UNSET))

        check_result_input_request = cls(
            endpoint_id=endpoint_id,
            success=success,
            checked_at=checked_at,
            status_code=status_code,
            error_code=error_code,
            error_name=error_name,
            duration_ms=duration_ms,
            ssl_cert_not_after=ssl_cert_not_after,
            http_dns_lookup_ms=http_dns_lookup_ms,
            http_tcp_connect_ms=http_tcp_connect_ms,
            http_tls_handshake_ms=http_tls_handshake_ms,
            http_time_to_first_byte_ms=http_time_to_first_byte_ms,
            http_response_size_bytes=http_response_size_bytes,
            http_tls_version=http_tls_version,
            http_resolved_ip=http_resolved_ip,
            resolved_ip=resolved_ip,
            http_error_category=http_error_category,
            http_tls_valid=http_tls_valid,
            http_tls_days_until_expiry=http_tls_days_until_expiry,
            http_tls_issuer=http_tls_issuer,
            http_tls_subject=http_tls_subject,
            icmp_rtt_ms=icmp_rtt_ms,
            icmp_packet_loss_percent=icmp_packet_loss_percent,
            icmp_packets_sent=icmp_packets_sent,
            icmp_packets_received=icmp_packets_received,
            icmp_min_rtt_ms=icmp_min_rtt_ms,
            icmp_max_rtt_ms=icmp_max_rtt_ms,
            tcp_connected=tcp_connected,
            tcp_banner=tcp_banner,
            tcp_response_matched=tcp_response_matched,
            dns_rcode=dns_rcode,
            dns_records=dns_records,
            dns_matched=dns_matched,
            dns_query_time_ms=dns_query_time_ms,
            dns_protocol=dns_protocol,
            dns_record_type=dns_record_type,
            dns_dnssec_valid=dns_dnssec_valid,
        )

        check_result_input_request.additional_properties = d
        return check_result_input_request

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
