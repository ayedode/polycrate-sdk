from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MaintenanceWindowStatus")


@_attrs_define
class MaintenanceWindowStatus:
    """Response serializer for the maintenance-window-status workspace action (Spec 220).
    Reports whether the workspace is currently within an active maintenance window.

        Attributes:
            in_maintenance_window (bool):
            window_id (None | UUID):
            window_name (None | str):
            window_display_name (None | str):
    """

    in_maintenance_window: bool
    window_id: None | UUID
    window_name: None | str
    window_display_name: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        in_maintenance_window = self.in_maintenance_window

        window_id: None | str
        if isinstance(self.window_id, UUID):
            window_id = str(self.window_id)
        else:
            window_id = self.window_id

        window_name: None | str
        window_name = self.window_name

        window_display_name: None | str
        window_display_name = self.window_display_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "in_maintenance_window": in_maintenance_window,
                "window_id": window_id,
                "window_name": window_name,
                "window_display_name": window_display_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        in_maintenance_window = d.pop("in_maintenance_window")

        def _parse_window_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                window_id_type_0 = UUID(data)

                return window_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        window_id = _parse_window_id(d.pop("window_id"))

        def _parse_window_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        window_name = _parse_window_name(d.pop("window_name"))

        def _parse_window_display_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        window_display_name = _parse_window_display_name(d.pop("window_display_name"))

        maintenance_window_status = cls(
            in_maintenance_window=in_maintenance_window,
            window_id=window_id,
            window_name=window_name,
            window_display_name=window_display_name,
        )

        maintenance_window_status.additional_properties = d
        return maintenance_window_status

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
