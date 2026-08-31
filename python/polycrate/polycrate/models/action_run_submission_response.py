from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ActionRunSubmissionResponse")


@_attrs_define
class ActionRunSubmissionResponse:
    """Response serializer for CLI action run submission.

    Used both for OpenAPI schema generation AND actual response serialization
    to ensure consistency between documentation and implementation.

        Attributes:
            success (bool): Whether the submission was successful
            action_run_id (UUID): UUID of the created ActionRun
            status (str): Status of the ActionRun (success/failed)
            message (str): Human-readable status message
            action_run_url (str): Absolute URL to view the ActionRun in the UI
    """

    success: bool
    action_run_id: UUID
    status: str
    message: str
    action_run_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        action_run_id = str(self.action_run_id)

        status = self.status

        message = self.message

        action_run_url = self.action_run_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "action_run_id": action_run_id,
                "status": status,
                "message": message,
                "action_run_url": action_run_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        action_run_id = UUID(d.pop("action_run_id"))

        status = d.pop("status")

        message = d.pop("message")

        action_run_url = d.pop("action_run_url")

        action_run_submission_response = cls(
            success=success,
            action_run_id=action_run_id,
            status=status,
            message=message,
            action_run_url=action_run_url,
        )

        action_run_submission_response.additional_properties = d
        return action_run_submission_response

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
