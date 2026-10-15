from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.lbi_v2_backend_request_kind import LbiV2BackendRequestKind, check_lbi_v2_backend_request_kind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lbi_v2_backend_request_circuit_breaker import LbiV2BackendRequestCircuitBreaker
    from ..models.lbi_v2_backend_target_request import LbiV2BackendTargetRequest
    from ..models.lbi_v2_backend_tls_request import LbiV2BackendTlsRequest
    from ..models.lbi_v2_health_check_request import LbiV2HealthCheckRequest
    from ..models.lbi_v2_load_balancing_request import LbiV2LoadBalancingRequest


T = TypeVar("T", bound="LbiV2BackendRequest")


@_attrs_define
class LbiV2BackendRequest:
    """
    Attributes:
        name (str):
        kind (LbiV2BackendRequestKind): * `fqdn` - fqdn
            * `ip` - ip
        targets (list[LbiV2BackendTargetRequest]):
        tls (LbiV2BackendTlsRequest | None | Unset):
        health_check (LbiV2HealthCheckRequest | None | Unset):
        load_balancing (LbiV2LoadBalancingRequest | None | Unset):
        circuit_breaker (LbiV2BackendRequestCircuitBreaker | Unset):
    """

    name: str
    kind: LbiV2BackendRequestKind
    targets: list[LbiV2BackendTargetRequest]
    tls: LbiV2BackendTlsRequest | None | Unset = UNSET
    health_check: LbiV2HealthCheckRequest | None | Unset = UNSET
    load_balancing: LbiV2LoadBalancingRequest | None | Unset = UNSET
    circuit_breaker: LbiV2BackendRequestCircuitBreaker | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.lbi_v2_backend_tls_request import LbiV2BackendTlsRequest  # noqa: PLC0415
        from ..models.lbi_v2_health_check_request import LbiV2HealthCheckRequest  # noqa: PLC0415
        from ..models.lbi_v2_load_balancing_request import LbiV2LoadBalancingRequest  # noqa: PLC0415

        name = self.name

        kind: str = self.kind

        targets = []
        for targets_item_data in self.targets:
            targets_item = targets_item_data.to_dict()
            targets.append(targets_item)

        tls: dict[str, Any] | None | Unset
        if isinstance(self.tls, Unset):
            tls = UNSET
        elif isinstance(self.tls, LbiV2BackendTlsRequest):
            tls = self.tls.to_dict()
        else:
            tls = self.tls

        health_check: dict[str, Any] | None | Unset
        if isinstance(self.health_check, Unset):
            health_check = UNSET
        elif isinstance(self.health_check, LbiV2HealthCheckRequest):
            health_check = self.health_check.to_dict()
        else:
            health_check = self.health_check

        load_balancing: dict[str, Any] | None | Unset
        if isinstance(self.load_balancing, Unset):
            load_balancing = UNSET
        elif isinstance(self.load_balancing, LbiV2LoadBalancingRequest):
            load_balancing = self.load_balancing.to_dict()
        else:
            load_balancing = self.load_balancing

        circuit_breaker: dict[str, Any] | Unset = UNSET
        if not isinstance(self.circuit_breaker, Unset):
            circuit_breaker = self.circuit_breaker.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "kind": kind,
                "targets": targets,
            }
        )
        if tls is not UNSET:
            field_dict["tls"] = tls
        if health_check is not UNSET:
            field_dict["healthCheck"] = health_check
        if load_balancing is not UNSET:
            field_dict["loadBalancing"] = load_balancing
        if circuit_breaker is not UNSET:
            field_dict["circuitBreaker"] = circuit_breaker

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lbi_v2_backend_request_circuit_breaker import LbiV2BackendRequestCircuitBreaker  # noqa: PLC0415
        from ..models.lbi_v2_backend_target_request import LbiV2BackendTargetRequest  # noqa: PLC0415
        from ..models.lbi_v2_backend_tls_request import LbiV2BackendTlsRequest  # noqa: PLC0415
        from ..models.lbi_v2_health_check_request import LbiV2HealthCheckRequest  # noqa: PLC0415
        from ..models.lbi_v2_load_balancing_request import LbiV2LoadBalancingRequest  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        kind = check_lbi_v2_backend_request_kind(d.pop("kind"))

        targets = []
        _targets = d.pop("targets")
        for targets_item_data in _targets:
            targets_item = LbiV2BackendTargetRequest.from_dict(targets_item_data)

            targets.append(targets_item)

        def _parse_tls(data: object) -> LbiV2BackendTlsRequest | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tls_type_1 = LbiV2BackendTlsRequest.from_dict(data)

                return tls_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LbiV2BackendTlsRequest | None | Unset, data)

        tls = _parse_tls(d.pop("tls", UNSET))

        def _parse_health_check(data: object) -> LbiV2HealthCheckRequest | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                health_check_type_1 = LbiV2HealthCheckRequest.from_dict(data)

                return health_check_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LbiV2HealthCheckRequest | None | Unset, data)

        health_check = _parse_health_check(d.pop("healthCheck", UNSET))

        def _parse_load_balancing(data: object) -> LbiV2LoadBalancingRequest | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                load_balancing_type_1 = LbiV2LoadBalancingRequest.from_dict(data)

                return load_balancing_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LbiV2LoadBalancingRequest | None | Unset, data)

        load_balancing = _parse_load_balancing(d.pop("loadBalancing", UNSET))

        _circuit_breaker = d.pop("circuitBreaker", UNSET)
        circuit_breaker: LbiV2BackendRequestCircuitBreaker | Unset
        if isinstance(_circuit_breaker, Unset):
            circuit_breaker = UNSET
        else:
            circuit_breaker = LbiV2BackendRequestCircuitBreaker.from_dict(_circuit_breaker)

        lbi_v2_backend_request = cls(
            name=name,
            kind=kind,
            targets=targets,
            tls=tls,
            health_check=health_check,
            load_balancing=load_balancing,
            circuit_breaker=circuit_breaker,
        )

        lbi_v2_backend_request.additional_properties = d
        return lbi_v2_backend_request

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
