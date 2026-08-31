from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CLIActivitySubmissionResponse")


@_attrs_define
class CLIActivitySubmissionResponse:
    """Response serializer for CLI activity creation (POST).

    Attributes:
        success (bool): Whether the submission was successful
        activity_id (UUID): UUID of the created Activity
        activity_url (str): Absolute URL for PATCH update
    """

    success: bool
    activity_id: UUID
    activity_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        activity_id = str(self.activity_id)

        activity_url = self.activity_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "activity_id": activity_id,
                "activity_url": activity_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        activity_id = UUID(d.pop("activity_id"))

        activity_url = d.pop("activity_url")

        cli_activity_submission_response = cls(
            success=success,
            activity_id=activity_id,
            activity_url=activity_url,
        )

        cli_activity_submission_response.additional_properties = d
        return cli_activity_submission_response

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
