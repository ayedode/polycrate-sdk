from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.block_rollout_config_kind_enum import BlockRolloutConfigKindEnum, check_block_rollout_config_kind_enum
from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum
from ..models.trigger_type_enum import TriggerTypeEnum, check_trigger_type_enum

if TYPE_CHECKING:
    from ..models.block_rollout_config_list_active_condition_instances_item import (
        BlockRolloutConfigListActiveConditionInstancesItem,
    )
    from ..models.block_rollout_config_list_created import BlockRolloutConfigListCreated
    from ..models.block_rollout_config_list_organization_type_0 import BlockRolloutConfigListOrganizationType0
    from ..models.block_rollout_config_list_workspace_type_0 import BlockRolloutConfigListWorkspaceType0


T = TypeVar("T", bound="BlockRolloutConfigList")


@_attrs_define
class BlockRolloutConfigList:
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
            active_condition_instances (list[BlockRolloutConfigListActiveConditionInstancesItem]):
            organization (BlockRolloutConfigListOrganizationType0 | None):
            organization_priority (bool): True when the object's organization has priority=True.
            workspace (BlockRolloutConfigListWorkspaceType0 | None):
            created (BlockRolloutConfigListCreated):
            archived (bool): Archived objects are not shown in the UI and are not managed by the API.
            reconciliation_running (bool):
            effective_criticality (EffectiveCriticalityEnum | None):
            url (str): Gibt die absolute URL zum Object zurück.
            kind (BlockRolloutConfigKindEnum): * `trigger` - Trigger
                * `config` - Config Default: 'config'.
            block_name (None | str):
            active (bool):
            is_system_config (bool):  Default: False.
            trigger_type (None | TriggerTypeEnum):
            target_version (None | str):
            template_block (None | str):
            rendered_target_version (str): Renders target_version with system_config context for UI display.
                Workspace-specific variables are unavailable and will render as empty string.
            rendered_template_block (str): Renders template_block with system_config context for UI display.
                Workspace-specific variables are unavailable and will render as empty string.
            max_concurrent_percent (int): Maximum percentage of wave items to dispatch concurrently (1-100)
            failure_threshold_percent (int): Failure rate (%) above which the wave is blocked
            max_retries (int):
    """

    id: UUID
    name: str
    state: LastStateEnum
    labels: Any
    conditions: Any
    condition_instance_count: int
    active_condition_instances: list[BlockRolloutConfigListActiveConditionInstancesItem]
    organization: BlockRolloutConfigListOrganizationType0 | None
    organization_priority: bool
    workspace: BlockRolloutConfigListWorkspaceType0 | None
    created: BlockRolloutConfigListCreated
    archived: bool
    reconciliation_running: bool
    effective_criticality: EffectiveCriticalityEnum | None
    url: str
    block_name: None | str
    active: bool
    trigger_type: None | TriggerTypeEnum
    target_version: None | str
    template_block: None | str
    rendered_target_version: str
    rendered_template_block: str
    max_concurrent_percent: int
    failure_threshold_percent: int
    max_retries: int
    kind: BlockRolloutConfigKindEnum = "config"
    is_system_config: bool = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.block_rollout_config_list_organization_type_0 import BlockRolloutConfigListOrganizationType0
        from ..models.block_rollout_config_list_workspace_type_0 import BlockRolloutConfigListWorkspaceType0

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
        if isinstance(self.organization, BlockRolloutConfigListOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        organization_priority = self.organization_priority

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, BlockRolloutConfigListWorkspaceType0):
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

        kind: str = self.kind

        block_name: None | str
        block_name = self.block_name

        active = self.active

        is_system_config = self.is_system_config

        trigger_type: None | str
        if isinstance(self.trigger_type, str):
            trigger_type = self.trigger_type
        else:
            trigger_type = self.trigger_type

        target_version: None | str
        target_version = self.target_version

        template_block: None | str
        template_block = self.template_block

        rendered_target_version = self.rendered_target_version

        rendered_template_block = self.rendered_template_block

        max_concurrent_percent = self.max_concurrent_percent

        failure_threshold_percent = self.failure_threshold_percent

        max_retries = self.max_retries

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
                "kind": kind,
                "block_name": block_name,
                "active": active,
                "is_system_config": is_system_config,
                "trigger_type": trigger_type,
                "target_version": target_version,
                "template_block": template_block,
                "rendered_target_version": rendered_target_version,
                "rendered_template_block": rendered_template_block,
                "max_concurrent_percent": max_concurrent_percent,
                "failure_threshold_percent": failure_threshold_percent,
                "max_retries": max_retries,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.block_rollout_config_list_active_condition_instances_item import (
            BlockRolloutConfigListActiveConditionInstancesItem,
        )
        from ..models.block_rollout_config_list_created import BlockRolloutConfigListCreated
        from ..models.block_rollout_config_list_organization_type_0 import BlockRolloutConfigListOrganizationType0
        from ..models.block_rollout_config_list_workspace_type_0 import BlockRolloutConfigListWorkspaceType0

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
            active_condition_instances_item = BlockRolloutConfigListActiveConditionInstancesItem.from_dict(
                active_condition_instances_item_data
            )

            active_condition_instances.append(active_condition_instances_item)

        def _parse_organization(data: object) -> BlockRolloutConfigListOrganizationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = BlockRolloutConfigListOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlockRolloutConfigListOrganizationType0 | None, data)

        organization = _parse_organization(d.pop("organization"))

        organization_priority = d.pop("organization_priority")

        def _parse_workspace(data: object) -> BlockRolloutConfigListWorkspaceType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = BlockRolloutConfigListWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlockRolloutConfigListWorkspaceType0 | None, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = BlockRolloutConfigListCreated.from_dict(d.pop("created"))

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

        kind = check_block_rollout_config_kind_enum(d.pop("kind"))

        def _parse_block_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        block_name = _parse_block_name(d.pop("block_name"))

        active = d.pop("active")

        is_system_config = d.pop("is_system_config")

        def _parse_trigger_type(data: object) -> None | TriggerTypeEnum:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                trigger_type_type_0 = check_trigger_type_enum(data)

                return trigger_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TriggerTypeEnum, data)

        trigger_type = _parse_trigger_type(d.pop("trigger_type"))

        def _parse_target_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        target_version = _parse_target_version(d.pop("target_version"))

        def _parse_template_block(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        template_block = _parse_template_block(d.pop("template_block"))

        rendered_target_version = d.pop("rendered_target_version")

        rendered_template_block = d.pop("rendered_template_block")

        max_concurrent_percent = d.pop("max_concurrent_percent")

        failure_threshold_percent = d.pop("failure_threshold_percent")

        max_retries = d.pop("max_retries")

        block_rollout_config_list = cls(
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
            kind=kind,
            block_name=block_name,
            active=active,
            is_system_config=is_system_config,
            trigger_type=trigger_type,
            target_version=target_version,
            template_block=template_block,
            rendered_target_version=rendered_target_version,
            rendered_template_block=rendered_template_block,
            max_concurrent_percent=max_concurrent_percent,
            failure_threshold_percent=failure_threshold_percent,
            max_retries=max_retries,
        )

        block_rollout_config_list.additional_properties = d
        return block_rollout_config_list

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
