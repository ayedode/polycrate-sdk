from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lbi_v2_backend_request import LbiV2BackendRequest
    from ..models.lbi_v2_listener_request import LbiV2ListenerRequest
    from ..models.lbi_v2_observability_request import LbiV2ObservabilityRequest
    from ..models.lbi_v2_route_request import LbiV2RouteRequest
    from ..models.lbi_v2_security_request import LbiV2SecurityRequest
    from ..models.lbi_v2_traffic_request import LbiV2TrafficRequest


T = TypeVar("T", bound="LbiV2SpecRequest")


@_attrs_define
class LbiV2SpecRequest:
    """SoT for LoadbalancerInstance.spec when engine_version=2.

    Attributes:
        listeners (list[LbiV2ListenerRequest]):
        routes (list[LbiV2RouteRequest]):
        backends (list[LbiV2BackendRequest]):
        security (LbiV2SecurityRequest | None | Unset):
        traffic (LbiV2TrafficRequest | None | Unset):
        observability (LbiV2ObservabilityRequest | None | Unset):
    """

    listeners: list[LbiV2ListenerRequest]
    routes: list[LbiV2RouteRequest]
    backends: list[LbiV2BackendRequest]
    security: LbiV2SecurityRequest | None | Unset = UNSET
    traffic: LbiV2TrafficRequest | None | Unset = UNSET
    observability: LbiV2ObservabilityRequest | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.lbi_v2_observability_request import LbiV2ObservabilityRequest  # noqa: PLC0415
        from ..models.lbi_v2_security_request import LbiV2SecurityRequest  # noqa: PLC0415
        from ..models.lbi_v2_traffic_request import LbiV2TrafficRequest  # noqa: PLC0415

        listeners = []
        for listeners_item_data in self.listeners:
            listeners_item = listeners_item_data.to_dict()
            listeners.append(listeners_item)

        routes = []
        for routes_item_data in self.routes:
            routes_item = routes_item_data.to_dict()
            routes.append(routes_item)

        backends = []
        for backends_item_data in self.backends:
            backends_item = backends_item_data.to_dict()
            backends.append(backends_item)

        security: dict[str, Any] | None | Unset
        if isinstance(self.security, Unset):
            security = UNSET
        elif isinstance(self.security, LbiV2SecurityRequest):
            security = self.security.to_dict()
        else:
            security = self.security

        traffic: dict[str, Any] | None | Unset
        if isinstance(self.traffic, Unset):
            traffic = UNSET
        elif isinstance(self.traffic, LbiV2TrafficRequest):
            traffic = self.traffic.to_dict()
        else:
            traffic = self.traffic

        observability: dict[str, Any] | None | Unset
        if isinstance(self.observability, Unset):
            observability = UNSET
        elif isinstance(self.observability, LbiV2ObservabilityRequest):
            observability = self.observability.to_dict()
        else:
            observability = self.observability

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "listeners": listeners,
                "routes": routes,
                "backends": backends,
            }
        )
        if security is not UNSET:
            field_dict["security"] = security
        if traffic is not UNSET:
            field_dict["traffic"] = traffic
        if observability is not UNSET:
            field_dict["observability"] = observability

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lbi_v2_backend_request import LbiV2BackendRequest  # noqa: PLC0415
        from ..models.lbi_v2_listener_request import LbiV2ListenerRequest  # noqa: PLC0415
        from ..models.lbi_v2_observability_request import LbiV2ObservabilityRequest  # noqa: PLC0415
        from ..models.lbi_v2_route_request import LbiV2RouteRequest  # noqa: PLC0415
        from ..models.lbi_v2_security_request import LbiV2SecurityRequest  # noqa: PLC0415
        from ..models.lbi_v2_traffic_request import LbiV2TrafficRequest  # noqa: PLC0415

        d = dict(src_dict)
        listeners = []
        _listeners = d.pop("listeners")
        for listeners_item_data in _listeners:
            listeners_item = LbiV2ListenerRequest.from_dict(listeners_item_data)

            listeners.append(listeners_item)

        routes = []
        _routes = d.pop("routes")
        for routes_item_data in _routes:
            routes_item = LbiV2RouteRequest.from_dict(routes_item_data)

            routes.append(routes_item)

        backends = []
        _backends = d.pop("backends")
        for backends_item_data in _backends:
            backends_item = LbiV2BackendRequest.from_dict(backends_item_data)

            backends.append(backends_item)

        def _parse_security(data: object) -> LbiV2SecurityRequest | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                security_type_1 = LbiV2SecurityRequest.from_dict(data)

                return security_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LbiV2SecurityRequest | None | Unset, data)

        security = _parse_security(d.pop("security", UNSET))

        def _parse_traffic(data: object) -> LbiV2TrafficRequest | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                traffic_type_1 = LbiV2TrafficRequest.from_dict(data)

                return traffic_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LbiV2TrafficRequest | None | Unset, data)

        traffic = _parse_traffic(d.pop("traffic", UNSET))

        def _parse_observability(data: object) -> LbiV2ObservabilityRequest | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                observability_type_1 = LbiV2ObservabilityRequest.from_dict(data)

                return observability_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LbiV2ObservabilityRequest | None | Unset, data)

        observability = _parse_observability(d.pop("observability", UNSET))

        lbi_v2_spec_request = cls(
            listeners=listeners,
            routes=routes,
            backends=backends,
            security=security,
            traffic=traffic,
            observability=observability,
        )

        lbi_v2_spec_request.additional_properties = d
        return lbi_v2_spec_request

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
