from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ReconcileStartedResponse")


@_attrs_define
class ReconcileStartedResponse:
    """
    Attributes:
        status (str):
        task_id (str):
        object_id (str):
        object_type (str):
        reconciliation_running (bool):
    """

    status: str
    task_id: str
    object_id: str
    object_type: str
    reconciliation_running: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        task_id = self.task_id

        object_id = self.object_id

        object_type = self.object_type

        reconciliation_running = self.reconciliation_running

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "task_id": task_id,
                "object_id": object_id,
                "object_type": object_type,
                "reconciliation_running": reconciliation_running,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = d.pop("status")

        task_id = d.pop("task_id")

        object_id = d.pop("object_id")

        object_type = d.pop("object_type")

        reconciliation_running = d.pop("reconciliation_running")

        reconcile_started_response = cls(
            status=status,
            task_id=task_id,
            object_id=object_id,
            object_type=object_type,
            reconciliation_running=reconciliation_running,
        )

        reconcile_started_response.additional_properties = d
        return reconcile_started_response

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
