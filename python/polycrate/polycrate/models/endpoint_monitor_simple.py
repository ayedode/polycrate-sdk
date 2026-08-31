from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.endpoint_monitor_kind_enum import EndpointMonitorKindEnum, check_endpoint_monitor_kind_enum

T = TypeVar("T", bound="EndpointMonitorSimple")


@_attrs_define
class EndpointMonitorSimple:
    """
    Attributes:
        id (UUID):
        name (str):
        reconciliation_running (bool):
        kind (EndpointMonitorKindEnum): * `uptime-kuma` - Uptime Kuma
        managed_by_content_type (int | None):
        managed_by_object_id (None | str):
    """

    id: UUID
    name: str
    reconciliation_running: bool
    kind: EndpointMonitorKindEnum
    managed_by_content_type: int | None
    managed_by_object_id: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        reconciliation_running = self.reconciliation_running

        kind: str = self.kind

        managed_by_content_type: int | None
        managed_by_content_type = self.managed_by_content_type

        managed_by_object_id: None | str
        managed_by_object_id = self.managed_by_object_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "reconciliation_running": reconciliation_running,
                "kind": kind,
                "managed_by_content_type": managed_by_content_type,
                "managed_by_object_id": managed_by_object_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        reconciliation_running = d.pop("reconciliation_running")

        kind = check_endpoint_monitor_kind_enum(d.pop("kind"))

        def _parse_managed_by_content_type(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        managed_by_content_type = _parse_managed_by_content_type(d.pop("managed_by_content_type"))

        def _parse_managed_by_object_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        managed_by_object_id = _parse_managed_by_object_id(d.pop("managed_by_object_id"))

        endpoint_monitor_simple = cls(
            id=id,
            name=name,
            reconciliation_running=reconciliation_running,
            kind=kind,
            managed_by_content_type=managed_by_content_type,
            managed_by_object_id=managed_by_object_id,
        )

        endpoint_monitor_simple.additional_properties = d
        return endpoint_monitor_simple

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
