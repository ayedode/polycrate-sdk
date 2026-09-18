from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.principal_kind_enum import PrincipalKindEnum, check_principal_kind_enum

T = TypeVar("T", bound="McpSession")


@_attrs_define
class McpSession:
    """
    Attributes:
        id (UUID):
        principal_kind (PrincipalKindEnum): * `user` - User
            * `system_api_key` - System API key
            * `org_api_key` - Organization API key
            * `microservice` - Microservice
        principal_label (str):
        client (str):
        prompt (str):
        started_at (datetime.datetime):
        ended_at (datetime.datetime | None):
        last_activity_at (datetime.datetime):
        tool_call_count (int):
        denied_count (int):
        error_count (int):
        is_active (bool):
    """

    id: UUID
    principal_kind: PrincipalKindEnum
    principal_label: str
    client: str
    prompt: str
    started_at: datetime.datetime
    ended_at: datetime.datetime | None
    last_activity_at: datetime.datetime
    tool_call_count: int
    denied_count: int
    error_count: int
    is_active: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        principal_kind: str = self.principal_kind

        principal_label = self.principal_label

        client = self.client

        prompt = self.prompt

        started_at = self.started_at.isoformat()

        ended_at: None | str
        if isinstance(self.ended_at, datetime.datetime):
            ended_at = self.ended_at.isoformat()
        else:
            ended_at = self.ended_at

        last_activity_at = self.last_activity_at.isoformat()

        tool_call_count = self.tool_call_count

        denied_count = self.denied_count

        error_count = self.error_count

        is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "principal_kind": principal_kind,
                "principal_label": principal_label,
                "client": client,
                "prompt": prompt,
                "started_at": started_at,
                "ended_at": ended_at,
                "last_activity_at": last_activity_at,
                "tool_call_count": tool_call_count,
                "denied_count": denied_count,
                "error_count": error_count,
                "is_active": is_active,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        principal_kind = check_principal_kind_enum(d.pop("principal_kind"))

        principal_label = d.pop("principal_label")

        client = d.pop("client")

        prompt = d.pop("prompt")

        started_at = datetime.datetime.fromisoformat(d.pop("started_at"))

        def _parse_ended_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ended_at_type_0 = datetime.datetime.fromisoformat(data)

                return ended_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        ended_at = _parse_ended_at(d.pop("ended_at"))

        last_activity_at = datetime.datetime.fromisoformat(d.pop("last_activity_at"))

        tool_call_count = d.pop("tool_call_count")

        denied_count = d.pop("denied_count")

        error_count = d.pop("error_count")

        is_active = d.pop("is_active")

        mcp_session = cls(
            id=id,
            principal_kind=principal_kind,
            principal_label=principal_label,
            client=client,
            prompt=prompt,
            started_at=started_at,
            ended_at=ended_at,
            last_activity_at=last_activity_at,
            tool_call_count=tool_call_count,
            denied_count=denied_count,
            error_count=error_count,
            is_active=is_active,
        )

        mcp_session.additional_properties = d
        return mcp_session

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
