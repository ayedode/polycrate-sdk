from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CLIActionRunStartConflict")


@_attrs_define
class CLIActionRunStartConflict:
    """
    Attributes:
        action_run_id (str):
        action (str):
        status (str):
        started_at (None | str):
        action_run_url (str):
    """

    action_run_id: str
    action: str
    status: str
    started_at: None | str
    action_run_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_run_id = self.action_run_id

        action = self.action

        status = self.status

        started_at: None | str
        started_at = self.started_at

        action_run_url = self.action_run_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action_run_id": action_run_id,
                "action": action,
                "status": status,
                "started_at": started_at,
                "action_run_url": action_run_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action_run_id = d.pop("action_run_id")

        action = d.pop("action")

        status = d.pop("status")

        def _parse_started_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        started_at = _parse_started_at(d.pop("started_at"))

        action_run_url = d.pop("action_run_url")

        cli_action_run_start_conflict = cls(
            action_run_id=action_run_id,
            action=action,
            status=status,
            started_at=started_at,
            action_run_url=action_run_url,
        )

        cli_action_run_start_conflict.additional_properties = d
        return cli_action_run_start_conflict

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
