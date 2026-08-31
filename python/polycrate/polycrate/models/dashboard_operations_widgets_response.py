from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dashboard_operations_widgets_response_lb_traffic import DashboardOperationsWidgetsResponseLbTraffic
    from ..models.dashboard_operations_widgets_response_s3_storage import DashboardOperationsWidgetsResponseS3Storage


T = TypeVar("T", bound="DashboardOperationsWidgetsResponse")


@_attrs_define
class DashboardOperationsWidgetsResponse:
    """
    Attributes:
        updated_at (datetime.datetime):
        s3_storage (DashboardOperationsWidgetsResponseS3Storage):
        lb_traffic (DashboardOperationsWidgetsResponseLbTraffic):
    """

    updated_at: datetime.datetime
    s3_storage: DashboardOperationsWidgetsResponseS3Storage
    lb_traffic: DashboardOperationsWidgetsResponseLbTraffic
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        updated_at = self.updated_at.isoformat()

        s3_storage = self.s3_storage.to_dict()

        lb_traffic = self.lb_traffic.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "updated_at": updated_at,
                "s3_storage": s3_storage,
                "lb_traffic": lb_traffic,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_operations_widgets_response_lb_traffic import (
            DashboardOperationsWidgetsResponseLbTraffic,
        )
        from ..models.dashboard_operations_widgets_response_s3_storage import (
            DashboardOperationsWidgetsResponseS3Storage,
        )

        d = dict(src_dict)
        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        s3_storage = DashboardOperationsWidgetsResponseS3Storage.from_dict(d.pop("s3_storage"))

        lb_traffic = DashboardOperationsWidgetsResponseLbTraffic.from_dict(d.pop("lb_traffic"))

        dashboard_operations_widgets_response = cls(
            updated_at=updated_at,
            s3_storage=s3_storage,
            lb_traffic=lb_traffic,
        )

        dashboard_operations_widgets_response.additional_properties = d
        return dashboard_operations_widgets_response

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
