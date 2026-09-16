from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum

if TYPE_CHECKING:
    from ..models.condition_instance_list_active_condition_instances_item import (
        ConditionInstanceListActiveConditionInstancesItem,
    )
    from ..models.condition_instance_list_created import ConditionInstanceListCreated
    from ..models.condition_instance_list_organization_type_0 import ConditionInstanceListOrganizationType0
    from ..models.condition_instance_list_workspace_type_0 import ConditionInstanceListWorkspaceType0


T = TypeVar("T", bound="ConditionInstanceList")


@_attrs_define
class ConditionInstanceList:
    """List serializer for ConditionInstance.

    Attributes:
        id (UUID):
        name (str): Gibt die bevorzugte UI-Anzeige (display_name) zurück.
        state (LastStateEnum): * `OK` - Ok
            * `WARNING` - Warning
            * `CRITICAL` - Critical
            * `READY` - Ready
            * `DEGRADED` - Degraded
            * `DOWN` - Down
        labels (Any):
        conditions (Any): Conditions are managed by the API and will be added during the reconcile phase. Some
            conditions are `degrading`, meaning an object becomes DEGRADED if it has such a condition.
        condition_instance_count (int): Number of active ConditionInstances linked to this object (Spec 419).
            Uses prefetched data (_prefetched_active_conditions) when available to avoid N+1.
        active_condition_instances (list[ConditionInstanceListActiveConditionInstancesItem]):
        organization (ConditionInstanceListOrganizationType0 | None):
        organization_priority (bool): True when the object's organization has priority=True.
        workspace (ConditionInstanceListWorkspaceType0 | None):
        created (ConditionInstanceListCreated):
        archived (bool): Archived objects are not shown in the UI and are not managed by the API.
        reconciliation_running (bool):
        effective_criticality (EffectiveCriticalityEnum | None):
        url (str): Gibt die absolute URL zum Object zurück.
        condition (UUID):
        condition_name (str):
        condition_severity (str):
        object_id (None | UUID):
        object_display (str): Return a best-effort display string for the linked object.
        object_url (str): Return the generic object-detail URL for the affected object.
        reason (str):
        active (bool):
        active_label (str):
        resolved_at (datetime.datetime | None):
    """

    id: UUID
    name: str
    state: LastStateEnum
    labels: Any
    conditions: Any
    condition_instance_count: int
    active_condition_instances: list[ConditionInstanceListActiveConditionInstancesItem]
    organization: ConditionInstanceListOrganizationType0 | None
    organization_priority: bool
    workspace: ConditionInstanceListWorkspaceType0 | None
    created: ConditionInstanceListCreated
    archived: bool
    reconciliation_running: bool
    effective_criticality: EffectiveCriticalityEnum | None
    url: str
    condition: UUID
    condition_name: str
    condition_severity: str
    object_id: None | UUID
    object_display: str
    object_url: str
    reason: str
    active: bool
    active_label: str
    resolved_at: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.condition_instance_list_organization_type_0 import (
            ConditionInstanceListOrganizationType0,  # noqa: PLC0415
        )
        from ..models.condition_instance_list_workspace_type_0 import (
            ConditionInstanceListWorkspaceType0,  # noqa: PLC0415
        )

        id = str(self.id)

        name = self.name

        state: str = self.state

        labels = self.labels

        conditions = self.conditions

        condition_instance_count = self.condition_instance_count

        active_condition_instances = []
        for active_condition_instances_item_data in self.active_condition_instances:
            active_condition_instances_item = active_condition_instances_item_data.to_dict()
            active_condition_instances.append(active_condition_instances_item)

        organization: dict[str, Any] | None
        if isinstance(self.organization, ConditionInstanceListOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        organization_priority = self.organization_priority

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, ConditionInstanceListWorkspaceType0):
            workspace = self.workspace.to_dict()
        else:
            workspace = self.workspace

        created = self.created.to_dict()

        archived = self.archived

        reconciliation_running = self.reconciliation_running

        effective_criticality: None | str
        if isinstance(self.effective_criticality, str):
            effective_criticality = self.effective_criticality
        else:
            effective_criticality = self.effective_criticality

        url = self.url

        condition = str(self.condition)

        condition_name = self.condition_name

        condition_severity = self.condition_severity

        object_id: None | str
        if isinstance(self.object_id, UUID):
            object_id = str(self.object_id)
        else:
            object_id = self.object_id

        object_display = self.object_display

        object_url = self.object_url

        reason = self.reason

        active = self.active

        active_label = self.active_label

        resolved_at: None | str
        if isinstance(self.resolved_at, datetime.datetime):
            resolved_at = self.resolved_at.isoformat()
        else:
            resolved_at = self.resolved_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "state": state,
                "labels": labels,
                "conditions": conditions,
                "condition_instance_count": condition_instance_count,
                "active_condition_instances": active_condition_instances,
                "organization": organization,
                "organization_priority": organization_priority,
                "workspace": workspace,
                "created": created,
                "archived": archived,
                "reconciliation_running": reconciliation_running,
                "effective_criticality": effective_criticality,
                "url": url,
                "condition": condition,
                "condition_name": condition_name,
                "condition_severity": condition_severity,
                "object_id": object_id,
                "object_display": object_display,
                "object_url": object_url,
                "reason": reason,
                "active": active,
                "active_label": active_label,
                "resolved_at": resolved_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.condition_instance_list_active_condition_instances_item import (
            ConditionInstanceListActiveConditionInstancesItem,  # noqa: PLC0415
        )
        from ..models.condition_instance_list_created import ConditionInstanceListCreated  # noqa: PLC0415
        from ..models.condition_instance_list_organization_type_0 import (
            ConditionInstanceListOrganizationType0,  # noqa: PLC0415
        )
        from ..models.condition_instance_list_workspace_type_0 import (
            ConditionInstanceListWorkspaceType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        state = check_last_state_enum(d.pop("state"))

        labels = d.pop("labels")

        conditions = d.pop("conditions")

        condition_instance_count = d.pop("condition_instance_count")

        active_condition_instances = []
        _active_condition_instances = d.pop("active_condition_instances")
        for active_condition_instances_item_data in _active_condition_instances:
            active_condition_instances_item = ConditionInstanceListActiveConditionInstancesItem.from_dict(
                active_condition_instances_item_data
            )

            active_condition_instances.append(active_condition_instances_item)

        def _parse_organization(data: object) -> ConditionInstanceListOrganizationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = ConditionInstanceListOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConditionInstanceListOrganizationType0 | None, data)

        organization = _parse_organization(d.pop("organization"))

        organization_priority = d.pop("organization_priority")

        def _parse_workspace(data: object) -> ConditionInstanceListWorkspaceType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = ConditionInstanceListWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConditionInstanceListWorkspaceType0 | None, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = ConditionInstanceListCreated.from_dict(d.pop("created"))

        archived = d.pop("archived")

        reconciliation_running = d.pop("reconciliation_running")

        def _parse_effective_criticality(data: object) -> EffectiveCriticalityEnum | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_criticality_type_0 = check_effective_criticality_enum(data)

                return effective_criticality_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EffectiveCriticalityEnum | None, data)

        effective_criticality = _parse_effective_criticality(d.pop("effective_criticality"))

        url = d.pop("url")

        condition = UUID(d.pop("condition"))

        condition_name = d.pop("condition_name")

        condition_severity = d.pop("condition_severity")

        def _parse_object_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                object_id_type_0 = UUID(data)

                return object_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        object_id = _parse_object_id(d.pop("object_id"))

        object_display = d.pop("object_display")

        object_url = d.pop("object_url")

        reason = d.pop("reason")

        active = d.pop("active")

        active_label = d.pop("active_label")

        def _parse_resolved_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resolved_at_type_0 = datetime.datetime.fromisoformat(data)

                return resolved_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        resolved_at = _parse_resolved_at(d.pop("resolved_at"))

        condition_instance_list = cls(
            id=id,
            name=name,
            state=state,
            labels=labels,
            conditions=conditions,
            condition_instance_count=condition_instance_count,
            active_condition_instances=active_condition_instances,
            organization=organization,
            organization_priority=organization_priority,
            workspace=workspace,
            created=created,
            archived=archived,
            reconciliation_running=reconciliation_running,
            effective_criticality=effective_criticality,
            url=url,
            condition=condition,
            condition_name=condition_name,
            condition_severity=condition_severity,
            object_id=object_id,
            object_display=object_display,
            object_url=object_url,
            reason=reason,
            active=active,
            active_label=active_label,
            resolved_at=resolved_at,
        )

        condition_instance_list.additional_properties = d
        return condition_instance_list

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
