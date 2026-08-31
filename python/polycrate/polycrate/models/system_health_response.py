from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.overall_status_enum import OverallStatusEnum, check_overall_status_enum

if TYPE_CHECKING:
    from ..models.system_health_response_services import SystemHealthResponseServices


T = TypeVar("T", bound="SystemHealthResponse")


@_attrs_define
class SystemHealthResponse:
    """
    Attributes:
        timestamp (datetime.datetime):
        overall_status (OverallStatusEnum): * `HEALTHY` - HEALTHY
            * `DEGRADED` - DEGRADED
            * `UNHEALTHY` - UNHEALTHY
            * `UNKNOWN` - UNKNOWN
        services (SystemHealthResponseServices):
    """

    timestamp: datetime.datetime
    overall_status: OverallStatusEnum
    services: SystemHealthResponseServices
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp.isoformat()

        overall_status: str = self.overall_status

        services = self.services.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "overall_status": overall_status,
                "services": services,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.system_health_response_services import SystemHealthResponseServices

        d = dict(src_dict)
        timestamp = datetime.datetime.fromisoformat(d.pop("timestamp"))

        overall_status = check_overall_status_enum(d.pop("overall_status"))

        services = SystemHealthResponseServices.from_dict(d.pop("services"))

        system_health_response = cls(
            timestamp=timestamp,
            overall_status=overall_status,
            services=services,
        )

        system_health_response.additional_properties = d
        return system_health_response

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
