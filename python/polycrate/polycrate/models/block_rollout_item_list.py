from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.block_rollout_item_status_enum import BlockRolloutItemStatusEnum, check_block_rollout_item_status_enum
from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum
from ..models.source_98d_enum import Source98DEnum, check_source_98d_enum

if TYPE_CHECKING:
    from ..models.block_rollout_item_list_active_condition_instances_item import (
        BlockRolloutItemListActiveConditionInstancesItem,
    )
    from ..models.block_rollout_item_list_created import BlockRolloutItemListCreated
    from ..models.block_rollout_item_list_organization_type_0 import BlockRolloutItemListOrganizationType0
    from ..models.block_rollout_item_list_workspace_type_0 import BlockRolloutItemListWorkspaceType0


T = TypeVar("T", bound="BlockRolloutItemList")


@_attrs_define
class BlockRolloutItemList:
    """Basis-Serializer für alle ManagedObject List-Endpoints.

    Liefert die generischen Felder die alle ManagedObjects teilen:
    - id: UUID
    - name: String-Repräsentation des Objects (__str__)
    - state: Object State
    - organization: Organization (id, slug, name)
    - workspace: Workspace (id, name) oder None
    - created: Kombifeld (created_at, created_at_humanized, created_at_display, created_by)

    Subclasses müssen:
    - model in Meta definieren
    - Zusätzliche model-spezifische Felder in Meta.fields hinzufügen

    Usage:
        class K8sClusterListSerializer(ManagedObjectListSerializer):
            class Meta(ManagedObjectListSerializer.Meta):
                model = K8sCluster
                fields = ManagedObjectListSerializer.Meta.fields + ['kubernetes_version', 'kind']

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
            active_condition_instances (list[BlockRolloutItemListActiveConditionInstancesItem]):
            organization (BlockRolloutItemListOrganizationType0 | None):
            organization_priority (bool): True when the object's organization has priority=True.
            workspace (BlockRolloutItemListWorkspaceType0 | None):
            created (BlockRolloutItemListCreated):
            archived (bool): Archived objects are not shown in the UI and are not managed by the API.
            reconciliation_running (bool):
            effective_criticality (EffectiveCriticalityEnum | None):
            url (str): Gibt die absolute URL zum Object zurück.
            block (UUID):
            block_name (str):
            action_name (str):
            status (BlockRolloutItemStatusEnum): * `pending` - Pending
                * `in_progress` - In Progress
                * `completed` - Completed
                * `failed` - Failed
                * `retrying` - Retrying
                * `skipped` - Skipped
            source (Source98DEnum): * `scheduler` - Scheduler
                * `manual` - Manual
            retry_count (int):
            dispatched_at (datetime.datetime | None):
            completed_at (datetime.datetime | None):
            rendered_target_version (None | str):
    """

    id: UUID
    name: str
    state: LastStateEnum
    labels: Any
    conditions: Any
    condition_instance_count: int
    active_condition_instances: list[BlockRolloutItemListActiveConditionInstancesItem]
    organization: BlockRolloutItemListOrganizationType0 | None
    organization_priority: bool
    workspace: BlockRolloutItemListWorkspaceType0 | None
    created: BlockRolloutItemListCreated
    archived: bool
    reconciliation_running: bool
    effective_criticality: EffectiveCriticalityEnum | None
    url: str
    block: UUID
    block_name: str
    action_name: str
    status: BlockRolloutItemStatusEnum
    source: Source98DEnum
    retry_count: int
    dispatched_at: datetime.datetime | None
    completed_at: datetime.datetime | None
    rendered_target_version: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.block_rollout_item_list_organization_type_0 import (
            BlockRolloutItemListOrganizationType0,  # noqa: PLC0415
        )
        from ..models.block_rollout_item_list_workspace_type_0 import (
            BlockRolloutItemListWorkspaceType0,  # noqa: PLC0415
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
        if isinstance(self.organization, BlockRolloutItemListOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        organization_priority = self.organization_priority

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, BlockRolloutItemListWorkspaceType0):
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

        block = str(self.block)

        block_name = self.block_name

        action_name = self.action_name

        status: str = self.status

        source: str = self.source

        retry_count = self.retry_count

        dispatched_at: None | str
        if isinstance(self.dispatched_at, datetime.datetime):
            dispatched_at = self.dispatched_at.isoformat()
        else:
            dispatched_at = self.dispatched_at

        completed_at: None | str
        if isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        rendered_target_version: None | str
        rendered_target_version = self.rendered_target_version

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
                "block": block,
                "block_name": block_name,
                "action_name": action_name,
                "status": status,
                "source": source,
                "retry_count": retry_count,
                "dispatched_at": dispatched_at,
                "completed_at": completed_at,
                "rendered_target_version": rendered_target_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.block_rollout_item_list_active_condition_instances_item import (
            BlockRolloutItemListActiveConditionInstancesItem,  # noqa: PLC0415
        )
        from ..models.block_rollout_item_list_created import BlockRolloutItemListCreated  # noqa: PLC0415
        from ..models.block_rollout_item_list_organization_type_0 import (
            BlockRolloutItemListOrganizationType0,  # noqa: PLC0415
        )
        from ..models.block_rollout_item_list_workspace_type_0 import (
            BlockRolloutItemListWorkspaceType0,  # noqa: PLC0415
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
            active_condition_instances_item = BlockRolloutItemListActiveConditionInstancesItem.from_dict(
                active_condition_instances_item_data
            )

            active_condition_instances.append(active_condition_instances_item)

        def _parse_organization(data: object) -> BlockRolloutItemListOrganizationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = BlockRolloutItemListOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlockRolloutItemListOrganizationType0 | None, data)

        organization = _parse_organization(d.pop("organization"))

        organization_priority = d.pop("organization_priority")

        def _parse_workspace(data: object) -> BlockRolloutItemListWorkspaceType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = BlockRolloutItemListWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlockRolloutItemListWorkspaceType0 | None, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = BlockRolloutItemListCreated.from_dict(d.pop("created"))

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

        block = UUID(d.pop("block"))

        block_name = d.pop("block_name")

        action_name = d.pop("action_name")

        status = check_block_rollout_item_status_enum(d.pop("status"))

        source = check_source_98d_enum(d.pop("source"))

        retry_count = d.pop("retry_count")

        def _parse_dispatched_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dispatched_at_type_0 = datetime.datetime.fromisoformat(data)

                return dispatched_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        dispatched_at = _parse_dispatched_at(d.pop("dispatched_at"))

        def _parse_completed_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = datetime.datetime.fromisoformat(data)

                return completed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        completed_at = _parse_completed_at(d.pop("completed_at"))

        def _parse_rendered_target_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        rendered_target_version = _parse_rendered_target_version(d.pop("rendered_target_version"))

        block_rollout_item_list = cls(
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
            block=block,
            block_name=block_name,
            action_name=action_name,
            status=status,
            source=source,
            retry_count=retry_count,
            dispatched_at=dispatched_at,
            completed_at=completed_at,
            rendered_target_version=rendered_target_version,
        )

        block_rollout_item_list.additional_properties = d
        return block_rollout_item_list

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
