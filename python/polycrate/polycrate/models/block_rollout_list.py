from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.block_rollout_status_enum import BlockRolloutStatusEnum, check_block_rollout_status_enum
from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum

if TYPE_CHECKING:
    from ..models.block_rollout_list_active_condition_instances_item import BlockRolloutListActiveConditionInstancesItem
    from ..models.block_rollout_list_created import BlockRolloutListCreated
    from ..models.block_rollout_list_organization_type_0 import BlockRolloutListOrganizationType0
    from ..models.block_rollout_list_rollout_config_data_type_0 import BlockRolloutListRolloutConfigDataType0
    from ..models.block_rollout_list_workspace_type_0 import BlockRolloutListWorkspaceType0


T = TypeVar("T", bound="BlockRolloutList")


@_attrs_define
class BlockRolloutList:
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
            active_condition_instances (list[BlockRolloutListActiveConditionInstancesItem]):
            organization (BlockRolloutListOrganizationType0 | None):
            organization_priority (bool): True when the object's organization has priority=True.
            workspace (BlockRolloutListWorkspaceType0 | None):
            created (BlockRolloutListCreated):
            archived (bool): Archived objects are not shown in the UI and are not managed by the API.
            reconciliation_running (bool):
            effective_criticality (EffectiveCriticalityEnum | None):
            url (str): Gibt die absolute URL zum Object zurück.
            batch_identifier (str):
            status (BlockRolloutStatusEnum): * `active` - Active
                * `paused` - Paused
                * `blocked` - Blocked
                * `completed` - Completed
                * `cancelled` - Cancelled
            total_items (int):
            dispatched_items (int):
            completed_items (int):
            failed_items (int):
            skipped_items_count (int): Live count of items that were skipped (e.g. cli_managed).
            failure_rate (float):
            last_item_added_at (datetime.datetime | None):
            rollout_config_data (BlockRolloutListRolloutConfigDataType0 | None):
    """

    id: UUID
    name: str
    state: LastStateEnum
    labels: Any
    conditions: Any
    condition_instance_count: int
    active_condition_instances: list[BlockRolloutListActiveConditionInstancesItem]
    organization: BlockRolloutListOrganizationType0 | None
    organization_priority: bool
    workspace: BlockRolloutListWorkspaceType0 | None
    created: BlockRolloutListCreated
    archived: bool
    reconciliation_running: bool
    effective_criticality: EffectiveCriticalityEnum | None
    url: str
    batch_identifier: str
    status: BlockRolloutStatusEnum
    total_items: int
    dispatched_items: int
    completed_items: int
    failed_items: int
    skipped_items_count: int
    failure_rate: float
    last_item_added_at: datetime.datetime | None
    rollout_config_data: BlockRolloutListRolloutConfigDataType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.block_rollout_list_organization_type_0 import BlockRolloutListOrganizationType0  # noqa: PLC0415
        from ..models.block_rollout_list_rollout_config_data_type_0 import (
            BlockRolloutListRolloutConfigDataType0,  # noqa: PLC0415
        )
        from ..models.block_rollout_list_workspace_type_0 import BlockRolloutListWorkspaceType0  # noqa: PLC0415

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
        if isinstance(self.organization, BlockRolloutListOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        organization_priority = self.organization_priority

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, BlockRolloutListWorkspaceType0):
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

        batch_identifier = self.batch_identifier

        status: str = self.status

        total_items = self.total_items

        dispatched_items = self.dispatched_items

        completed_items = self.completed_items

        failed_items = self.failed_items

        skipped_items_count = self.skipped_items_count

        failure_rate = self.failure_rate

        last_item_added_at: None | str
        if isinstance(self.last_item_added_at, datetime.datetime):
            last_item_added_at = self.last_item_added_at.isoformat()
        else:
            last_item_added_at = self.last_item_added_at

        rollout_config_data: dict[str, Any] | None
        if isinstance(self.rollout_config_data, BlockRolloutListRolloutConfigDataType0):
            rollout_config_data = self.rollout_config_data.to_dict()
        else:
            rollout_config_data = self.rollout_config_data

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
                "batch_identifier": batch_identifier,
                "status": status,
                "total_items": total_items,
                "dispatched_items": dispatched_items,
                "completed_items": completed_items,
                "failed_items": failed_items,
                "skipped_items_count": skipped_items_count,
                "failure_rate": failure_rate,
                "last_item_added_at": last_item_added_at,
                "rollout_config_data": rollout_config_data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.block_rollout_list_active_condition_instances_item import (
            BlockRolloutListActiveConditionInstancesItem,  # noqa: PLC0415
        )
        from ..models.block_rollout_list_created import BlockRolloutListCreated  # noqa: PLC0415
        from ..models.block_rollout_list_organization_type_0 import BlockRolloutListOrganizationType0  # noqa: PLC0415
        from ..models.block_rollout_list_rollout_config_data_type_0 import (
            BlockRolloutListRolloutConfigDataType0,  # noqa: PLC0415
        )
        from ..models.block_rollout_list_workspace_type_0 import BlockRolloutListWorkspaceType0  # noqa: PLC0415

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
            active_condition_instances_item = BlockRolloutListActiveConditionInstancesItem.from_dict(
                active_condition_instances_item_data
            )

            active_condition_instances.append(active_condition_instances_item)

        def _parse_organization(data: object) -> BlockRolloutListOrganizationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = BlockRolloutListOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlockRolloutListOrganizationType0 | None, data)

        organization = _parse_organization(d.pop("organization"))

        organization_priority = d.pop("organization_priority")

        def _parse_workspace(data: object) -> BlockRolloutListWorkspaceType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = BlockRolloutListWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlockRolloutListWorkspaceType0 | None, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = BlockRolloutListCreated.from_dict(d.pop("created"))

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

        batch_identifier = d.pop("batch_identifier")

        status = check_block_rollout_status_enum(d.pop("status"))

        total_items = d.pop("total_items")

        dispatched_items = d.pop("dispatched_items")

        completed_items = d.pop("completed_items")

        failed_items = d.pop("failed_items")

        skipped_items_count = d.pop("skipped_items_count")

        failure_rate = d.pop("failure_rate")

        def _parse_last_item_added_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_item_added_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_item_added_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_item_added_at = _parse_last_item_added_at(d.pop("last_item_added_at"))

        def _parse_rollout_config_data(data: object) -> BlockRolloutListRolloutConfigDataType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rollout_config_data_type_0 = BlockRolloutListRolloutConfigDataType0.from_dict(data)

                return rollout_config_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlockRolloutListRolloutConfigDataType0 | None, data)

        rollout_config_data = _parse_rollout_config_data(d.pop("rollout_config_data"))

        block_rollout_list = cls(
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
            batch_identifier=batch_identifier,
            status=status,
            total_items=total_items,
            dispatched_items=dispatched_items,
            completed_items=completed_items,
            failed_items=failed_items,
            skipped_items_count=skipped_items_count,
            failure_rate=failure_rate,
            last_item_added_at=last_item_added_at,
            rollout_config_data=rollout_config_data,
        )

        block_rollout_list.additional_properties = d
        return block_rollout_list

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
