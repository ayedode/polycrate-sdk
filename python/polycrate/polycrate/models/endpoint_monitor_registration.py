from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.endpoint_monitor_simple import EndpointMonitorSimple
    from ..models.endpoint_simple import EndpointSimple


T = TypeVar("T", bound="EndpointMonitorRegistration")


@_attrs_define
class EndpointMonitorRegistration:
    """
    Attributes:
        endpoint (EndpointSimple):
        endpoint_monitor (EndpointMonitorSimple):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    endpoint: EndpointSimple
    endpoint_monitor: EndpointMonitorSimple
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        endpoint = self.endpoint.to_dict()

        endpoint_monitor = self.endpoint_monitor.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endpoint": endpoint,
                "endpoint_monitor": endpoint_monitor,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.endpoint_monitor_simple import EndpointMonitorSimple
        from ..models.endpoint_simple import EndpointSimple

        d = dict(src_dict)
        endpoint = EndpointSimple.from_dict(d.pop("endpoint"))

        endpoint_monitor = EndpointMonitorSimple.from_dict(d.pop("endpoint_monitor"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        endpoint_monitor_registration = cls(
            endpoint=endpoint,
            endpoint_monitor=endpoint_monitor,
            created_at=created_at,
            updated_at=updated_at,
        )

        endpoint_monitor_registration.additional_properties = d
        return endpoint_monitor_registration

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
