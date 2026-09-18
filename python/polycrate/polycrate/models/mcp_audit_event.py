from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.access_enum import AccessEnum, check_access_enum
from ..models.outcome_enum import OutcomeEnum, check_outcome_enum

T = TypeVar("T", bound="McpAuditEvent")


@_attrs_define
class McpAuditEvent:
    """
    Attributes:
        id (UUID):
        session (UUID):
        tool (str):
        access (AccessEnum): * `read` - Read
            * `write` - Write
        outcome (OutcomeEnum): * `ok` - OK
            * `denied` - Denied
            * `error` - Error
        detail (str):
        target_type (str):
        target_id (str):
        payload (Any):
        actor_label (str):
        created_at (datetime.datetime):
    """

    id: UUID
    session: UUID
    tool: str
    access: AccessEnum
    outcome: OutcomeEnum
    detail: str
    target_type: str
    target_id: str
    payload: Any
    actor_label: str
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        session = str(self.session)

        tool = self.tool

        access: str = self.access

        outcome: str = self.outcome

        detail = self.detail

        target_type = self.target_type

        target_id = self.target_id

        payload = self.payload

        actor_label = self.actor_label

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "session": session,
                "tool": tool,
                "access": access,
                "outcome": outcome,
                "detail": detail,
                "target_type": target_type,
                "target_id": target_id,
                "payload": payload,
                "actor_label": actor_label,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        session = UUID(d.pop("session"))

        tool = d.pop("tool")

        access = check_access_enum(d.pop("access"))

        outcome = check_outcome_enum(d.pop("outcome"))

        detail = d.pop("detail")

        target_type = d.pop("target_type")

        target_id = d.pop("target_id")

        payload = d.pop("payload")

        actor_label = d.pop("actor_label")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        mcp_audit_event = cls(
            id=id,
            session=session,
            tool=tool,
            access=access,
            outcome=outcome,
            detail=detail,
            target_type=target_type,
            target_id=target_id,
            payload=payload,
            actor_label=actor_label,
            created_at=created_at,
        )

        mcp_audit_event.additional_properties = d
        return mcp_audit_event

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
