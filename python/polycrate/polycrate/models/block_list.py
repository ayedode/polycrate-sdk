from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.block_kind_enum import BlockKindEnum, check_block_kind_enum
from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.installation_status_enum import InstallationStatusEnum, check_installation_status_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum

if TYPE_CHECKING:
    from ..models.block_list_active_condition_instances_item import BlockListActiveConditionInstancesItem
    from ..models.block_list_created import BlockListCreated
    from ..models.block_list_organization_type_0 import BlockListOrganizationType0
    from ..models.block_list_workspace_type_0 import BlockListWorkspaceType0
    from ..models.block_simple import BlockSimple


T = TypeVar("T", bound="BlockList")


@_attrs_define
class BlockList:
    """Block List serializer - erbt von ManagedObjectListSerializer.

    Generische Felder (von ManagedObjectListSerializer):
    - id, name, state, organization, workspace, created, reconciliation_running, url

    Block-spezifische Felder:
    - kind, type, flavor, version, template_block, is_behind_stable, latest_stable

    Per .specs/0.11.4/dynamic-table-v2.md

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
            active_condition_instances (list[BlockListActiveConditionInstancesItem]):
            organization (BlockListOrganizationType0 | None):
            organization_priority (bool): True when the object's organization has priority=True.
            workspace (BlockListWorkspaceType0 | None):
            created (BlockListCreated):
            archived (bool): Archived objects are not shown in the UI and are not managed by the API.
            reconciliation_running (bool):
            effective_criticality (EffectiveCriticalityEnum | None):
            url (str): Gibt die absolute URL zum Object zurück.
            kind (BlockKindEnum): * `dockerapp` - Docker App
                * `linuxapp` - Linux App
                * `k8sapp` - Kubernetes App
                * `k8sappinstance` - Kubernetes App Instance
                * `k8scluster` - Kubernetes Cluster
                * `library` - Block Library
                * `generic` - Anything
            type_ (None | str):
            flavor (None | str):
            version (None | str):
            registry_url (None | str):
            template_block (BlockSimple):
            is_behind_stable (bool):
            latest_stable (None | str):
            template (bool):  Default: False.
            installed (bool): True if the block is currently installed
            installation_status (InstallationStatusEnum): * `idle` - Idle
                * `installing` - Installing
                * `uninstalling` - Uninstalling
                * `install_failed` - Install Failed
                * `uninstall_failed` - Uninstall Failed
            installed_version (None | str): Version that was last successfully installed via the install action
            update_needed (bool): True when the block is installed but installed_version differs from the desired version.
    """

    id: UUID
    name: str
    state: LastStateEnum
    labels: Any
    conditions: Any
    condition_instance_count: int
    active_condition_instances: list[BlockListActiveConditionInstancesItem]
    organization: BlockListOrganizationType0 | None
    organization_priority: bool
    workspace: BlockListWorkspaceType0 | None
    created: BlockListCreated
    archived: bool
    reconciliation_running: bool
    effective_criticality: EffectiveCriticalityEnum | None
    url: str
    kind: BlockKindEnum
    type_: None | str
    flavor: None | str
    version: None | str
    registry_url: None | str
    template_block: BlockSimple
    is_behind_stable: bool
    latest_stable: None | str
    installed: bool
    installation_status: InstallationStatusEnum
    installed_version: None | str
    update_needed: bool
    template: bool = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.block_list_organization_type_0 import BlockListOrganizationType0
        from ..models.block_list_workspace_type_0 import BlockListWorkspaceType0

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
        if isinstance(self.organization, BlockListOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        organization_priority = self.organization_priority

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, BlockListWorkspaceType0):
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

        type_: None | str
        type_ = self.type_

        flavor: None | str
        flavor = self.flavor

        version: None | str
        version = self.version

        registry_url: None | str
        registry_url = self.registry_url

        template_block = self.template_block.to_dict()

        is_behind_stable = self.is_behind_stable

        latest_stable: None | str
        latest_stable = self.latest_stable

        template = self.template

        installed = self.installed

        installation_status: str = self.installation_status

        installed_version: None | str
        installed_version = self.installed_version

        update_needed = self.update_needed

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
                "type": type_,
                "flavor": flavor,
                "version": version,
                "registry_url": registry_url,
                "template_block": template_block,
                "is_behind_stable": is_behind_stable,
                "latest_stable": latest_stable,
                "template": template,
                "installed": installed,
                "installation_status": installation_status,
                "installed_version": installed_version,
                "update_needed": update_needed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.block_list_active_condition_instances_item import BlockListActiveConditionInstancesItem
        from ..models.block_list_created import BlockListCreated
        from ..models.block_list_organization_type_0 import BlockListOrganizationType0
        from ..models.block_list_workspace_type_0 import BlockListWorkspaceType0
        from ..models.block_simple import BlockSimple

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
            active_condition_instances_item = BlockListActiveConditionInstancesItem.from_dict(
                active_condition_instances_item_data
            )

            active_condition_instances.append(active_condition_instances_item)

        def _parse_organization(data: object) -> BlockListOrganizationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = BlockListOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlockListOrganizationType0 | None, data)

        organization = _parse_organization(d.pop("organization"))

        organization_priority = d.pop("organization_priority")

        def _parse_workspace(data: object) -> BlockListWorkspaceType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = BlockListWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlockListWorkspaceType0 | None, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = BlockListCreated.from_dict(d.pop("created"))

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

        kind = check_block_kind_enum(d.pop("kind"))

        def _parse_type_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        type_ = _parse_type_(d.pop("type"))

        def _parse_flavor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        flavor = _parse_flavor(d.pop("flavor"))

        def _parse_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        version = _parse_version(d.pop("version"))

        def _parse_registry_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        registry_url = _parse_registry_url(d.pop("registry_url"))

        template_block = BlockSimple.from_dict(d.pop("template_block"))

        is_behind_stable = d.pop("is_behind_stable")

        def _parse_latest_stable(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        latest_stable = _parse_latest_stable(d.pop("latest_stable"))

        template = d.pop("template")

        installed = d.pop("installed")

        installation_status = check_installation_status_enum(d.pop("installation_status"))

        def _parse_installed_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        installed_version = _parse_installed_version(d.pop("installed_version"))

        update_needed = d.pop("update_needed")

        block_list = cls(
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
            type_=type_,
            flavor=flavor,
            version=version,
            registry_url=registry_url,
            template_block=template_block,
            is_behind_stable=is_behind_stable,
            latest_stable=latest_stable,
            template=template,
            installed=installed,
            installation_status=installation_status,
            installed_version=installed_version,
            update_needed=update_needed,
        )

        block_list.additional_properties = d
        return block_list

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
