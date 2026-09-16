from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.workspace_simple import WorkspaceSimple


T = TypeVar("T", bound="DowntimeAffectedObject")


@_attrs_define
class DowntimeAffectedObject:
    """Full serializer for DowntimeAffectedObject.

    Attributes:
        id (UUID):
        object_type (str):
        object_id (str):
        object_name (str):
        affected_from (datetime.datetime): When this specific object went into downtime
        affected_until (datetime.datetime | None): When this object became available again (null = still DOWN)
        trigger_condition (None | str): The condition that triggered the downtime
        workspace (WorkspaceSimple):
        duration_str (str): Human-readable duration for this object.
        is_recovered (bool): Whether this object has recovered.
    """

    id: UUID
    object_type: str
    object_id: str
    object_name: str
    affected_from: datetime.datetime
    affected_until: datetime.datetime | None
    trigger_condition: None | str
    workspace: WorkspaceSimple
    duration_str: str
    is_recovered: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        object_type = self.object_type

        object_id = self.object_id

        object_name = self.object_name

        affected_from = self.affected_from.isoformat()

        affected_until: None | str
        if isinstance(self.affected_until, datetime.datetime):
            affected_until = self.affected_until.isoformat()
        else:
            affected_until = self.affected_until

        trigger_condition: None | str
        trigger_condition = self.trigger_condition

        workspace = self.workspace.to_dict()

        duration_str = self.duration_str

        is_recovered = self.is_recovered

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "object_type": object_type,
                "object_id": object_id,
                "object_name": object_name,
                "affected_from": affected_from,
                "affected_until": affected_until,
                "trigger_condition": trigger_condition,
                "workspace": workspace,
                "duration_str": duration_str,
                "is_recovered": is_recovered,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workspace_simple import WorkspaceSimple  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        object_type = d.pop("object_type")

        object_id = d.pop("object_id")

        object_name = d.pop("object_name")

        affected_from = datetime.datetime.fromisoformat(d.pop("affected_from"))

        def _parse_affected_until(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                affected_until_type_0 = datetime.datetime.fromisoformat(data)

                return affected_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        affected_until = _parse_affected_until(d.pop("affected_until"))

        def _parse_trigger_condition(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        trigger_condition = _parse_trigger_condition(d.pop("trigger_condition"))

        workspace = WorkspaceSimple.from_dict(d.pop("workspace"))

        duration_str = d.pop("duration_str")

        is_recovered = d.pop("is_recovered")

        downtime_affected_object = cls(
            id=id,
            object_type=object_type,
            object_id=object_id,
            object_name=object_name,
            affected_from=affected_from,
            affected_until=affected_until,
            trigger_condition=trigger_condition,
            workspace=workspace,
            duration_str=duration_str,
            is_recovered=is_recovered,
        )

        downtime_affected_object.additional_properties = d
        return downtime_affected_object

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
