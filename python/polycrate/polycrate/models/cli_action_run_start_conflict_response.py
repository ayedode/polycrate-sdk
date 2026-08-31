from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cli_action_run_start_conflict import CLIActionRunStartConflict


T = TypeVar("T", bound="CLIActionRunStartConflictResponse")


@_attrs_define
class CLIActionRunStartConflictResponse:
    """
    Attributes:
        success (bool):
        error (str):
        conflict (CLIActionRunStartConflict):
    """

    success: bool
    error: str
    conflict: CLIActionRunStartConflict
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        error = self.error

        conflict = self.conflict.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "error": error,
                "conflict": conflict,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cli_action_run_start_conflict import CLIActionRunStartConflict

        d = dict(src_dict)
        success = d.pop("success")

        error = d.pop("error")

        conflict = CLIActionRunStartConflict.from_dict(d.pop("conflict"))

        cli_action_run_start_conflict_response = cls(
            success=success,
            error=error,
            conflict=conflict,
        )

        cli_action_run_start_conflict_response.additional_properties = d
        return cli_action_run_start_conflict_response

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
