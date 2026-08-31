from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ReconcileAlreadyRunningResponse")


@_attrs_define
class ReconcileAlreadyRunningResponse:
    """
    Attributes:
        status (str):
        reconciliation_running (bool):
        message (str):
    """

    status: str
    reconciliation_running: bool
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        reconciliation_running = self.reconciliation_running

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "reconciliation_running": reconciliation_running,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = d.pop("status")

        reconciliation_running = d.pop("reconciliation_running")

        message = d.pop("message")

        reconcile_already_running_response = cls(
            status=status,
            reconciliation_running=reconciliation_running,
            message=message,
        )

        reconcile_already_running_response.additional_properties = d
        return reconcile_already_running_response

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
