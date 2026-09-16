from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.object_tasks_list_response_tasks_item import ObjectTasksListResponseTasksItem


T = TypeVar("T", bound="ObjectTasksListResponse")


@_attrs_define
class ObjectTasksListResponse:
    """
    Attributes:
        count_running (int):
        tasks (list[ObjectTasksListResponseTasksItem]):
    """

    count_running: int
    tasks: list[ObjectTasksListResponseTasksItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count_running = self.count_running

        tasks = []
        for tasks_item_data in self.tasks:
            tasks_item = tasks_item_data.to_dict()
            tasks.append(tasks_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count_running": count_running,
                "tasks": tasks,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.object_tasks_list_response_tasks_item import ObjectTasksListResponseTasksItem  # noqa: PLC0415

        d = dict(src_dict)
        count_running = d.pop("count_running")

        tasks = []
        _tasks = d.pop("tasks")
        for tasks_item_data in _tasks:
            tasks_item = ObjectTasksListResponseTasksItem.from_dict(tasks_item_data)

            tasks.append(tasks_item)

        object_tasks_list_response = cls(
            count_running=count_running,
            tasks=tasks,
        )

        object_tasks_list_response.additional_properties = d
        return object_tasks_list_response

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
