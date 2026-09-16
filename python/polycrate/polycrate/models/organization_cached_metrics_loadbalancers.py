from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OrganizationCachedMetricsLoadbalancers")


@_attrs_define
class OrganizationCachedMetricsLoadbalancers:
    """
    Attributes:
        count (int): Non-archived owned plus Loopback-delegated load balancer count
        traffic_30d_bytes (int): 30-day traffic in bytes for owned plus Loopback-delegated load balancers
    """

    count: int
    traffic_30d_bytes: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        traffic_30d_bytes = self.traffic_30d_bytes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "traffic_30d_bytes": traffic_30d_bytes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count")

        traffic_30d_bytes = d.pop("traffic_30d_bytes")

        organization_cached_metrics_loadbalancers = cls(
            count=count,
            traffic_30d_bytes=traffic_30d_bytes,
        )

        organization_cached_metrics_loadbalancers.additional_properties = d
        return organization_cached_metrics_loadbalancers

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
