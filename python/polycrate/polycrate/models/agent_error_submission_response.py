from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AgentErrorSubmissionResponse")


@_attrs_define
class AgentErrorSubmissionResponse:
    """
    Attributes:
        status (str): Always "success"
        agent_id (UUID): Platform agent ID
        error_id (UUID): Stored error report ID
    """

    status: str
    agent_id: UUID
    error_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        agent_id = str(self.agent_id)

        error_id = str(self.error_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "agent_id": agent_id,
                "error_id": error_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = d.pop("status")

        agent_id = UUID(d.pop("agent_id"))

        error_id = UUID(d.pop("error_id"))

        agent_error_submission_response = cls(
            status=status,
            agent_id=agent_id,
            error_id=error_id,
        )

        agent_error_submission_response.additional_properties = d
        return agent_error_submission_response

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
